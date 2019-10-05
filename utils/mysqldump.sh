#!/bin/bash
cp ../data/landlord.sql ../data/backups/landlord-$RANDOM.sql
docker exec landlord_data /usr/bin/mysqldump -u landlord --password=hackupstate landlord > ../data/landlord.sql
