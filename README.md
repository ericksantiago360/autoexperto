# autoexperto

ls
1# activar enviroment
source ./venv/bin/activate
2# acceder al proyecto

cd autoexperto/ 
3# activar el contenedor  docker de base de datos  mysqlserver  autoexperto
descargar contenedeor desde dockerhub
arm64v8/mysql

editar settings como
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'autoexperto',
            'USER': 'root',
            'PASSWORD': 'admin',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
crear bse de datos dede 
CREATE DATABASE autoexperto CHARACTER SET utf8;



4# python3 manage.py runserver
