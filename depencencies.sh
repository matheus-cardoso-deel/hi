#!/bin/bash
#
#-----------------------------------
# @autor: Wendell P. Barreto
# @email: wendellp.barreto@gmail.com
# @project: Hi
# @doc: dependencies.sh
# @desc: 
# ----------------------------------

#echo "[\/] Entering virtual environment..."
. $HOME/.virtualenvs/hi/bin/activate

#echo "[>] Installing Django v.1.5.2..."
pip install Django==1.5.2

#echo "[>] Installing Grapelli v.1.5.2..."
pip install django-grappelli==2.4.6

#echo "[>] Installing South v.1.5.2..."
pip install South==0.8.2

#echo "[>] Installing Unipath v.1.5.2..."
pip install Unipath==1.0

#echo "[>] Installing PostgreSQL dependencies..."
pip install psycopg2
pip install setproctitle

#echo "[\/] Showing project dependencies!"
pip freeze