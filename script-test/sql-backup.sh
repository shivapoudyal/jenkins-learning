DB_USER=$1
DB_PASSWORD=$2
CONTAINER_NAME=$3
DB_NAME=$4 
BUCKET_NAME=$5
AWS_ACCESS_KEY_ID=$6
AWS_SECRET_ACCESS_KEY=$7
BACKUP_DB_NAME=backup_$( date '+%Y-%m-%d_%H:%M:%S' ).sql


# mysqldump -u $DB_USER -p$DB_PASSWORD -h $DB_HOST $DB_NAME > /home/anyuser/mysql-db-backup/$BACKUP_DB_NAME && \ #(for non-docker)

docker exec $CONTAINER_NAME /usr/bin/mysqldump -u $DB_USER --password=$DB_PASSWORD $DB_NAME > /home/remote-user2/mysql-db-backup/$BACKUP_DB_NAME #(for docker)

export AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID && \
export AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY && \

echo "deleting old sql backup from s3 bucket" && \

aws s3 rm --recursive s3://$BUCKET_NAME/ 	#(removes other older sql files from s3 bucket)

echo "uploading new sql backup to s3 bucket" && \

aws s3 cp /home/remote-user2/mysql-db-backup/$BACKUP_DB_NAME s3://$BUCKET_NAME
