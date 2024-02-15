-- Create the database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the database
USE hbtn_0d_usa;

-- Create the table cities with a foreign key reference to states
CREATE TABLE IF NOT EXISTS cities (
    id INT PRIMARY KEY AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    CONSTRAINT unique_id UNIQUE (id),
    FOREIGN KEY (state_id) REFERENCES states (id)
);

