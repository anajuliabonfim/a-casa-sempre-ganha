# =====================================================
#  🎰 A CASA SEMPRE GANHA · o tabuleiro
#  Um jogo de tabuleiro dentro de uma bet de mentira.
#  Baseado em Marques e Falcão (2026), Arcos Design.
# =====================================================
#  Pra rodar:  python -m streamlit run app.py
#
#  Como o Streamlit funciona (3 regrinhas):
#  1. A cada clique, ele roda ESTE arquivo inteiro de novo.
#  2. O que precisa sobreviver entre cliques fica em
#     st.session_state (aqui a gente chama de "jogo").
#  3. ir_para('tela') troca de tela e redesenha na hora.
# =====================================================

import random
import time

import streamlit as st

import conteudo as c

st.set_page_config(page_title='A Casa Sempre Ganha', page_icon='🎰', layout='centered')

TAMANHO = 20  # casas do tabuleiro: 0 é o início, 19 é a saída

# ---------- Visual (fonte Poppins + tons pastéis) ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');
html, body, p, li, label, input, textarea, h1, h2, h3, h4, .stMarkdown, .stButton button { font-family: 'Poppins', sans-serif !important; }
[data-testid="stIconMaterial"], .material-symbols-rounded, [class*="material-symbols"] { font-family: 'Material Symbols Rounded' !important; }}
.tabuleiro { display: grid; grid-template-columns: repeat(5, 1fr); gap: 6px; margin: 8px 0 4px; }
.casa { border-radius: 14px; padding: 6px 2px; text-align: center; font-size: 0.7rem;
        border: 2px solid transparent; min-height: 64px; color: #3D3550; }
.casa .emo { font-size: 1.4rem; line-height: 1.6rem; }
.casa.passou { opacity: 0.4; }
.casa.aqui { border: 3px solid #7C5CFF; box-shadow: 0 0 0 3px #E4DBFF; transform: scale(1.06); }
.maquina { background: #3D3550; border-radius: 20px; padding: 14px; text-align: center;
           font-size: 3rem; letter-spacing: 12px; margin: 10px 0; }
.carta { background: #FFFDF5; border: 3px solid #F4D35E; border-radius: 18px; padding: 16px 20px; margin: 8px 0; }
.carta h3 { margin: 0 0 6px; color: #7C5CFF; }
.popup { background: #FFDCDC; border: 3px dashed #FF7A7A; border-radius: 16px; padding: 14px;
         text-align: center; font-weight: 600; margin: 8px 0; }
.aviso { background: #FFF4C2; border-radius: 10px; padding: 4px 10px; font-size: 0.75rem; text-align: center; }
</style>
""", unsafe_allow_html=True)


# =====================================================
#  MEMÓRIA DO JOGO
# =====================================================
INICIAL = {
    'fase': 'inicio', 'nome': '',
    'saldo': 0, 'saldo_inicial': 0, 'bonus': 0,
    'pos': 0, 'dado': 0, 'tabuleiro': [], 'tipo': '',
    'evento': None, 'resolvido': False, 'msg': '', 'simbolos': '',
    'cartas': [], 'pergunta': None, 'acertou': False, 'depois_carta': 'tabuleiro',
    'apostas': 0, 'total_apostado': 0, 'quase': 0, 'recusas': 0,
    'escudo': False, 'oculto': 0, 'festa': False, 'contou': False, 'etica': 0, 'comissao': 0,
    'etapas': [], 'etapa': 0, 'voltas': 0, 'saque_final': False, 'sacou': False,
    'quiz': [], 'respostas': [],
}
for chave, valor in INICIAL.items():
    if chave not in st.session_state:
        st.session_state[chave] = valor
jogo = st.session_state


# =====================================================
#  FERRAMENTAS
# =====================================================
def ir_para(fase):
    jogo.fase = fase
    st.rerun()


def embaralhar(certa, erradas):
    opcoes = erradas + [certa]
    random.shuffle(opcoes)
    return opcoes


def montar_tabuleiro():
    """Lista com o tipo de cada casa. O meio é embaralhado a cada partida."""
    meio = []
    for tipo, info in c.CASAS.items():
        meio += [tipo] * info['quantidade']
    random.shuffle(meio)
    return ['inicio'] + meio + ['saida']


def desenhar_tabuleiro():
    html = "<div class='tabuleiro'>"
    for i, tipo in enumerate(jogo.tabuleiro):
        if tipo == 'inicio':
            emoji, nome, cor = '🏁', 'Início', '#F3EEFF'
        elif tipo == 'saida':
            emoji, nome, cor = '🏦', 'SAÍDA', '#C8F0D0'
        else:
            info = c.CASAS[tipo]
            emoji, nome, cor = info['emoji'], info['nome'], info['cor']
        classe = 'casa'
        if i < jogo.pos:
            classe += ' passou'
        if i == jogo.pos:
            classe += ' aqui'
            emoji = '🧍‍♀️'
        html += (f"<div class='{classe}' style='background:{cor}'>"
                 f"<div class='emo'>{emoji}</div><b>{i}</b> {nome}</div>")
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)


def mostrar_status():
    col1, col2, col3 = st.columns(3)
    if jogo.oculto > 0:
        col1.metric('💰 Saldo', 'R$ ****')
    else:
        col1.metric('💰 Saldo', f'R$ {jogo.saldo}')
    col2.metric('🃏 Cartas', f'{len(jogo.cartas)} de {len(c.CARTAS)}')
    col3.metric('🛡️ Escudo', 'Ativo' if jogo.escudo else 'Não')


def girar_maquina(chance):
    """Gira o caça-níquel com animação. Devolve 'ganhou', 'quase' ou 'perdeu'."""
    tela = st.empty()
    for _ in range(10):
        tela.markdown(f"<div class='maquina'>{' '.join(random.choices(c.SIMBOLOS, k=3))}</div>",
                      unsafe_allow_html=True)
        time.sleep(0.08)
    if random.random() < chance:
        s = random.choice(c.SIMBOLOS)
        jogo.simbolos, tipo = f'{s} {s} {s}', 'ganhou'
    elif random.random() < 0.6:
        s = random.choice(c.SIMBOLOS)
        outro = random.choice([x for x in c.SIMBOLOS if x != s])
        jogo.simbolos, tipo = f'{s} {s} {outro}', 'quase'
        jogo.quase += 1
    else:
        jogo.simbolos, tipo = ' '.join(random.sample(c.SIMBOLOS, 3)), 'perdeu'
    return tipo


def apostar(valor, chance=c.CHANCE_GANHAR, pagamento=c.PAGAMENTO):
    """Faz uma aposta completa e devolve o texto do resultado."""
    jogo.apostas += 1
    jogo.total_apostado += valor
    resultado = girar_maquina(chance)
    if resultado == 'ganhou':
        premio = valor * pagamento
        jogo.saldo += premio - valor
        jogo.festa = True
        return f'🔊 PLIM PLIM PLIM! 🎉 **GANHOU R$ {premio}!**'
    texto = perder(valor)
    if resultado == 'quase':
        return f'🔊 PLIM PLIM... 😱 **QUASE!!!** Faltou só UM! {texto}'
    return f'Não foi dessa vez. {texto}'


def perder(valor):
    if jogo.escudo:
        jogo.escudo = False
        return f'🛡️ O Escudo da Lei devolveu seus R$ {valor}. (Escudo usado)'
    jogo.saldo -= valor
    return f'Você perdeu R$ {valor}.'


def resolver(msg):
    jogo.msg = msg
    jogo.resolvido = True
    st.rerun()


def abrir_pergunta(tipo, depois):
    """Se a pessoa ainda não tem a carta desse tipo, faz a pergunta."""
    jogo.depois_carta = depois
    if tipo in jogo.cartas:
        ir_para(depois)
    v = random.choice(c.CARTAS[tipo]['perguntas'])
    jogo.pergunta = {'tipo': tipo, 'texto': v['pergunta'], 'certa': v['certa'],
                     'opcoes': embaralhar(v['certa'], v['erradas'])}
    ir_para('pergunta')


def carta_html(conceito, definicao, exemplo, artigo=None):
    extra = f'<br><br>📖 <b>No artigo:</b> {artigo}' if artigo else ''
    st.markdown(f"<div class='carta'><h3>🃏 {conceito}</h3>{definicao}"
                f"<br><br>💡 <b>No dia a dia:</b> {exemplo}{extra}</div>",
                unsafe_allow_html=True)


def simular_jogadores(qtd=1000, apostas=8, valor=20):
    """1.000 pessoas jogando com AS MESMAS regras do caça-níquel deste jogo."""
    perderam, lucro_casa = 0, 0
    for _ in range(qtd):
        saldo = c.SALDO_INICIAL
        for _ in range(apostas):
            if saldo < valor:
                break
            if random.random() < c.CHANCE_GANHAR:
                saldo += valor * (c.PAGAMENTO - 1)
            else:
                saldo -= valor
        if saldo < c.SALDO_INICIAL:
            perderam += 1
        lucro_casa += c.SALDO_INICIAL - saldo
    return perderam, lucro_casa


def comecar_saque(final):
    jogo.saque_final = final
    jogo.etapas = random.sample(c.ETAPAS_SAQUE, 3)
    jogo.etapa = 0
    ir_para('saque')


def preparar_quiz():
    jogo.quiz = []
    for pergunta, certa, erradas in random.sample(c.QUIZ, 3):
        jogo.quiz.append({'pergunta': pergunta, 'certa': certa,
                          'opcoes': embaralhar(certa, erradas)})
    ir_para('quiz')


# =====================================================
#  BARRA LATERAL: regras e créditos (sempre visível)
# =====================================================
with st.sidebar:
    st.markdown('## 🎰 A Casa Sempre Ganha')
    with st.expander('📜 Manual do jogo', expanded=False):
        st.markdown(c.MANUAL)
    if jogo.cartas:
        st.markdown('**🃏 Meu álbum**')
        for tipo in sorted(jogo.cartas, key=lambda t: c.CARTAS[t]['conceito']):
            with st.expander(f"{c.CASAS[tipo]['emoji']} {c.CARTAS[tipo]['conceito']}"):
                st.write(c.CARTAS[tipo]['definicao'])
    st.divider()
    st.caption('📄 Baseado em: ' + c.REFERENCIA)
    st.markdown(f'[Ler o artigo]({c.LINK_ARTIGO})')
    st.caption('👩‍💻 ' + ' · '.join(c.EQUIPE))
    st.caption(f'{c.DISCIPLINA} · {c.PROFESSORA}\n\n{c.CURSO} · {c.UNIVERSIDADE}')

fase = jogo.fase


# =====================================================
#  TELA INICIAL
# =====================================================
if fase == 'inicio':
    st.title('🎰 A Casa Sempre Ganha')
    st.subheader('Um jogo de tabuleiro dentro de uma bet de mentira')
    st.write('Atravesse o tabuleiro da **SorteJá.bet** e tente sair com dinheiro no bolso. '
             'Parece fácil. Mas cada casa esconde um **truque de verdade**, contado por quem '
             'cria as bets.')
    st.caption('Nenhum dinheiro de verdade aqui. 😉 Cada partida é diferente.')
    with st.expander('📜 Ler as regras (1 minutinho)'):
        st.markdown(c.MANUAL)
    nome = st.text_input('Qual é o seu nome?')
    if st.button('🎲 Começar', type='primary', disabled=not nome.strip()):
        jogo.nome = nome.strip().title()
        jogo.bonus = random.choice(c.BONUS_BOAS_VINDAS)
        jogo.saldo = c.SALDO_INICIAL + jogo.bonus
        jogo.saldo_inicial = jogo.saldo
        jogo.tabuleiro = montar_tabuleiro()
        ir_para('intro')


# =====================================================
#  INTRODUÇÃO (pra quem nunca ouviu falar do assunto)
# =====================================================
elif fase == 'intro':
    st.header('Antes de entrar: o que é uma bet? 🤔')
    st.write('**Bets** são sites e apps de apostas: você coloca dinheiro tentando acertar um '
             'resultado, como um jogo de futebol ou um caça-níquel.')
    col1, col2 = st.columns(2)
    col1.metric('💸 Movimentados por mês no Brasil', '≈ R$ 30 bi')
    col2.metric('📉 Apostadores com dívida atrasada', '42%')
    st.caption('Banco Central (2025) e DataSenado (2024), citados no artigo.')
    st.info('📄 **De onde vem este jogo:** os pesquisadores Daniel Marques (UFRB) e Thiago Falcão '
            '(UFPB) entrevistaram **5 profissionais que criam bets**. Eles contaram os truques que '
            'colocam nas telas. Você vai sentir esses truques na pele.')
    st.success(f'🎁 Bem-vindo(a), {jogo.nome}! Você ganhou **R$ {jogo.bonus} de bônus**. '
               f'Seu saldo: **R$ {jogo.saldo}**. Sem cadastro, um clique e pronto! 💸')
    st.caption('Reparou como foi fácil entrar? Guarda essa sensação. 👀')
    if st.button('Entrar no tabuleiro 🎲', type='primary'):
        ir_para('tabuleiro')


# =====================================================
#  TABULEIRO
# =====================================================
elif fase == 'tabuleiro':
    st.markdown("<div class='aviso'>⚠️ Jogue com responsabilidade · SorteJá.bet</div>",
                unsafe_allow_html=True)
    st.header(f'🎲 Vez de {jogo.nome}')
    mostrar_status()
    desenhar_tabuleiro()
    if jogo.oculto > 0:
        st.caption('🙈 Seu saldo está escondido por causa do Apagão.')

    if st.button('🎲 Rolar o dado', type='primary'):
        jogo.dado = random.randint(1, 6)
        jogo.pos = min(jogo.pos + jogo.dado, TAMANHO - 1)
        if jogo.oculto > 0:
            jogo.oculto -= 1
        jogo.tipo = jogo.tabuleiro[jogo.pos]
        jogo.resolvido = False
        jogo.msg = ''
        jogo.simbolos = ''
        jogo.contou = False
        if jogo.tipo == 'apagao':
            jogo.oculto = 3  # esta rodada + as 2 próximas
        if jogo.tipo == 'saida':
            comecar_saque(final=True)
        # sorteia o conteúdo do evento dessa casa
        if jogo.tipo == 'notificacao':
            jogo.evento = random.choice(c.NOTIFICACOES)
        elif jogo.tipo == 'relampago':
            jogo.evento = random.choice(c.OFERTAS)
        elif jogo.tipo == 'influencer':
            jogo.evento = random.choice(c.INFLUENCERS)
        elif jogo.tipo == 'bastidores':
            jogo.evento = random.choice(c.PEDIDOS)
        else:
            jogo.evento = None
        ir_para('casa')


# =====================================================
#  A CASA ONDE VOCÊ CAIU
# =====================================================
elif fase == 'casa':
    tipo = jogo.tipo
    info = c.CASAS[tipo]
    st.caption(f'🎲 Você tirou {jogo.dado} e caiu na casa {jogo.pos}')
    st.header(f"{info['emoji']} {info['nome']}")
    mostrar_status()

    # ---------- resultado (depois que a pessoa escolheu) ----------
    if jogo.resolvido:
        if jogo.simbolos:
            st.markdown(f"<div class='maquina'>{jogo.simbolos}</div>", unsafe_allow_html=True)
        if jogo.festa:
            st.balloons()
            jogo.festa = False
        st.info(jogo.msg)
        if st.button('Continuar ➡️', type='primary'):
            if jogo.saldo <= 0:
                abrir_pergunta(tipo, depois='quebrou')
            abrir_pergunta(tipo, depois='tabuleiro')

    # ---------- 🎰 CAÇA-NÍQUEL ----------
    elif tipo == 'cassino':
        st.write('Três símbolos iguais pagam **3x** o que você apostar. Quanto vai ser?')
        st.markdown("<div class='maquina'>❔ ❔ ❔</div>", unsafe_allow_html=True)
        cols = st.columns(4)
        for col, valor in zip(cols, [10, 20, 50]):
            if col.button(f'R$ {valor}', disabled=valor > jogo.saldo):
                resolver(apostar(valor))
        if cols[3].button('Não apostar'):
            jogo.recusas += 1
            resolver('😢 *"Tem certeza? A máquina tava quente, ia sair agora!"*\n\n'
                     'Você não apostou. Repara: até pra não jogar a bet tenta te fazer sentir culpa.')

    # ---------- 🎟️ RASPADINHA ----------
    elif tipo == 'raspadinha':
        st.write('Cada bilhete custa **R$ 10**. Um deles pode ter um prêmio. Escolhe um!')
        cols = st.columns(3)
        for i, col in enumerate(cols):
            if col.button(f'🎟️ Bilhete {i + 1}', disabled=jogo.saldo < 10):
                jogo.apostas += 1
                jogo.total_apostado += 10
                if random.random() < 0.2:
                    jogo.saldo += 30
                    resolver(f'✨ Você raspou o bilhete {i + 1}: **R$ 40!** Ganhou! 🎉')
                jogo.quase += 1
                vizinho = random.choice([n for n in [1, 2, 3] if n != i + 1])
                resolver(f'Você raspou o bilhete {i + 1}: nada. 😩 {perder(10)}\n\n'
                         f'👀 E olha só... o **bilhete {vizinho} tinha R$ 100!** Foi por pouco!')
        if st.button('Não comprar'):
            jogo.recusas += 1
            resolver('Você passou. Mas a tela continua piscando: *"ÚLTIMOS BILHETES PREMIADOS!"*')

    # ---------- 🔔 NOTIFICAÇÃO ----------
    elif tipo == 'notificacao':
        promessa, verdade = jogo.evento
        st.markdown(f"<div class='popup'>📱 SorteJá.bet · agora<br><span style='font-size:1.4rem'>"
                    f"{promessa}</span><br><small>toque pra resgatar</small></div>",
                    unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        if col1.button('🎁 Resgatar prêmio', disabled=jogo.saldo < 10):
            resolver(f'Era pegadinha: **{verdade}**. Você depositou e girou...\n\n{apostar(10)}')
        if col2.button('Ignorar'):
            jogo.recusas += 1
            resolver(f'Boa! A letra miúda dizia: *{verdade}*.\n\n'
                     'Enquanto você lia isso, chegaram mais 2 notificações iguais. 📱📱')

    # ---------- ⏰ OFERTA RELÂMPAGO ----------
    elif tipo == 'relampago':
        st.markdown(f"<div class='popup'>🔥 OFERTA RELÂMPAGO 🔥<br>{jogo.evento}</div>",
                    unsafe_allow_html=True)
        relogio = st.empty()
        if not jogo.contou:  # conta só na primeira vez, senão repetia a cada clique
            for s in range(5, 0, -1):
                relogio.markdown(f"<h2 style='text-align:center'>⏰ {s}</h2>", unsafe_allow_html=True)
                time.sleep(0.5)
            jogo.contou = True
        relogio.markdown("<h2 style='text-align:center'>⏰ ÚLTIMA CHANCE!</h2>",
                         unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        if col1.button('⚡ APOSTAR R$ 30 AGORA', disabled=jogo.saldo < 30):
            resolver(apostar(30, pagamento=2) + '\n\n(O "dobro" pagava MENOS que o caça-níquel normal. 🤫)')
        if col2.button('Deixar passar'):
            jogo.recusas += 1
            resolver('Você deixou passar. E adivinha: a mesma "oferta única" volta amanhã. 😉')

    # ---------- 🤳 INFLUENCER ----------
    elif tipo == 'influencer':
        perfil, post = jogo.evento
        st.markdown(f"<div class='carta'>🤳 <b>{perfil}</b><br>{post}<br><br>"
                    f"🧾 <i>[print de PIX: R$ 5.000,00]</i></div>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        if col1.button('Copiar a aposta (R$ 50)', disabled=jogo.saldo < 50):
            resolver(apostar(50, chance=0.15) + '\n\n🕵️ Depois você descobre: o print era montado '
                     'e o influencer ganha uma comissão a cada pessoa que perde pelo link dele.')
        if col2.button('Desconfiar'):
            jogo.recusas += 1
            resolver('Boa! 🕵️ O print era montado. E o influencer ganha comissão de quem perde pelo link.')

    # ---------- 🙈 APAGÃO ----------
    elif tipo == 'apagao':
        st.write('💡 Ops... **seu saldo sumiu da tela!** Ele fica escondido pelas próximas 2 rodadas.')
        st.markdown("<div class='popup'>⚡ Aposta rápida de R$ 20? É só um clique!</div>",
                    unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        if col1.button('Apostar R$ 20', disabled=jogo.saldo < 20):
            resolver(apostar(20) + '\n\nE aí, você sabe quanto tem agora? Pois é. 🙈')
        if col2.button('Não apostar'):
            jogo.recusas += 1
            resolver('Você não apostou. Mas repara: sem ver o saldo, fica muito mais difícil decidir.')

    # ---------- 💸 CAIXA ----------
    elif tipo == 'caixa':
        st.write('Aqui você pode **sacar seu dinheiro e sair do jogo** agora mesmo. '
                 'Sair cedo também é uma estratégia.')
        col1, col2 = st.columns(2)
        if col1.button('💸 Sacar e sair'):
            comecar_saque(final=False)
        if col2.button('Seguir jogando'):
            etapas = ', '.join(random.sample(c.ETAPAS_SAQUE, 3)).lower()
            resolver(f'Você seguiu. Só pra saber: pra sacar você teria que {etapas}. '
                     'Já pra apostar de novo... é só um clique. 😉')

    # ---------- 👔 BASTIDORES ----------
    elif tipo == 'bastidores':
        st.write('🔄 **Plot twist!** Por uma rodada você trabalha na agência que cria a SorteJá.bet.')
        st.warning(f'👔 **CHEFE:** "{jogo.evento["pedido"]}"')
        col1, col2 = st.columns(2)
        if col1.button('Faço (+R$ 20 de comissão)'):
            jogo.saldo += 20
            jogo.comissao += 20
            resolver(f'📈 Meta batida, comissão no bolso. E mais gente presa no app.\n\n'
                     f'📖 **Isso aconteceu de verdade:** {jogo.evento["artigo"]}')
        if col2.button('Recuso e questiono'):
            jogo.etica += 1
            resolver(f'🛡️ +1 de ética. Mas o chefe ficou de cara feia...\n\n'
                     f'📖 **Isso aconteceu de verdade:** {jogo.evento["artigo"]}\n\n'
                     '🗣️ O P5 resumiu: *"eu não deixava a minha cadeira limitar os meus argumentos"*.')

    # ---------- ⚖️ LEI ----------
    elif tipo == 'lei':
        st.write('Você encontrou a **Lei 14.790/2023** e a **Portaria 722/2024**. Elas obrigam as bets '
                 'a ter aviso de "jogue com responsabilidade", limite de gasto, autoexclusão e '
                 'contador de tempo.')
        if st.button('🛡️ Pegar o Escudo da Lei', type='primary'):
            jogo.escudo = True
            resolver('Você ganhou o 🛡️ **Escudo da Lei**: ele devolve sua próxima perda.\n\n'
                     'Mas repara: a lei te protege UMA vez. Os pop-ups, sons e contadores continuam todos lá.')


# =====================================================
#  "QUE TRUQUE FOI ESSE?" + CARTA
# =====================================================
elif fase == 'pergunta':
    p = jogo.pergunta
    st.header('🕵️ Que truque foi esse?')
    st.caption('Não precisa saber nada antes. Usa o bom senso!')
    resposta = st.radio(p['texto'], p['opcoes'], index=None)
    if st.button('Responder', type='primary', disabled=resposta is None):
        jogo.acertou = resposta == p['certa']
        jogo.cartas.append(p['tipo'])
        ir_para('carta')


elif fase == 'carta':
    p = jogo.pergunta
    carta = c.CARTAS[p['tipo']]
    if jogo.acertou:
        st.success('✅ Isso! Você desmascarou o truque.')
    else:
        st.warning(f"Quase! A resposta era: **{p['certa']}**")
    st.subheader('🃏 Carta nova no álbum!')
    carta_html(carta['conceito'], carta['definicao'], carta['exemplo'], carta['artigo'])
    st.caption(f'Álbum: {len(jogo.cartas)} de {len(c.CARTAS)} cartas')
    if st.button('Continuar ➡️', type='primary'):
        ir_para(jogo.depois_carta)


# =====================================================
#  SAQUE (a fricção na prática)
# =====================================================
elif fase == 'saque':
    st.header('🏦 Sacar meu dinheiro')
    mostrar_status()
    total = len(jogo.etapas)
    if jogo.etapa < total:
        st.progress(jogo.etapa / total, text=f'Etapa {jogo.etapa + 1} de {total}')
        st.write(f'📋 **{jogo.etapas[jogo.etapa]}**')
        st.markdown(f"<div class='popup'>{random.choice(c.POPUPS_SAQUE)}</div>",
                    unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        if col1.button('Continuar o saque ➡️'):
            jogo.etapa += 1
            st.rerun()
        pode_ficar = not (jogo.saque_final and jogo.voltas >= 1)  # na saída, só 1 volta extra
        if pode_ficar and col2.button('Ficar e ganhar R$ 20 🎁'):
            jogo.saldo += 20
            if jogo.saque_final:
                jogo.voltas += 1
                jogo.pos = 0  # volta pro começo do tabuleiro
                jogo.tabuleiro = montar_tabuleiro()
            jogo.tipo = 'caixa'
            jogo.msg = ('🎁 R$ 20 de bônus! Você desistiu do saque e continua no jogo.'
                        + (' E voltou pro começo do tabuleiro. 🔁' if jogo.saque_final else ''))
            jogo.simbolos = ''
            jogo.resolvido = True
            if jogo.saque_final:
                abrir_pergunta('caixa', depois='tabuleiro')
            ir_para('casa')
    else:
        st.success(f'✅ Saque aprovado! Você saiu com **R$ {jogo.saldo}**. Ufa! 😮‍💨')
        jogo.sacou = True
        st.caption('Contou quantas etapas foram pra sair? E quantas pra entrar? (nenhuma)')
        if st.button('Ver meu resultado ➡️', type='primary'):
            abrir_pergunta('caixa', depois='raiox')


# =====================================================
#  SALDO ZEROU
# =====================================================
elif fase == 'quebrou':
    st.header('💸 Seu saldo acabou')
    st.error('A SorteJá.bet te capturou. Mas calma: a culpa não é só sua.')
    st.write('O artigo mostra que essa tela foi **projetada** pra isso. A pergunta certa não é '
             '"por que você não parou?", e sim "como a plataforma fez parar ficar tão difícil?".')
    if st.button('Ver o Raio-X ➡️', type='primary'):
        ir_para('raiox')


# =====================================================
#  RAIO-X + SIMULAÇÃO
# =====================================================
elif fase == 'raiox':
    st.header('🔍 Raio-X: tudo que a bet sabia sobre você')
    col1, col2 = st.columns(2)
    col1.metric('🎲 Apostas feitas', jogo.apostas)
    col2.metric('💸 Total apostado', f'R$ {jogo.total_apostado}')
    col3, col4 = st.columns(2)
    col3.metric('😬 Vezes que "quase ganhou"', jogo.quase)
    col4.metric('🙅 Vezes que recusou', jogo.recusas)
    st.metric(f'💰 Entrou com R$ {jogo.saldo_inicial}, saiu com', f'R$ {max(jogo.saldo, 0)}',
              delta=max(jogo.saldo, 0) - jogo.saldo_inicial)
    if jogo.comissao:
        st.caption(f'(R$ {jogo.comissao} disso veio da comissão dos Bastidores, '
                   'ou seja, do prejuízo de outros apostadores.)')
    st.write('A plataforma sabia tudo isso o tempo todo. **Você sabia?**')

    st.subheader('🧮 E se 1.000 pessoas jogassem?')
    st.caption('Mesmas regras do caça-níquel deste jogo: 8 apostas de R$ 20 cada.')
    if st.button('Simular 1.000 jogadores'):
        with st.spinner('Simulando...'):
            time.sleep(1)
        perderam, lucro = simular_jogadores()
        st.error(f'❌ **{perderam} de 1.000** saíram perdendo')
        st.metric('🏦 A CASA LUCROU', f'R$ {lucro:,}'.replace(',', '.'))
        st.caption('Alguns ganham, sim. Mas no conjunto quem sempre lucra é a casa. Daí o nome do jogo.')
    if st.button('Ver meu álbum ➡️', type='primary'):
        ir_para('album')


# =====================================================
#  ÁLBUM + CARTA BÔNUS
# =====================================================
elif fase == 'album':
    st.header('🃏 Seu álbum de truques')
    st.write(f'Você desmascarou **{len(jogo.cartas)} de {len(c.CARTAS)}** truques.')
    faltam = [t for t in c.CARTAS if t not in jogo.cartas]
    if faltam:
        st.caption('Faltaram: ' + ', '.join(sorted(c.CARTAS[t]['conceito'] for t in faltam))
                   + '. Joga de novo pra completar!')
    st.subheader('⭐ Carta bônus: a grande ideia do artigo')
    f = c.CARTA_FINAL
    carta_html(f['conceito'], f['definicao'], f['exemplo'])
    if st.button('Quiz final (3 perguntas) ⚡', type='primary'):
        preparar_quiz()


# =====================================================
#  QUIZ
# =====================================================
elif fase == 'quiz':
    st.header('⚡ Quiz relâmpago')
    st.caption('Tudo aqui apareceu no jogo. Você consegue!')
    respostas = []
    for i, q in enumerate(jogo.quiz):
        respostas.append(st.radio(q['pergunta'], q['opcoes'], index=None, key=f'q{i}'))
    if st.button('Ver resultado', type='primary', disabled=None in respostas):
        jogo.respostas = respostas
        ir_para('fim')


# =====================================================
#  FIM
# =====================================================
elif fase == 'fim':
    pontos = sum(r == q['certa'] for q, r in zip(jogo.quiz, jogo.respostas))
    cartas = len(jogo.cartas)
    if cartas >= 7 and pontos >= 2:
        selo = '🕵️ Detetive das Bets'
    elif cartas >= 4:
        selo = '🔍 Aprendiz de Detetive'
    else:
        selo = '🎰 Ainda preso(a) no app'

    st.title(f'Fim de jogo, {jogo.nome}!')
    st.header(selo)
    col1, col2, col3 = st.columns(3)
    col1.metric('💰 Saldo final', f'R$ {max(jogo.saldo, 0)}')
    col2.metric('🃏 Cartas', f'{cartas} de {len(c.CARTAS)}')
    col3.metric('⚡ Quiz', f'{pontos} de 3')
    if jogo.etica:
        st.caption(f'👔 Nos Bastidores você recusou {jogo.etica} pedido(s) enganoso(s).')

    st.subheader('Revisando o quiz')
    for q, r in zip(jogo.quiz, jogo.respostas):
        st.write(f"{'✅' if r == q['certa'] else '❌'} **{q['pergunta']}** {q['certa']}")

    st.info('**O que levar daqui:** a bet não é neutra. Cada som, pop-up e contador foi desenhado '
            'por alguém, com meta pra bater. Por isso o vício não é só culpa de quem aposta, e as '
            'regras precisam cuidar também do **design** das telas.')
    st.caption('💛 Se apostar deixou de ser diversão pra você ou alguém próximo, procure ajuda: '
               'o CAPS da sua cidade ou os Jogadores Anônimos.')

    if st.button('🔄 Jogar de novo (tabuleiro novo)', type='primary'):
        st.session_state.clear()
        st.rerun()

    st.divider()
    st.caption('📄 ' + c.REFERENCIA)
    st.link_button('Ler o artigo completo', c.LINK_ARTIGO)
    st.caption('👩‍💻 ' + ' · '.join(c.EQUIPE))
