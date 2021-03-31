
1) Create New user
    adduser username

# 1) Jenkins Local Path
#     /home/jenkins/jenkins-data

2) Jenkins Docker Path
    /var/jenkins_home

3) Jenkins Password Path
    /var/jenkins_home/secrets/initialAdminPassword (also find into local mounted dir)

4) Create New Admin User & Password    

------------------------------------------------ FOR SLAVE NODE ------------------------------

1) Create another machine Run project on this machine (mysql, node, php, nginx)

2) Connect with master
    create an user and connect this node via this created user

-------------------------------------------- PERFORM ACTION ON SLAVE SERVER FROM MASTER SERVER ----------------------

1) go to jenkins url (jenkins installed on master)  
    a) create job -> mark checked on "Restrict where this project can be run" -> choose node server -> now create anything
    b) it will create to slave node server