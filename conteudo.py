# =====================================================
#  conteudo.py : TODO o texto do jogo mora aqui.
#  Quer mudar uma pergunta, uma fala do artigo ou um pedido
#  do chefe? Mexe SÓ aqui. O app.py cuida das regras e da tela.
# =====================================================

# ---------------- CRÉDITOS ----------------
EQUIPE = [  # em ordem alfabética
    'Ana Júlia Bonfim',
    'Gabriela Nóbrega',
    'Kédynna Dantas',
    'Manoel Medeiros',
]
DISCIPLINA = 'Leitura e Produção de Texto'
PROFESSORA = 'Profa. Suéllen Rodrigues Ramos da Silva'
CURSO = 'Ciência da Computação · P1, manhã · 2026.2'
UNIVERSIDADE = 'UEPB · Campus VII'
REFERENCIA = ('MARQUES, Daniel; FALCÃO, Thiago. Design persuasivo e mediação tecnológica '
              'em plataformas digitais de apostas: práticas e dilemas éticos de designers '
              'e desenvolvedores. Arcos Design, v. 19, n. 1, 2026.')
LINK_ARTIGO = 'https://doi.org/10.12957/arcosdesign.2026.93891'

# ---------------- REGRAS DE DINHEIRO ----------------
SALDO_INICIAL = 100
BONUS_BOAS_VINDAS = [20, 30, 50]   # sorteado no começo
CHANCE_GANHAR = 0.25               # 1 em 4 no caça-níquel
PAGAMENTO = 3                      # ganhou? recebe 3x o que apostou
SIMBOLOS = ['🍒', '🍋', '💎', '🔔', '🍀']

# ---------------- AS CASAS DO TABULEIRO ----------------
# quantidade = quantas casas desse tipo aparecem no tabuleiro (fora início e fim)
CASAS = {
    'apagao':      {'nome': 'Apagão',            'emoji': '🙈', 'cor': '#E3E3F5', 'quantidade': 1},
    'bastidores':  {'nome': 'Bastidores',        'emoji': '👔', 'cor': '#FFE3EC', 'quantidade': 2},
    'caixa':       {'nome': 'Caixa',             'emoji': '💸', 'cor': '#DFF5E1', 'quantidade': 2},
    'cassino':     {'nome': 'Caça-níquel',       'emoji': '🎰', 'cor': '#FFF4C2', 'quantidade': 4},
    'influencer':  {'nome': 'Influencer',        'emoji': '🤳', 'cor': '#FFE6D5', 'quantidade': 2},
    'lei':         {'nome': 'Lei',               'emoji': '⚖️', 'cor': '#DDEEFF', 'quantidade': 1},
    'notificacao': {'nome': 'Notificação',       'emoji': '🔔', 'cor': '#EFE3FF', 'quantidade': 2},
    'raspadinha':  {'nome': 'Raspadinha',        'emoji': '🎟️', 'cor': '#E0F7F5', 'quantidade': 2},
    'relampago':   {'nome': 'Oferta relâmpago',  'emoji': '⏰', 'cor': '#FFDCDC', 'quantidade': 2},
}

# ---------------- AS CARTAS DO ÁLBUM ----------------
# Cada tipo de casa ensina UM conceito do artigo.
# A pessoa vive o truque, tenta adivinhar o porquê e ganha a carta.
CARTAS = {
    'cassino': {
        'conceito': 'Captura afetiva',
        'definicao': 'A bet mexe com as suas emoções (empolgação, expectativa, frio na barriga) '
                     'pra você continuar jogando. A decisão deixa de ser pensada e vira sentimento.',
        'exemplo': 'É como a notificação de curtida: dá aquele friozinho e você quer mais.',
        'artigo': 'Um supervisor de design (P1) disse que "a comunicação do design às vezes '
                  'funciona abaixo do nível racional da gente". Sons de vitória e de quase-acerto '
                  'são feitos pra isso.',
        'perguntas': [
            {'pergunta': 'Quando deu QUASE, a tela comemorou. Por que a bet faria isso?',
             'certa': 'Pra eu sentir que tô perto e tentar de novo',
             'erradas': ['Pra comemorar comigo', 'Foi sem querer']},
            {'pergunta': 'Por que tem som e brilho até quando você perde?',
             'certa': 'Pra manter minha empolgação lá em cima',
             'erradas': ['Só pra deixar bonito', 'Foi um erro do programa']},
        ],
    },
    'raspadinha': {
        'conceito': 'Recompensa variável',
        'definicao': 'Você nunca sabe QUANDO o prêmio vem. Essa incerteza prende muito mais do '
                     'que um prêmio certo, porque a próxima tentativa sempre "pode ser a boa".',
        'exemplo': 'É como atualizar o e-mail esperando uma resposta importante.',
        'artigo': 'Um game designer de raspadinhas online (P3) contou que esses jogos são feitos '
                  'pra estimular o jogador "visualmente, mentalmente, emocionalmente".',
        'perguntas': [
            {'pergunta': 'A raspadinha do lado tinha R$ 100. Por que mostrar isso pra você?',
             'certa': 'Pra eu achar que quase acertei e comprar outra',
             'erradas': ['Pra ser honesta comigo', 'Pra me ensinar a escolher']},
            {'pergunta': 'Ganhar de vez em quando, sem saber quando, faz o quê com a gente?',
             'certa': 'Deixa a gente ansioso pela próxima tentativa',
             'erradas': ['Ensina uma estratégia', 'Nada, é só sorte']},
        ],
    },
    'notificacao': {
        'conceito': 'Dark patterns',
        'definicao': 'São truques de tela pra você decidir sem pensar: mensagem falsa de prêmio, '
                     'botão de sair escondido, letra miúda. Você acha que escolheu, mas a tela '
                     'escolheu por você.',
        'exemplo': 'Site de compras dizendo "só restam 2 unidades!" é um dark pattern.',
        'artigo': 'Um desenvolvedor (P5) contou que as notificações diziam "você ganhou!" quando, '
                  'na verdade, era só uma nova chance de participar.',
        'perguntas': [
            {'pergunta': 'A notificação dizia VOCÊ GANHOU, mas não era prêmio. Por quê?',
             'certa': 'Pra me enganar e me fazer voltar pro app',
             'erradas': ['Foi um erro de digitação', 'Pra me dar um presente']},
            {'pergunta': 'Uma tela que te engana pra você clicar é...',
             'certa': 'Um truque feito de propósito',
             'erradas': ['Um defeito do celular', 'Uma promoção normal']},
        ],
    },
    'relampago': {
        'conceito': 'Gatilhos de urgência',
        'definicao': 'Contador regressivo, "últimos segundos", "só hoje". A pressa tira o tempo '
                     'de pensar, e sem pensar a gente aposta mais.',
        'exemplo': 'Black Friday com relógio na tela: você compra antes de decidir se precisa.',
        'artigo': 'O P5 admitiu usar "gatilhos de escassez, de urgência, de recompensa" e citou '
                  '"um contador que fica contando de trás pra frente".',
        'perguntas': [
            {'pergunta': 'Pra que serve aquele relógio contando os segundos?',
             'certa': 'Pra me apressar e eu não pensar direito',
             'erradas': ['Pra organizar o jogo', 'Porque o site ia sair do ar']},
            {'pergunta': 'Você decide melhor com calma ou com pressa?',
             'certa': 'Com calma, e por isso a bet me apressa',
             'erradas': ['Com pressa, decido mais rápido', 'Tanto faz']},
        ],
    },
    'influencer': {
        'conceito': 'Promessa de renda fácil',
        'definicao': 'As bets se vendem como um jeito de "ganhar uma renda extra", como se '
                     'apostar fosse trabalho. O artigo chama isso de "empreendedorismo lúdico". '
                     'E muitos prints de ganho são montados.',
        'exemplo': 'Influencer mostrando PIX gigante, mas ninguém mostra as perdas.',
        'artigo': 'Uma designer (P2) admitiu ter feito "prints de pagamentos que não pareciam reais" '
                  'pra propaganda.',
        'perguntas': [
            {'pergunta': 'Por que o influencer só mostra os ganhos?',
             'certa': 'Porque ele ganha pra divulgar, e as perdas não vendem',
             'erradas': ['Porque ele nunca perde', 'Porque é proibido mostrar perda']},
            {'pergunta': 'Um print de PIX gigante prova que dá pra ganhar?',
             'certa': 'Não, pode ser montado',
             'erradas': ['Sim, print não mente', 'Sim, se tiver muitas curtidas']},
        ],
    },
    'apagao': {
        'conceito': 'Zonas de não-conhecimento',
        'definicao': 'A tela esconde, ou passa rápido demais, o que importa, tipo quanto você já '
                     'perdeu. Sem essa informação, você decide no escuro.',
        'exemplo': 'É como comprar sem ver o preço e só descobrir na fatura.',
        'artigo': 'O P5 disse que "a plataforma não incentiva nenhum controle financeiro". '
                  'Não existe uma tela de "quanto você perdeu hoje".',
        'perguntas': [
            {'pergunta': 'Por que o seu saldo sumiu da tela?',
             'certa': 'Pra eu apostar sem lembrar quanto já perdi',
             'erradas': ['Foi um bug', 'Pra proteger minha privacidade']},
            {'pergunta': 'Por que quase nenhuma bet mostra "quanto você perdeu hoje"?',
             'certa': 'Porque se eu soubesse, talvez parasse',
             'erradas': ['Porque é difícil de programar', 'Porque a lei proíbe']},
        ],
    },
    'caixa': {
        'conceito': 'Fricção',
        'definicao': 'A bet escolhe onde colocar obstáculo e onde tirar. Pra apostar: 1 clique. '
                     'Pra sacar ou parar: um labirinto. Cada etapa a mais é uma chance de desistir.',
        'exemplo': 'Assinar um streaming é fácil. Cancelar é que é difícil.',
        'artigo': 'O artigo cita Ash e colegas (2018): o design de interface "gerencia fricções" '
                  'pra diminuir a hesitação nos momentos de decisão.',
        'perguntas': [
            {'pergunta': 'Apostar é 1 clique e sacar tem várias etapas. Por quê?',
             'certa': 'Pra ser mais fácil continuar do que parar',
             'erradas': ['É coincidência', 'É pra proteger meu dinheiro']},
            {'pergunta': 'No meio do saque apareceu um bônus pra você ficar. Isso é...',
             'certa': 'Um jeito de me fazer desistir de sair',
             'erradas': ['Um presente de despedida', 'Um erro do site']},
        ],
    },
    'bastidores': {
        'conceito': 'Responsabilidade de quem cria',
        'definicao': 'Alguém desenha cada botão, som e pop-up. O artigo entrevistou essas pessoas: '
                     'elas sabem do impacto, mas metas, chefes e medo de demissão fazem quase '
                     'ninguém questionar. A culpa fica "em outra cadeira".',
        'exemplo': 'Quem coloca doce no caixa do mercado sabe por que coloca ali.',
        'artigo': 'Os pesquisadores entrevistaram 5 profissionais que criam bets e produtos '
                  'parecidos. Um deles (P4) contou que colegas foram demitidos por recusar pedidos.',
        'perguntas': [
            {'pergunta': 'Quem o artigo entrevistou?',
             'certa': 'Designers e programadores que criam bets',
             'erradas': ['Apostadores viciados', 'Donos de time de futebol']},
            {'pergunta': 'Por que é difícil um designer dizer "não" pro chefe?',
             'certa': 'Por causa de metas, hierarquia e medo de demissão',
             'erradas': ['Porque ele concorda com tudo', 'Porque a lei proíbe recusar']},
        ],
    },
    'lei': {
        'conceito': 'O buraco da lei',
        'definicao': 'A Lei 14.790/2023 e a Portaria 722/2024 obrigam aviso de "jogue com '
                     'responsabilidade", limite de gasto e contador de tempo. Mas dizem O QUE a '
                     'tela mostra, e não COMO ela é projetada. Os truques continuam liberados.',
        'exemplo': 'É como obrigar o aviso "beba com moderação" e liberar o open bar.',
        'artigo': 'Os autores dizem que essas salvaguardas "se mostram insuficientes" e pedem '
                  'regras éticas pro próprio design.',
        'perguntas': [
            {'pergunta': 'A frase "jogue com responsabilidade" resolve o problema?',
             'certa': 'Não, os truques continuam lá',
             'erradas': ['Sim, resolve tudo', 'Só se for em letra grande']},
            {'pergunta': 'O que falta na lei, segundo o artigo?',
             'certa': 'Regras sobre COMO a tela é projetada',
             'erradas': ['Cobrar mais imposto', 'Proibir celular']},
        ],
    },
}

# Carta bônus, que todo mundo ganha no fim: a grande ideia do artigo
CARTA_FINAL = {
    'conceito': 'Autonomia relacional',
    'definicao': 'Ninguém decide sozinho. A decisão de apostar é dividida com notificações, '
                 'contadores, algoritmos e metas de empresa. Por isso o artigo troca a pergunta '
                 '"por que a pessoa não se controla?" por "como a plataforma fabrica as condições '
                 'pra ela não conseguir se controlar?".',
    'exemplo': 'É como tentar fazer dieta morando em cima de uma padaria que te manda mensagem '
               'toda vez que sai pão quente.',
}

# ---------------- EVENTOS DE CADA CASA (sorteados) ----------------
NOTIFICACOES = [
    ('🎉 VOCÊ GANHOU!!! 🎉', 'era só uma chance de apostar de novo, se depositar R$ 10'),
    ('🎁 PRÊMIO LIBERADO PRA VOCÊ!', 'um giro "grátis" que só vale depositando R$ 10'),
    ('🍀 Você é um dos jogadores com mais sorte hoje!', 'todo mundo recebeu essa mesma mensagem'),
]

OFERTAS = [
    'Aposte R$ 30 e o prêmio vem em DOBRO!',
    'Só pros próximos segundos: prêmio turbinado!',
    'Seu bônus EXPIRA se você não apostar agora!',
]

INFLUENCERS = [
    ('@reidagreen', 'Fiz R$ 5 mil hoje com R$ 50! Usa meu link 🔥'),
    ('@mariasortuda', 'Larguei o emprego, agora vivo de bet 💅 Link na bio!'),
    ('@gugaestrategia', 'Meu método nunca falha. Copia minha aposta 👇'),
]

ETAPAS_SAQUE = [
    'Confirmar seu e-mail',
    'Enviar foto do documento',
    'Tirar uma selfie segurando o documento',
    'Responder um questionário de segurança',
    'Cadastrar uma nova chave Pix',
    'Aguardar até 72 horas de análise',
]

POPUPS_SAQUE = [
    '😢 Já vai? Fica mais um pouquinho e ganha R$ 20 de bônus!',
    '🔥 NÃO ABANDONE! Seus amigos estão ganhando agora!',
    '🎁 Espera! Tem um giro grátis te esperando!',
]

# Pedidos do chefe (casa Bastidores). Tudo baseado no que os entrevistados contaram.
PEDIDOS = [
    {'pedido': 'Coloca um som de vitória quando o usuário QUASE ganhar.',
     'artigo': 'Sons de vitória e de quase-acerto aparecem no artigo como microinterações feitas '
               'pra manter a pessoa jogando sem refletir.'},
    {'pedido': 'Manda notificação "VOCÊ GANHOU!" pra quem sumiu do app.',
     'artigo': 'O P5 contou que fazia exatamente isso: "você ganhou!" quando era só uma nova chance.'},
    {'pedido': 'Tira o controle de gastos do app. Ele diminui o lucro.',
     'artigo': 'O P5 disse que "a plataforma não incentiva nenhum controle financeiro". O P3 sugeriu '
               'o contrário: um "limitador de perdas financeiras mais escancarado".'},
    {'pedido': 'Monta um print de PIX de R$ 10 mil pra propaganda. Não precisa ser real.',
     'artigo': 'A P2 admitiu ter feito "prints de pagamentos que não pareciam reais". E disse que no '
               'trabalho "ninguém fala sobre isso".'},
    {'pedido': 'Quando a pessoa tentar sair, mostra um pop-up: "Não abandone!".',
     'artigo': 'O P5 descreveu pop-ups que "explodem na tela" diante de qualquer hesitação.'},
    {'pedido': 'Deixa a tela bem poluída. O cliente disse: "esse público gosta do feio".',
     'artigo': 'O P5 ouviu de um cliente: "esse público é classe D e F, eles gostam do feio mesmo". '
               'O artigo mostra como esse preconceito vira design e reforça a desigualdade.'},
]

# Quiz final: só o que o jogo ensinou. (pergunta, certa, [erradas])
QUIZ = [
    ('Quantos profissionais o artigo entrevistou?', '5', ['500', '50']),
    ('Quem o artigo entrevistou?', 'Quem cria as bets: designers e programadores',
     ['Apostadores', 'Políticos']),
    ('De quem é a culpa pelo vício, segundo o artigo?',
     'De toda a rede que cria a bet, não só de quem aposta', ['Só de quem aposta', 'De ninguém']),
    ('Apostar é fácil e sacar é difícil. Esse truque se chama...', 'Fricção', ['Sorte', 'Segurança']),
    ('Contador regressivo serve pra...', 'Me apressar e eu não pensar',
     ['Organizar o jogo', 'Me ajudar a decidir']),
    ('Qual destas é uma proposta dos autores?', 'Mostrar com clareza quanto a pessoa já gastou',
     ['Dar mais bônus', 'Proibir celulares']),
    ('Por que a lei atual não basta, segundo o artigo?',
     'Ela diz o que a tela mostra, mas não como ela é projetada',
     ['Não existe lei nenhuma', 'A lei é dura demais']),
    ('Uma tela de bet é neutra?', 'Não, carrega as escolhas de quem a criou',
     ['Sim, sempre', 'Só quando é gratuita']),
    ('Segundo o DataSenado (2024), quantos apostadores têm dívida atrasada?', '42%', ['4%', '92%']),
    ('O que aconteceu com colegas que recusaram pedidos enganosos (relato do P4)?',
     'Foram demitidos', ['Foram promovidos', 'Nada']),
]

# ---------------- MANUAL (aparece no jogo e no MANUAL.md) ----------------
MANUAL = """
### 🎯 Objetivo
Atravessar o tabuleiro da **SorteJá.bet** (uma bet de mentira) e **sair com dinheiro no bolso**.
No caminho, a bet vai usar os truques que os profissionais contaram no artigo pra te prender.
Cada truque que você desmascara vira uma **carta do álbum**. São 9 cartas, mais 1 bônus no final.

**Você vence de verdade se:** sair com dinheiro E completar o máximo de cartas.

### 🎲 Como jogar
1. Você começa na casa 🏁 com **R$ 100 + um bônus de boas-vindas**.
2. Aperte **Rolar o dado**: você anda de 1 a 6 casas.
3. A casa onde você cair tem um evento. Escolha o que fazer.
4. Na primeira vez que cair num tipo de casa, aparece uma pergunta **"Que truque foi esse?"**.
   Não precisa saber nada antes, é só usar o bom senso. Acertando ou não, você aprende e ganha a carta.
5. Chegou na casa 🏦 **SAÍDA**? Tente sacar seu dinheiro e o jogo acaba.

### 🗺️ As casas
| Casa | O que acontece |
|---|---|
| 🙈 Apagão | Seu saldo some da tela por 2 rodadas |
| 👔 Bastidores | Plot twist: por 1 rodada você trabalha criando a bet. O chefe faz um pedido |
| 💸 Caixa | Você pode tentar sacar e sair do jogo mais cedo |
| 🎰 Caça-níquel | Aposte R$ 10, 20 ou 50. Três símbolos iguais pagam 3x |
| 🤳 Influencer | Um influencer te dá uma "dica certeira" |
| ⚖️ Lei | Você ganha o 🛡️ Escudo da Lei, que devolve sua próxima perda |
| 🔔 Notificação | Chega um "VOCÊ GANHOU!" no celular |
| ⏰ Oferta relâmpago | Um relógio conta os segundos pra você apostar |
| 🎟️ Raspadinha | Pague R$ 10, escolha 1 de 3 bilhetes |

### 📏 Regras extras
- **Sempre dá pra não apostar.** Recusar também é uma jogada (e a bet não gosta).
- **Saldo zerou?** Fim de jogo. A bet te "capturou".
- **Pra sacar** você passa por etapas e pop-ups. Se desistir no meio, volta a jogar.
- **🛡️ Escudo da Lei:** devolve o dinheiro da próxima aposta que você perder. Só funciona uma vez.
- **👔 Ética:** nos Bastidores, recusar pedidos enganosos dá 1 ponto de ética.
- **Cada partida é diferente:** a ordem das casas, as perguntas e os eventos são sorteados.

### 🏆 No final
Você vê o **Raio-X** (tudo que a bet sabia sobre você), uma simulação com **1.000 jogadores**
com as mesmas regras, seu álbum de cartas e um quiz de 3 perguntas.
"""
