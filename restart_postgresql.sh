#!/bin/bash
#
#-----------------------------------
# @autor: Wendell P. Barreto
# @email: wendellp.barreto@gmail.com
# @project: Hi
# @doc: dependencies.sh
# @desc: 
# ----------------------------------


sudo -u postgres psql -c "DROP DATABASE hi_db"
sudo -u postgres createdb -O hi_admin -E UTF8 hi_db
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE hi_db TO hi_admin"

echo "[>] Syncing db..."
python manage.py syncdb --migrate

echo "[>] Collecting static files..."
python manage.py collectstatic --no-input

echo "[>] Starting server..."
python manage.py runserver