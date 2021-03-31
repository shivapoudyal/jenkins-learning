
1) Create a folder for storing sql backups into local (own prefer)

----------------> shell script file work ------------------->

2) take sql backup into folder 
    i)      if mysql is not docker container
                mysqldump -u root -ptradeindia current_db > ./current_db.sql (tradeindia - password, pestco -dbname)
    
    ii)     if mysql is docker container
                docker exec CONTAINER /usr/bin/mysqldump -u root --password=root DATABASE > backup.sql
                #$ docker exec some-mysql sh -c 'exec mysqldump --all-databases -uroot -p"$MYSQL_ROOT_PASSWORD"' > /some/path/on/your/host/all-databases.sql #(for multi db)

    iii)    better add user (ubuntu) to docker group (for non-root user docker accessing)

3) Create an IAM user with S3 Create permission

4) Login with user credential ie. access key, secret key

    i)  export AWS_ACCESS_KEY_ID=AKIAZM3ZSMWZCMUSUC7S
    ii) export AWS_SECRET_ACCESS_KEY=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

5) Ref. shell script file - work-tut/sql-backup.sh

6) Install AWS CLI
    sudo apt-get install awscli

7) shell script file must have executable permission
    sudo chmod 666 file.sh

8) Add user into docker group
    sudo usermod -G docker username

9) Give excecutable permission to docker
    sudo chmod 666 /var/run/docker.sock    

7) RUN shell file
    ./file.sh param1 param2 param3    
------------------------------------------------------------ WORK IN JENKINS --------------------------------------

1) Create a parametrised job

2) Install mysql for accessing the mysql
    sudo apt install mysql-client-core-5.7

3) Add mysql password as secret key into jenkins
    1) goto manage credentials -> Global credentials (unrestricted) -> Add Credentials -> Kind (Secret Text) -> ID as ref. name & Password as mysql pass
    2) Select Secret text on parameterized job

4) Job Shell Command Eg.
    /home/slave01/sql-backup.sh $DB_USER $DB_PASSWORD $CONTAINER_NAME $DB_NAME $BUCKET_NAME $AWS_ACCESS_KEY_ID $AWS_SECRET_ACCESS_KEY    
