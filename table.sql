DROP TABLE cars4sale;
CREATE TABLE IF NOT EXISTS cars4sale(
    id serial PRIMARY KEY,
    cartype text,
    manufacturer text,
    model text,
    mileage int,
    price int,
    leatherseats text
);

