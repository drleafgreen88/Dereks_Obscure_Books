DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS publishers;
DROP TABLE IF EXISTS authors;

CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

CREATE TABLE publishers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    author_id INT NOT NULL REFERENCES authors(id),
    publisher_id INT NOT NULL REFERENCES publishers(id),
    genre VARCHAR(255),
    buying_price INT NOT NULL,
    selling_price INT NOT NULL
);