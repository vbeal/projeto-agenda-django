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

-> Com seu ambiente virtual ativo, vamos criar noss app
python manage.py startapp contact
