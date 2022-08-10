-- creates the database hbtn_0d_2 and user_0d_2
-- The user has SELECT privilege with password user_0d_2_pwd
CREATE DATABASE
	IF NOT EXISTS hbtn_0d_2;
CREATE USER
	IF NOT EXISTS 'user_0d_2'@'localhost'
	IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT
	ON hbtn_od_2.*
	TO 'user_0d_2'@'localhost';
