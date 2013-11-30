#!/bin/bash
#
#-----------------------------------
# @autor: Wendell P. Barreto
# @email: wendellp.barreto@gmail.com
# @project: hi_db
# @doc: dependencies.sh
# @desc: 
# ----------------------------------

echo "[>] Installing python-setuptools (apt-get install python-setuptools)."
sudo apt-get install python-setuptools

echo "[>] Installing python-pip (apt-get install python-pip)."
sudo apt-get install python-pip

echo "[>] Installing aptitude (apt-get install python-aptitude)."
sudo apt-get install aptitude

echo "[>] Installing dependencies (libpq-dev python-dev psycopg2 setproctitle)..."
sudo apt-get install libpq-dev python-dev

echo "[>] Installing PostgreSQL v9.3"
sudo apt-get install postgresql-9.3 postgresql-contrib-9.3

echo "[#] Creating PostgreSQL user (see more http://www.postgresql.org/docs/9.3/static/app-createuser.html)"
echo "[#] Username: hi_admin"
sudo -u postgres createuser -s -D -P hi_admin

echo "[#] Creating PostgreSQL batabase (see more http://www.postgresql.org/docs/9.3/static/app-createdb.html)"
echo "[#] Database: hi_db"
sudo -u postgres createdb -O hi_admin -E UTF8 hi_db
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE hi_db TO hi_admin"
sudo -u postgres psql -d hi_db -c 'CREATE EXTENSION hstore'

echo "[>] Copying pg_hba.conf to PostgreSQL directory..."
sudo cp -f confs/postgresql/pg_hba.conf /etc/postgresql/9.3/main/
sudo chown postgres:postgres /etc/postgresql/9.3/main/pg_hba.conf

echo "[>] Restarting PostgreSQL server..."
sudo service postgresql restart