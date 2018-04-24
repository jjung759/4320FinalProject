## How to connect to our Database using MySQL Workbench
#### MySQL is a handy interface you can use to interact with our database. I find it a lot cleaner, (and frankly, less intimidating) to use with our database then just accessing via the command line.
#### Download instructions for MySQL database can be found at the following link:
* ##### [MySQL Workbench Download](https://dev.mysql.com/downloads/workbench/)
### Accessing our database:
#### In order to access the database, first click on the plus sign next to MySQL Connections in MySQL Workbench.
#### This will create a new DB Connections
#### Use the following options:
* ##### Connection Name: CS4320
* ##### Connection Method Standard TCP/IP over SSH
* ##### SSH Hostname: ec2-54-202-84-25.us-west-2.compute.amazonaws.com:22
* ##### SSH Username: ubuntu
* ##### SSH Key File: select location of .pem (message me for access)
* ##### MySQL Hostname: localhost
* ##### MySQL Server Port: 3306
* ##### Username: groupmem
##### Click test connection, to test out all settings.
##### When you test the connection, you will be prompted for a password. This should be the same password we'll end up using to authorize all DB calls. For now, just message me for it.
