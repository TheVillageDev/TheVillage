#!/bin/bash
if [ $1 ]; then
	username=$1;
	password=$2;
else
	echo "Database username: ";
	read username;
	echo "Database password: ";
	read password;
fi;

echo "lösche alte datenbank";
cat DROP_DATABASE.sql | mysql -u $username -p$password
echo "erstelle neue datenbank";
cat CREATE_DATABASE.sql | mysql -u $username -p$password
echo "erstelle tabellen";
cat CREATE_TABLES.sql | mysql -u $username -p$password
echo "insert data";
# cat INSERT_REQUIRED.sql | mysql -u $username -p$password
# cat INSERT_EXAMPLES.sql | mysql -u $username -p$password

