# Como Testar o Código

Aqui está um guia simples para você rodar o código na sua máquina e entender o que ele faz.

## 1. O que você precisa ter:

- **Python** instalado (de preferência a versão mais recente).
- **Google Chrome** instalado.
- **ChromeDriver** compatível com sua versão do Chrome:
  - Faça o download em [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads).
  - Coloque o ChromeDriver na mesma pasta do código ou adicione ao PATH do sistema.

## 2. Configurando o ambiente:

1. Baixe ou copie o código para uma pasta no seu computador.
2. Abra o terminal (ou prompt de comando) e vá até a pasta onde o código está:

```bash
cd caminho/da/sua/pasta
```

3. Instale o Selenium, necessário para o código funcionar. No terminal, execute:

```bash
pip install selenium
```

## 3. O que o código faz:

Este bot automatiza algumas ações no navegador para coletar informações no YouTube. Aqui está o que ele vai fazer:

1. Abrir o navegador Google Chrome.
2. Acessar a página do YouTube e navegar até a seção "Em alta".
3. Explorar as categorias "Música", "Jogos" e "Filmes".
4. Coletar informações sobre os três primeiros vídeos de cada categoria.
5. Salvar os dados coletados em um arquivo Excel na pasta onde o código está.

## 4. Rodando o código:

Com tudo configurado, basta executar o script com o comando:

```bash
python nome_do_arquivo.py
```

O navegador abrirá automaticamente e o bot começará a executar as ações descritas acima.

## 5. Vídeo demonstrativo:

Veja abaixo uma demonstração de como o código funciona:

![Demonstração do Código](Desktop%202025.01.13%20-%2009.51.35.02.gif)

---


