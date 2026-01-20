-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS bookings CASCADE;
DROP SEQUENCE IF EXISTS bookings_id_seq;


-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
id SERIAL PRIMARY KEY,
guest_id int,
listing_id INT,
start_date DATE,
end_date DATE,
checkout_date DATE, 
booking_price NUMERIC(10,2),

CONSTRAINT fk_guest_id FOREIGN KEY (guest_id)
REFERENCES users(id),

CONSTRAINT fk_listing_id FOREIGN KEY (listing_id)
REFERENCES listings(id)
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO bookings (guest_id, listing_id, start_date, end_date, checkout_date, booking_price) 
VALUES (1, 3, 2026-01-20, 2026-01-21, 2026-01-20, 50.00), 
    (2, 2, 2026-01-28, 2026-01-29, 2026-01-15, 77.00),
    (3, 1, 2026-02-10, 2026-02-11, 2026-01-18, 100.00),
    (1, 3, 2026-01-25, 2026-01-26, 2026-01-19, 50.00),
    (2, 3, 2026-01-21, 2026-01-22, 2026-01-20, 50.00)
    ;