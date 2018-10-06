CREATE TABLE passengers (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    flight_id INTEGER REFERENCES flights
);

INSERT INTO passengers (name, flight_id) VALUES ('Alice', 1);
INSERT INTO passengers (name, flight_id) VALUES ('Bob', 1);
INSERT INTO passengers (name, flight_id) VALUES ('Charlie', 2);
INSERT INTO passengers (name, flight_id) VALUES ('Diane', 2);
INSERT INTO passengers (name, flight_id) VALUES ('Eric', 4);
INSERT INTO passengers (name, flight_id) VALUES ('Francine', 6);
INSERT INTO passengers (name, flight_id) VALUES ('Greg', 6);


SELECT origin, destination, name FROM flights INNER JOIN passengers ON passengers.flight_id = flights.id;
SELECT origin, destination, name FROM flights JOIN passengers ON passengers.flight_id = flights.id;
SELECT origin, destination, name FROM flights LEFT OUTER JOIN passengers ON passengers.flight_id = flights.id;
SELECT origin, destination, name FROM flights RIGHT OUTER JOIN passengers ON passengers.flight_id = flights.id;
