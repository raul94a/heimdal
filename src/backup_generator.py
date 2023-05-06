import heimdal as h

heimdal = h.Heimdal()

heimdal.create_ssh_client()
heimdal.mysqldump()
heimdal.get_database_file()

