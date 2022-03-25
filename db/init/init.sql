CREATE DATABASE IF NOT EXISTS mysite CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
CREATE USER IF NOT EXISTS 'mysiteuser'@'%' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON mysite.* TO 'mysiteuser'@'%';
GRANT ALL PRIVILEGES ON test_database.* TO 'mysiteuser'@'%';

FLUSH PRIVILEGES;
