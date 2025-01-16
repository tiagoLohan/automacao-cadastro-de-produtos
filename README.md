# Automação de Cadastro de Produtos com Python 🛠️

Este projeto automatiza o cadastro de produtos em um sistema web, utilizando a biblioteca `pyautogui` para simular interações manuais com o navegador. A automação realiza o processo de login, preenche os dados dos produtos de uma base CSV e os cadastra no sistema.

---

## Funcionalidades ✨

- **Login automático**: Acessa o sistema com credenciais fornecidas.
- **Cadastro em massa**: Lê uma base de dados CSV e insere os produtos no sistema de forma automatizada.
- **Execução sequencial**: Realiza o cadastro linha por linha, até que todos os produtos sejam processados.

---

## Tecnologias utilizadas 💻

- **Python**: Linguagem principal do projeto.
- **Pandas**: Para manipulação e leitura do arquivo CSV com os dados dos produtos.
- **PyAutoGUI**: Para interagir com o navegador e os elementos do sistema.

---

## Pré-requisitos 🛠️

- Base de dados dos produtos em formato CSV.
- Configuração do navegador e coordenadas dos cliques ajustadas para o seu ambiente.

---

## Estrutura do CSV 📂

A base de dados deve ter o seguinte formato, com as colunas indicadas:

| codigo | marca   | tipo   | categoria   | preco_unitario | custo | obs          |
| ------ | ------- | ------ | ----------- | -------------- | ----- | ------------ |
| 101    | Marca X | Tipo A | Categoria 1 | 19.99          | 15.00 | Observação 1 |
| 102    | Marca Y | Tipo B | Categoria 2 | 29.99          | 20.00 | Observação 2 |
| 103    | Marca Z | Tipo C | Categoria 3 | 39.99          | 25.00 |              |

---

## Personalização 🔧

- **URL do sistema**: Altere o link diretamente na variável `link` do código.
- **Credenciais**: Insira seu e-mail e senha nas variáveis `email` e `senha`.
- **Coordenadas do clique**: Ajuste as coordenadas `x` e `y` do `pyag.click` para a posição correta do botão no seu sistema.

---

## Próximos passos 📌

- Adicionar logs para monitorar o status de cada cadastro.
- Tratar erros em caso de falha de conexão ou inconsistências nos dados.
- Melhorar a interface do script para aceitar argumentos na linha de comando.
