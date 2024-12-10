from .contact_views import *
from .contact_forms import *
'''
Atenção como estamos importando tudo dos arquivos contact_views e contact_forms
ele vai pegar tudo que tem dentro desses arquivos
assim eles não podem ter o mesmo nome de view. 
Ex: def index(request) no contact_views e def index(request) no contact_forms
Isso vai gerar um erro, pois eles tem o mesmo nome
'''