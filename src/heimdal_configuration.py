import os
from dotenv import load_dotenv
class HeimdalConfiguration:
    ssh_ip: str
    ssh_port: str
    ssh_user: str
    ssh_password: str
    backup_path: str
    host: str
    user: str
    password: str
    database: str

    
    def __new__(self):
        instance = super().__new__(self)
        print('Comprobando .env...')
        load_dotenv()
        print('Cargando configuración de SSH')
        ssh_ip = os.getenv('SSH_IP')
        ssh_user = os.getenv("SSH_USER")
        ssh_password = os.getenv("SSH_PASSWORD")
        ssh_port = os.getenv("SSH_PORT")
        if ssh_ip is None:
            raise Exception('La clave SSH_IP no se ha encontrado en el archivo .env!! Abortando')
        else:
           instance.ssh_ip = ssh_ip
        if ssh_user is None:
            raise Exception('La clave SSH_USER no se ha encontrado en el archivo .env!! Abortando')
        else:
           instance.ssh_user = ssh_user
        if ssh_password is None:
            raise Exception('La clave SSH_PASSWORD no se ha encontrado en el archivo .env!! Abortando')
        else:
           instance.ssh_password = ssh_password  
            
        if ssh_port is None:
            raise Exception('La clave SSH_PORT no se ha encontrado en el archivo .env!! Abortando')
        else:
           instance.ssh_port = ssh_port   
        
        print('Cargando configuración de la base de datos')
        user = os.getenv("USER")
        database = os.getenv("DATABASE")
        password = os.getenv("PASSWORD")
        host = os.getenv("HOST")
        
        if user is None:
            raise Exception('La clave USER no se ha encontrado en el archivo .env!! Abortando')
        else:
            instance.user = user
            
        if database is None:
            raise Exception('La clave DATABASE no se ha encontrado en el archivo .env!! Abortando')
        else:
            instance.database = database
            
        if password is None:
            raise Exception('La clave PASSWORD no se ha encontrado en el archivo .env!! Abortando')
        else:
            instance.password = password
        
        if host is None:
            raise Exception('La clave HOST no se ha encontrado en el archivo .env!! Abortando')
        else:
            instance.host = host
        return instance