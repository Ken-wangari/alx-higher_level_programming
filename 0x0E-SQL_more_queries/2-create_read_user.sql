-- Create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user with a different syntax
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privileges using a different syntax
GRANT SELECT
ON hbtn_0d_2.*
TO 'user_0d_2'@'localhost';

