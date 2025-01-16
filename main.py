import pyautogui as pyag
import time
import pandas as pd


# 1- Abrir o navegador;
# 2- Abrir o site do sistema (https://dlp.hashtagtreinamentos.com/python/intensivao/login);
# 3- Fazer login com usuário e senha;
# 4- Inserir todas as informações do produto;
# 5- Enviar as informações para o sistema;
# 6- Repetir o cadastro até acabar todos os produtos da base de dados.

# Configura uma pausa automática entre os comandos para evitar erros de sincronização.
pyag.PAUSE = 0.8

# Configuração inicial: URL do sistema e credenciais
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email = "tiiagolohan@gmail.com"
senha = "123"

# Abrir o navegador Chrome e acessar o link do sistema
pyag.press("win")     # Abre o menu Iniciar
pyag.write("chrome")  # Digita "chrome" para buscar o navegador
pyag.press("enter")   # Pressiona Enter para abrir o Chrome
pyag.write(link)      # Digita o link do sistema
pyag.press("enter")   # Acessa o site

time.sleep(4)   # Aguarda o carregamento completo do site

# Realiza o login no sistema
pyag.press("tab")     # Navega até o campo de e-mail
pyag.write(email)     # Insere o e-mail
pyag.press("tab")     # Navega até o campo de senha
pyag.write(senha)     # Insere a senha
pyag.press("tab")     # Navega até o botão de login
pyag.press("enter")   # Realiza o login

# Lê a base de dados dos produtos para cadastro
file = "produtos.csv"     # Nome do arquivo CSV com os produtos
product_base = pd.read_csv(file)    # Carrega os dados do CSV em um DataFrame

# Laço para cadastrar cada produto na base de dados
for i, line in product_base.iterrows():

  # Clica para iniciar o cadastro do produto (ajustar coordenadas conforme necessário)
  pyag.click(x=651, y=362)

  # Insere o código do produto
  pyag.write(str(line["codigo"]))
  pyag.press("tab")       # Avança para o próximo campo

  # Insere a marca do produto
  pyag.write(str(line["marca"]))
  pyag.press("tab")

  # Insere o tipo do produto
  pyag.write(str(line["tipo"]))
  pyag.press("tab")

  # Insere a categoria do produto
  pyag.write(str(line["categoria"]))
  pyag.press("tab")

  # Insere o preço unitário
  pyag.write(str(line["preco_unitario"]))
  pyag.press("tab")

  # Insere o custo do produto
  pyag.write(str(line["custo"]))
  pyag.press("tab")

  # Insere observações, se existirem
  if str(line["obs"]) != "nan":     # Verifica se há observações válidas
    pyag.write(str(line["obs"]))
    
  pyag.press("tab")     # Avança para o próximo campo

  # Envia o formulário (cadastra o produto)
  pyag.press("enter")

  # Ajusta o scroll para visualizar o próximo formulário
  pyag.scroll(500)

  