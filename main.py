import sqlite3

PASSWORD = '123456'

senha = input("Insira sua senha: ")
if senha != PASSWORD:
  print('Senha Incorreta! Encerrando...')
  exit()

conn = sqlite3.connect('passwords.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
  service TEXT NOT NULL,
  username TEXT NOT NULL,
  password TEXT NOT NULL
)
''')

def menu():
  print('****************************')
  print('i : Inserir nova senha')
  print('l : Listar serviços salvos')
  print('r : Recuperar uma senha')
  print('s : Sair')
  print('****************************')

def getPassword(service):
  cursor.execute(f'''
    select username, password FROM users WHERE service = '{service}'
  ''')

  if cursor.rowcount == 0:
    print('Serviço Não Cadastrado (use "1" para verificar os serviços.)')
  else:
    for user in cursor.fetchall():
      print(user)

def insertPassword(service, username, password):
  cursor.execute(f'''
    insert into users (service, username, password) values ('{service}','{username}','{password}')
  ''')
  conn.commit()

def showPasswords():
  cursor.execute('''
    select service from users;
  ''')
  for service in cursor.fetchall():
    print(service)

while True:
  menu()
  op = input('O que deseja fazer? ')
  if op not in ['l','i','r','s']:
    print("Opção Inválida")
    continue

  if op == 's':
    break

  if op == 'i':
    service = input('Qual o nome do serviço? ')
    username = input('Qual o e-mail/username? ')
    password = input('Qual a senha? ')
    insertPassword(service, username, password)

  if op == 'l':
    showPasswords()

  if op == 'r':
    service = input('Qual o serviço? ')
    getPassword(service)

conn.close()