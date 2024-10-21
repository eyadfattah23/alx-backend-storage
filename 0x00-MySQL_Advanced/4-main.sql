INSERT INTO users (email, name, country) VALUES ("bob@dylan.com", "Bob", "US");
INSERT INTO users (email, name, country) VALUES ("sylvie@dylan.com", "Sylvie", "CO");
INSERT INTO users (email, name) VALUES ("john@dylan.com", "John");


DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS orders;
CREATE TABLE IF NOT EXISTS items (
    name VARCHAR(255) NOT NULL,
    quantity int NOT NULL DEFAULT 10
);
CREATE TABLE IF NOT EXISTS orders (
    item_name VARCHAR(255) NOT NULL,
    number int NOT NULL
);
INSERT INTO items (name) VALUES ("apple"), ("pineapple"), ("pear");



SELECT * FROM items;
SELECT * FROM orders;

INSERT INTO orders (item_name, number) VALUES ('apple', 1);
INSERT INTO orders (item_name, number) VALUES ('apple', 3);
INSERT INTO orders (item_name, number) VALUES ('pear', 2);
INSERT INTO orders (item_name, number) VALUES ('pineapple', 5);

SELECT "--";

SELECT * FROM items;
SELECT * FROM orders;
