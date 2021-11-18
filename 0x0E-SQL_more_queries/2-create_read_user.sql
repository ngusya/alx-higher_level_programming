-- Createss database and user
-- Creates database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Creates user user_0d_2
CREATE USER IF NOT EXISTS user_0d_2@localhost;
-- Sets password to pwd
SET PASSWORD FOR user_0d_2@localhost = "user_0d_2_pwd";
-- Grants select privileges
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
