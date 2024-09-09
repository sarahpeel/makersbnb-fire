-- First, we must delete (drop) all our tables
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
    availability int ARRAY,
    price int,
    occupied boolean,
    user_id int,
    constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);


INSERT INTO users (username) VALUES ('Catherine');
INSERT INTO users (username) VALUES ('Sarah');
INSERT INTO users (username) VALUES ('Andy');
