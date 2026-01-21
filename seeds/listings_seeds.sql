-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS listings CASCADE;
DROP SEQUENCE IF EXISTS listings_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS listings_id_seq;
CREATE TABLE listings (
    id SERIAL PRIMARY KEY, 
    owner_id INT NOT NULL REFERENCES users(id),
    title VARCHAR(255) NOT NULL,
    price_per_night NUMERIC NOT NULL,
    county VARCHAR(255) NOT NULL,
    listing_description VARCHAR(255),
    img_url TEXT
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO listings (owner_id, title, price_per_night, county, listing_description, img_url) VALUES 
(1, '2 bed apartment', 100.50, 'Hertfordshire', 'lovely stay with breakfast included', 'https://tinyurl.com/ye23e59b'),
(2, '15 bed castle', 3000, 'Edinburgh', 'huge castle, tennis courts', 'https://tinyurl.com/mpm6dnam'),
(3, '40 bed castle', 3000, 'Edinburgh', 'huge castle, tennis courts', 'https://tinyurl.com/mpm6dnam');