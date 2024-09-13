-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS bookings;
DROP SEQUENCE IF EXISTS bookings_id_seq;
DROP TABLE IF EXISTS listings;
DROP SEQUENCE IF EXISTS listings_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;


-- Create the table without the foreign key first.
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username text
);

-- Then the table with the foreign key second.
CREATE TABLE listings (
    id SERIAL PRIMARY KEY,
    name text,
    description text,
    location text,
    price int,
    user_id int,
    constraint fk_user foreign key(user_id)
        references users(id)
        on delete cascade
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    listing_id INT,
    requester_id INT,
    requester_name TEXT,
    start_date DATE,
    end_date DATE,
    status TEXT, 
    listing_name TEXT,
    price INT,
    CONSTRAINT fk_listing FOREIGN KEY(listing_id) REFERENCES listings(id) ON DELETE CASCADE,
    CONSTRAINT fk_user FOREIGN KEY(requester_id) REFERENCES users(id) ON DELETE CASCADE
);

INSERT INTO users (username) VALUES ('Catherine');
INSERT INTO users (username) VALUES ('Sarah');
INSERT INTO users (username) VALUES ('Andy');



INSERT INTO listings (name, description, location, price, user_id) VALUES ('Blackpool Tower', 'Really high', 'Blackpool', 25, 1);
INSERT INTO listings (name, description, location, price, user_id) VALUES ('London Eye', 'Really round', 'London', 150, 1);
INSERT INTO listings (name, description, location, price, user_id) VALUES ('Windsor Castle', 'Really old', 'Windsor', 1150, 2);
INSERT INTO listings (name, description, location, price, user_id) VALUES ('SS Great Britain', 'Really wet', 'Bristol', 180, 3);


INSERT INTO bookings (listing_id, requester_id, requester_name, start_date, end_date, status, listing_name, price) VALUES (1, 2, 'Sarah', '2023-09-10', '2023-09-12', 'requested', 'Blackpool Tower', 25);
INSERT INTO bookings (listing_id, requester_id, requester_name, start_date, end_date, status, listing_name, price) VALUES (1, 3, 'Andy', '2023-10-10', '2023-10-12', 'requested', 'Blackpool Tower', 25);
INSERT INTO bookings (listing_id, requester_id, requester_name, start_date, end_date, status, listing_name, price) VALUES (2, 3, 'Andy','2023-06-15', '2023-06-20', 'confirmed', 'London Eye', 150);
INSERT INTO bookings (listing_id, requester_id, requester_name, start_date, end_date, status, listing_name, price) VALUES (2, 3, 'Andy','2023-12-15', '2023-12-20', 'confirmed', 'London Eye', 150);
INSERT INTO bookings (listing_id, requester_id, requester_name, start_date, end_date, status, listing_name, price) VALUES (3, 1, 'Catherine', '2023-12-10', '2023-12-10', 'requested','Windsor Castle', 1150);
