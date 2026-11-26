# 🎰 A Casa Sempre Ganha · o tabuleiro

Jogo de tabuleiro dentro de uma bet de mentira, feito em Python com Streamlit. Cada casa do tabuleiro é um truque que os profissionais contaram no artigo:

MARQUES, Daniel; FALCÃO, Thiago. Design persuasivo e mediação tecnológica em plataformas digitais de apostas. Arcos Design, v. 19, n. 1, 2026.

Leitura e Produção de Texto · Ciência da Computação · UEPB Campus VII
Equipe: Ana Júlia Bonfim, Gabriela Nóbrega, Kédynna Dantas, Manoel Medeiros.

Regras do jogo: [MANUAL.md](MANUAL.md)

---

# 🧠 Guia de estudo da Ana

## 1. Rodar no seu PC
```
pip install streamlit
python -m streamlit run app.py
```
Pra parar: Ctrl + C no terminal.

## 2. Os arquivos
| Arquivo | O que tem | Quando mexer |
|---|---|---|
| `app.py` | As regras e as telas | Quer mudar como uma casa funciona |
| `conteudo.py` | TODO o texto: casas, cartas, perguntas, pedidos do chefe, quiz, manual | Quer mudar ou acrescentar texto (90% das vezes é aqui) |
| `.streamlit/config.toml` | Cores do tema | Quer trocar as cores |
| `requirements.txt` | Avisa o servidor pra instalar o Streamlit | Quase nunca |

## 3. Como o jogo anda (o "mapa" do app.py)
Cada tela tem um nome, guardado em `jogo.fase`. O app.py é um grande `if / elif` que olha esse nome e desenha a tela certa:

```
inicio → intro → tabuleiro → casa → pergunta → carta → tabuleiro → ...
                                 ↘ (caiu na Caixa ou na Saída) saque → raiox → album → quiz → fim
                                 ↘ (saldo zerou) quebrou → raiox → ...
```

- **tabuleiro**: rola o dado (`random.randint(1, 6)`), anda e descobre o tipo da casa.
- **casa**: um `elif` pra cada tipo (cassino, raspadinha...). Primeiro a pessoa escolhe, depois aparece o resultado (`jogo.resolvido`).
- **pergunta / carta**: só aparecem na PRIMEIRA vez em cada tipo de casa (`if tipo in jogo.cartas`).

## 4. O Python que aparece (e cai na prova de Algoritmos!)
- **Lista**: `jogo.tabuleiro` é uma lista de 20 textos. `jogo.cartas` vai crescendo com `.append()`.
- **Dicionário**: cada carta em `CARTAS` é um dicionário (`carta['conceito']`).
- **for**: `for i, tipo in enumerate(jogo.tabuleiro)` desenha as 20 casas. O `enumerate` dá o número e o valor juntos.
- **Funções**: `apostar()`, `perder()`, `montar_tabuleiro()`. Cada uma faz uma coisa só.
- **random**: `shuffle` embaralha o tabuleiro, `choice` sorteia uma pergunta, `random() < 0.25` é "1 chance em 4".
- **min()**: `min(jogo.pos + jogo.dado, 19)` impede de passar da última casa.
- **Índice começa em 0**: a casa de início é a 0 e a saída é a 19 (são 20 casas).

## 5. Como o Streamlit funciona (3 regrinhas)
1. A cada clique, ele roda o `app.py` **inteiro de novo**, de cima pra baixo.
2. Variável normal se perde no clique. O que precisa ficar vai em `st.session_state` (que a gente apelidou de `jogo`).
3. `ir_para('tela')` muda `jogo.fase` e chama `st.rerun()`, que redesenha na hora.

## 6. Dá pra colocar imagem? Dá!
Coloca a imagem na pasta (ex.: `mascote.png`) e escreve onde quiser:
```python
st.image('mascote.png', width=200)
```
Também funciona com GIF. Só use imagens que vocês mesmos fizeram (Canva, por exemplo) ou que sejam livres, e nunca personagens de marca (tipo o tigrinho).

## 7. Colocar no ar (link pra professora)
Cloudflare Pages e GitHub Pages só hospedam sites "parados" (HTML), não rodam Python. Pra Streamlit, o caminho é o **Streamlit Community Cloud** (grátis):
1. Crie um repositório público no GitHub (ex.: `a-casa-sempre-ganha`) e suba todos os arquivos, inclusive a pasta `.streamlit`.
2. Entre em share.streamlit.io com o GitHub.
3. **Create app** → escolha o repositório, branch `main`, arquivo `app.py` → **Deploy**.
4. Sai um link tipo `a-casa-sempre-ganha.streamlit.app`.

Cada `git push` atualiza o site sozinho. Se ninguém abrir por uns dias, ele "dorme": abra 5 minutos antes da apresentação.

## 8. Exercícios pra deixar o jogo seu
1. Acrescente um influencer novo em `INFLUENCERS` (conteudo.py). Fácil.
2. Acrescente 2 perguntas no `QUIZ`.
3. Mude o tabuleiro pra ter 6 caça-níqueis (mexa em `quantidade` e em `TAMANHO` no app.py). Dica: `TAMANHO` = soma das quantidades + 2.
4. Crie uma casa nova (ex.: 🎡 Roleta). Precisa: entrada em `CASAS`, carta em `CARTAS` e um `elif tipo == 'roleta':` no app.py.
