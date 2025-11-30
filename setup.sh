#!/usr/bin/env bash
apt update
apt install mysql-server micro -y
pip3 install pycodestyle
service mysql start
git config --global user.email "12495@holbertonstudents.com"
git config --global user.name "islamqasimov"
alias gp="git add .; git commit -m 'autocommit'; git push"
alias mysqlr='mysql -hlocalhost -uroot -p'
