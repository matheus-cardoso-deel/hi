#!/bin/bash
#
#-----------------------------------
# @autor: Wendell P. Barreto
# @email: wendellp.barreto@gmail.com
# @project: Hi!
# @doc: development.sh
# @desc: 
# ----------------------------------

pip install -r requirements.txt

#echo "[>] Installing python-setuptools (apt-get install python-setuptools)."
apt-get install python-setuptools

apt-get install python-pip

# echo "[>] Installing aptitude (apt-get install python-aptitude)."
# sudo apt-get install aptitude

apt-get install libpq-dev python-dev

#echo "[>] Installing PostgreSQL v9.3"
apt-get install postgresql-9.3 postgresql-contrib-9.3

#echo "[#] Creating PostgreSQL user (see more http://www.postgresql.org/docs/9.3/static/app-createuser.html)"
#echo "[#] Username: hi_admin"
postgres createuser -s -D -P hi_admin

#echo "[#] Creating PostgreSQL batabase (see more http://www.postgresql.org/docs/9.3/static/app-createdb.html)"
#echo "[#] Database: hi_db"
postgres createdb -O hi_admin -E UTF8 hi_db
postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE hi_db TO hi_admin"

#echo "[>] Copying pg_hba.conf to PostgreSQL directory..."
cp -f confs/postgresql/pg_hba.conf /etc/postgresql/9.3/main/
chown postgres:postgres /etc/postgresql/9.3/main/pg_hba.conf

#echo "[>] Restarting PostgreSQL server..."
service postgresql restart