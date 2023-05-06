import os
from paramiko import SSHClient, AutoAddPolicy
from scp import SCPClient
from datetime import date
from heimdal_configuration import HeimdalConfiguration


class Heimdal:
    ssh_client: SSHClient
    scp_client: SCPClient
    heindalConfiguration: HeimdalConfiguration
    def __new__(self):
        instance = super().__new__(self)
        print('Se ha instanciado Heimdal. El guardián está listo para comenzar su acción!')
        print('Heimdal requiere que se configure la conexión SSH, además de la información necesaria para acceder a la base de datos')
        print('Heimdal se encargará de realizar una copia de la base de datos y descargarla en su dispositivo')
        instance.heindalConfiguration = HeimdalConfiguration()
        return instance
    
                
    def create_ssh_client(self):
        configuration = self.heindalConfiguration
        client = SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect(
            configuration.ssh_ip, 
            port=configuration.ssh_port, 
            username=configuration.ssh_user, 
            password=configuration.ssh_password
            )
        self.ssh_client = client

    def mysqldump(self):
        config = self.heindalConfiguration
        command = 'mysqldump -u ' + config.user + ' -p"' + config.password + '" ' + config.database + ' > database.sql'
        self.execute_command(command)
    
    def create_scp_client(self):
        self.scp_client = SCPClient(self.ssh_client.get_transport())
   
    def get_database_file(self):
        self.create_scp_client()
        self.scp_client.get(remote_path="database.sql",local_path=self.get_backup_path())
        self.remote_delete_mysqldump()
        self.close()
        
    def remote_delete_mysqldump(self):
        command = 'rm database.sql'
        self.execute_command(command)
    
    def execute_command(self,command: str):
         try:
            self.ssh_client.exec_command(command)
         except:
            raise Exception('SSH client has not been created. Please, call create_ssh_client method before executing a command')
    
    def get_backup_path(self):
        today = date.today()
        backup_path = os.getenv("BACKUP_PATH") + 'database' + '-' + today.__str__() + '.sql'
        return backup_path
    
    def close(self):
        self.ssh_client.close()
        self.scp_client.close()
        
