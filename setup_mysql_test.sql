--  Creates a MySQL server with:
--    A database hbnb_test_db
--    A new user hbnb_test (in localhost)
--    password of hbnb_test should match hbnb_test_pwd
--    hbnb_test(user) has all privileges on the database hbnb_test_db(only)
--    hbnb_test should have SELECT privilege on the database performance_schema(only)

--  create a new database hbnb_test_db, if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

--  Create a new user hbnb_dev (in localhost)
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY '123Hbnb_test_pwd$';

-- hbnb_test(user) has all privileges on the database hbnb_test_db(only)
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- hbnb_test has SELECT privilege on the database performance_schema(only)
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Flush privileges for changes
FLUSH PRIVILEGES;
