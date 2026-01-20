-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users;

-- Then, we recreate them
CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) NOT NULL,
    password_hash VARCHAR(255) NOT NULL
    );

-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (name, email, password_hash) VALUES 
('Fred Smith', 'fred@smith.com', 'fred123');
('Sam Jones', 'sam@jones.com', 'sam123');
('Matthew Wiggans', 'matthew@wiggans.com', 'matthew123');
('Dani Rojas', 'dani@rojas.com', 'rojas123');