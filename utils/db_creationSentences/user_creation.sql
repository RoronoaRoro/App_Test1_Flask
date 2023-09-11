CREATE USER 'test_user'@'localhost' IDENTIFIED BY 'testpassword';
GRANT SELECT, INSERT ON App_Test1_Flask.* TO 'test_user'@'localhost';
FLUSH PRIVILEGES;