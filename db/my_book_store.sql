DROP TABLE IF EXISTS authors;
DROP TABLE IF EXISTS publishers;
DROP TABLE IF EXISTS books;

CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

CREATE TABLE publishers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
)

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    publisher_id INT NOT NULL REFERENCES publishers(id),
    author_id INT NOT NULL REFERENCES authors(id),
    genre VARCHAR(255),
    buying_price INT NOT NULL,
    selling_price INT NOT NULL
);