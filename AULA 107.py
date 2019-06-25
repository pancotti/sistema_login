#AULA 107 - GIT E GITHUB

#Cria um usuário do Github

#Cria um novo repositório - Sistema Login

#Executa o download do git no site: https://git-scm.com/

# Executa a instalação do git

#Após instalação procura: Git Bash no windows. Vai abrir uma janela de prompt

#No prompt acessa a pasta do projeto. Para acessar a nuvem deve ser digitado cd g:. Depois cd e os subdiretorios.

#No pycharm deve ser criado um arquivo texto com o nome: .gitgnore

    #Acesse o arquivo pelo pycharm e informe os arquivos que devem ser ignorados e não enviados ao guithub:
        #*.pyc
        #venv/

#No prompt do DSOS, dentro da pasta do projeto. Na subpasta venv/Scripts, digita o comando: activate.bat para abrir
#o ambiente virtual. Qd é acessado o ambiente virtual, vai aparecer no prompt: (venv) g:\...

#Dentro do ambiente virtual é necessário criar um arquivo de requerimento utilizando o pip:
    #pip freeze > requirements.txt. Neste arquivo conterá a relação de bibliotecas instaladas dentro do ambiente
    #virtual.

#Na página do github, dentro do repositório, deve ser clicado no botão "clone download" para copiar o caminho do
#repositório.

#No prompt do git Bash, execute os comandos:

    #git init . -> para iniciar o repositório vazio.

    #git remote add origin + o endereço do repositório -> acessa o repositorio no site do github.

    #git pull origin master -> para trazer as operações do repositorio remoto para o repositorio local. Neste momento
    #é importado o arquivo README.md na raiz do repositório local.

    # git commit -m "primeiro commit" -> enviar tudo para o github

    # git push origin master -> neste momento é enviado todos os arquivos do repositorio local para o repositório na
    #página do github.


##Criando um novo repositório
#crie uma nova pasta, abra-a e execute o comando:

    #git init
#para criar um novo repositório.


##Obtenha um repositório
#crie uma cópia de trabalho em um repositório local executando o comando
    #git clone /caminho/para/o/repositório

#quando usar um servidor remoto, seu comando será
    #git clone usuário@servidor:/caminho/para/o/repositório


#Fluxo de trabalho
#Seus repositórios locais consistem em três "árvores" mantidas pelo git. a primeira delas é sua Working Directory que
# contém os arquivos vigentes. a segunda Index que funciona como uma área temporária e finalmente a HEAD que aponta
# para o último commit (confirmação) que você fez.

#Adicionar & confirmar
#Você pode propor mudanças (adicioná-las ao Index) usando
    #git add <arquivo>
    #git add *
    #Este é o primeiro passo no fluxo de trabalho básico do git. Para realmente confirmar estas mudanças
    # (isto é, fazer um commit), use git commit -m "comentários das alterações"
    #Agora o arquivo é enviado para o HEAD, mas ainda não para o repositório remoto.

#Enviando alterações
#Suas alterações agora estão no HEAD da sua cópia de trabalho local. Para enviar estas alterações ao seu repositório
# remoto, execute:
    #git push origin master
#Altere master para qualquer ramo (branch) desejado, enviando suas alterações para ele.

#Se você não clonou um repositório existente e quer conectar seu repositório a um servidor remoto,
# você deve adicioná-lo com:
    #git remote add origin <servidor>

#Agora você é capaz de enviar suas alterações para o servidor remoto selecionado.

#Atualizar & mesclar
#para atualizar seu repositório local com a mais nova versão, execute:
    #git pull
#na sua pasta de trabalho para obter e fazer merge (mesclar) alterações remotas. Para fazer merge de um outro branch
# ao seu branch ativo (ex. master), use git merge <branch> em ambos os casos o git tenta fazer o merge das
# alterações automaticamente. Infelizmente, isto nem sempre é possível e resulta em conflitos. Você é responsável
# por fazer o merge estes conflitos manualmente editando os arquivos exibidos pelo git. Depois de alterar,
# você precisa marcá-los como merged com git add <arquivo>

#antes de fazer o merge das alterações, você pode também pré-visualizá-as usando git diff <branch origem>
# <branch destino>.
