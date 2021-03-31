To enable the connection between our master and slave nodes, we need the public key (.pub file) of the master into the slave's authorized_keys.

https://scmquest.com/jenkins-master-slave-setup-and-configuration-with-screenshots/

a) Create Master Server & generate the key = ssh-keygen -t rsa (save to a location)  (it will give a token (.pub file) and private key (given filename, moslty /home/ubuntu/.ssh))

b) Create Slave Server and copy master’s .pub file code (token) as per below eg. (you will find it on => .ssh/)

ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC5oqJrRVgx9c8qKgjafgjQXo9V+g+Ijtj9YuR3AS81/0KhTR0P5FQ9PvPPnj2kXYmfMOx/PjBYIVmh8Ihf9dDE9WsiW22HTgfVGIjW8TTC4/fbsEgpnXONQId/mZ4C2/8vD+8ve+vSE6f/6o2lFqu0ky0ButiNhp+fb19zXPihZDvXAcWRV+7hbP3//bfrtlsfTOjTWhUpwrcuiL7knwUnnLseK8AvgrR2D7k5bCF9FxPe4mi/+W/gjowHFeNOHFJzN/ubvsNn2++Y1Ae4R7xGVN+jumkcz0hDzFkgI2iKc996B18wucwAqCAScxhGIMFUrIfln9Luv4ac6JtWgItp ubuntu@ip-172-31-38-189

*Now, this code is concate to slave’s authorised key (token) into .ssh dir

Now, we have Master Server’s pub key into Slave Server’s directory = .ssh/authorized_keys

c) Create New Node in Jenkins and follow given points
    i) Manage Plugin-> Manage Node-> New Node
i) Remote root directory = /home/ubuntu 
ii) Launch method = Launch Agents Via SSH
                a) Host -> if same region & same network -> Slave Server’s Private IP else public ip
iii)* (imp part) In Add credentials 
    > Kind => Choose “SSH Username with private key” in Kind
> Username => ubuntu
    > Private Key => Master Server’s Generated Key (private key)
    
    (remain as it is for ID, Description (blank) )

            iv) Host Key Verification Strategy = Manually Trusted Key Verf Strategy

            Click to Add and select this credential and select this credentials

            Now, Save and it will create a Slave Node and must be run successfully.

            Note :- Java must be install in slave node (slave machine)
                sudo apt install default-jre            
                sudo apt install openjdk-11-jre-headless
                sudo apt install openjdk-8-jre-headless
