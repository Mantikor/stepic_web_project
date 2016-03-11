sudo /etc/init.d/mysql restart
sudo mysql -uroot -e "CREATE DATABASE qa;"
sudo mysql -uroot -e "GRANT ALL PRIVILEGES ON qa.* TO 'root'@'localhost' WITH GRANT OPTION;"
