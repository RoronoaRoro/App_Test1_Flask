CREATE USER 'test_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'testpassword';
GRANT SELECT, INSERT ON App_Test1_Flask.* TO 'test_user'@'localhost';
FLUSH PRIVILEGES;