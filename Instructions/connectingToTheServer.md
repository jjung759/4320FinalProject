## In case you want to access our production server, the following information may be helpful
### Currently, our server is configured to run on an AWS Ubuntu server. Primarily, most server operations are being served through Python.
#### If you would like access to the production server, please message me (jim) in regards to getting setup with the ssh credentials.
#### Accessing our server through the terminal:
* ##### Any AWS terminal can be remotely logged into utilizing the github shell. In order to access the server, navigate to the directory in which you stored the .pem file, and issue the following command:
```Apache
ssh -i "4320keypair.pem" ubuntu@ec2-54-202-84-25.us-west-2.compute.amazonaws.com
```
* ##### When you attempt to access the server, you may be prompted whether you wish to connect to the server. Just enter (or click) Yes.
#### Connecting to the Server via Filezilla:
* ##### The following image contains instructions on connecting to the server via Filezilla. This makes file uploading wayyyyy easier
* ##### Note: since we're operating a ubuntu server, make sure to use username "ubuntu" when storing the login credentials
* ##### Again, if you need the .pem file, message me
![Connecting Filezilla to ec2](https://github.com/jjung759/4320FinalProject/blob/master/Instructions/images/ec2Filezilla.png)
* ##### Credits for instructions goes to Professor Wergeles, from CS2830 Spring 2017
