#AULA 109 - DEPLOY DA APLICAÇÃO

#Cria um usuário do HEROKU - http://heroku.com

#Usuário: pancotti@bol.com.br
#Password: Bb981920

#No Prompt do MSDOS, dentro da pasta de trabalho, digita os comandos:
#heroku login. O sistema irá pedir a senha através do site

#No pycharm deve ser criado um arquivo chamado |Procfile. Neste arquivo deve conter a lista de comando para iniciar
#cada processo.

#Verifique a necessidade de atualizar o repositório no GitHub

#No prompt do MSDOS cria o nome do aplicativo no Heroku, através do comando:
#heroku create sistemaloginpancotti -> "nome_do_aplicativo

#Comando para setar o Heroku como repositório remoto da aplicação:
#heroku git:remote sistemaloginpancotti -> "nome do aplicativo criado no heroku".
#git remote - v -> vai demonstrar que esta direcionado para o branch Heroku.

#git push heroku master -> envia o repositório do git para o Hiroku

#heroku config:set APP_location=heroku -> para setar o Heroku como servidor do aplicativo.

#heroku open -> para abrir o aplicativo/página no heroku