# Projeto Portal

:point_right: Criar uma pasta para o projeto:
```
mkdir pasta_projeto
cd pasta_projeto
```

:point_right: Criar um ambiente virtual:
```
python3 -m venv {nome_do_ambiente}
source venv/bin/activate
```

:point_right: Para instalar os requirements:
```
pip install -r requirements.txt
```

:point_right: É nessário criar um banco de dados no postgreSQL e colocar as configurações no 'settings.py':
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{nome_do_banco}',
        'USER': '{nome_do_usuario}',
        'PASSWORD': '{senha_do_banco}',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```
