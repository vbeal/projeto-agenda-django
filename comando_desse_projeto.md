-> Criando o ambiente virtual
python -m venv venv

-> Ativando meu ambiente virtual
.\venv\Scripts\activate

-> Instalando o Django
pip install django

-> Caso apareça mensagem do Pip estar desatualizado
python.exe -m pip install --upgrade pip

-> Verificar se o Django foi instalado neste diretório
pip freeze

-> Vamos criar o nosso projeto Django na raiz usando o .
django-admin startproject project .

-> Vamos rodar o servidor do Django para ver se está tudo ok
python manage.py runserver

-> Desativar ambiente virtual
deactivate

---

    Vamos configurar o Git

---

git config --global user.name 'Seu Nome'
git config --global user.email 'seu@email.com'
git config --global init.defaultBranch main

# Configurando o .gitignore

-> Iniciar o Git
git init

-> Vamos adicionar ou use o ínco da direita do VSC
git add .

-> Vamos comitar/ comentar nosso envio
git commit -m 'Mensagem desejada'

-> Criar o repositório lá no seu Git
-> Copiar o código do repositório ssh e dar o comando
git remote add origin 'link do seu repositório'

-> Vamos enviar os arquivos para lá agora
git push origin master

->Se não der certo vamos criar uma chave SSH
-> Para não haver erro vá abra seu prompt de comando e vá até
o diretório c:/user/'seu_nome_da_maquina' cd user/<seunome> abre a pasta
-> Verificar se vc tem o diretório .ssh
-> caso não tenha crie ele nesta pasta
-> agora rode o comando para criar sua chave.
ssh-keygen -f seu_nome_rsa -t rsa -b 4096
-> Se deseja digite uma senha e depois confirme e vai receber
a mensagem de chave criar
-> Agora abra o arquivo seu_nome_rsa.pub que foi criado no diretório .ssh
cat seu_nome_rsa.pub
-> copie o código e cole lá no settings do git
git remote rm origin
git remote add [copie a sua chave ssh no git]
git push origin master
