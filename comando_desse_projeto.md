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

-> Com seu ambiente virtual ativo, vamos criar noss app chamado contact
python manage.py startapp contact

-> Vamos até a pasta contact
-> abra o arquivo apps.py
-> copie o nome do seu app
-> name = 'contact' deve estar assim
-> vá até a pasta project
-> abra o arquivo settings.py
-> Vá até INSTALLED_APPS = [
-> Na ultima linha coloque uma , e adiciona 'contact',
-> Sempre importante fazer isso ao criar o seu APP

-> configuramos urls e views, templates iniciais etc..

python manage.py migrate

-> vamos criar um usuário master para o Django Admin
python manage.py createsuperuser
-> caso você esqueça a sua senha de usuário basta rodar o comando
python manage.py changepassword 'seu_nome_de_usuario'

-> Toda vez que eu atualizar meus models preciso rodar o camando
python manage.py makemigrations
-> Como criei as migrações, agora vamos migrar e criar as tabelas na base de dados
python manage.py migrate

-> Realizar o Collectstatic para não enviar para o git pois ele só será
usado quando for feito deploy no servidor real
python manage.py collectstatic
