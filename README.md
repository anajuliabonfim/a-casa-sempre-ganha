# 🎰 A Casa Sempre Ganha

**Um jogo de tabuleiro dentro de uma bet de mentira, pra entender como as plataformas de apostas prendem as pessoas.**

🔗 **Jogue agora:** [a-casa-sempre-ganha.streamlit.app](https://a-casa-sempre-ganha.streamlit.app)

Jogo educativo feito em **Python** com **Streamlit**, baseado em um artigo científico sobre design persuasivo em bets. Cada casa do tabuleiro reproduz um truque que designers e programadores do setor contaram aos pesquisadores: o "quase ganhei", a notificação falsa de prêmio, o contador regressivo, o saque cheio de etapas.

## 🎲 Como funciona

1. Você entra na **SorteJá.bet** (fictícia) com R$ 100 e um bônus de boas-vindas.
2. Rola o dado e anda pelo tabuleiro de 20 casas.
3. Cada casa é um truque: caça-níquel, raspadinha, notificação, oferta relâmpago, influencer, apagão do saldo e mais.
4. Na primeira vez em cada truque, você tenta adivinhar o que está acontecendo e ganha uma **carta** com o conceito do artigo.
5. No final: um **Raio-X** do que a plataforma sabia sobre você, uma **simulação com 1.000 jogadores** e um quiz rápido.

Cada partida sorteia a ordem das casas, as perguntas e os eventos, então ninguém joga igual duas vezes.

📜 Regras completas: [MANUAL.md](MANUAL.md)

## 📚 O que o jogo ensina

Os conceitos vêm do artigo e aparecem como cartas do álbum:

- **Autonomia relacional**: ninguém decide sozinho, a decisão é dividida com a interface.
- **Captura afetiva**: sons e animações que mexem com a emoção.
- **Dark patterns**: truques de tela pra decidir sem pensar.
- **Fricção**: entrar é fácil, sair é difícil.
- **Gatilhos de urgência**: a pressa tira o tempo de pensar.
- **O buraco da lei**: as regras dizem o que mostrar, não como projetar.
- **Promessa de renda fácil**: apostar vendido como trabalho.
- **Recompensa variável**: não saber quando o prêmio vem é o que prende.
- **Responsabilidade de quem cria**: alguém desenha cada botão.
- **Zonas de não-conhecimento**: a tela esconde o que importa.

## 🛠️ Tecnologias

- Python 3
- Streamlit (interface web e gerenciamento de estado com `session_state`)
- HTML e CSS embutidos para o tabuleiro e o visual
- Deploy no Streamlit Community Cloud

## 💻 Rodar localmente

```bash
git clone https://github.com/anajuliabonfim/a-casa-sempre-ganha.git
cd a-casa-sempre-ganha
pip install -r requirements.txt
python -m streamlit run app.py
```

## 📁 Estrutura

| Arquivo | O que tem |
|---|---|
| `app.py` | Regras do jogo e telas |
| `conteudo.py` | Todo o conteúdo: casas, cartas, perguntas, quiz e manual |
| `.streamlit/config.toml` | Tema visual |

O conteúdo fica separado da lógica: pra acrescentar perguntas ou eventos, é só mexer no `conteudo.py`.

## 📄 Artigo base

MARQUES, Daniel; FALCÃO, Thiago. Design persuasivo e mediação tecnológica em plataformas digitais de apostas: práticas e dilemas éticos de designers e desenvolvedores. **Arcos Design**, v. 19, n. 1, 2026. [doi.org/10.12957/arcosdesign.2026.93891](https://doi.org/10.12957/arcosdesign.2026.93891)

## 👩‍💻 Equipe

- Ana Júlia Bonfim ([LinkedIn](https://www.linkedin.com/in/anajuliabonfim/))
- Gabriela Nóbrega
- Kédynna Dantas
- Manoel Medeiros

Projeto da disciplina **Leitura e Produção de Texto** (Profa. Suéllen Rodrigues Ramos da Silva), curso de Ciência da Computação da **UEPB, Campus VII**, 2026.2.

---
