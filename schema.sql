CREATE TABLE places(
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(255) NOT NULL,
    county VARCHAR(255),
    country VARCHAR(255)
);

CREATE TABLE people(
    id INT AUTO_INCREMENT PRIMARY KEY,
    given_name VARCHAR(255) NOT NULL,
    family_name VARCHAR(255) NOT NULL,
    date_of_birth DATE,
    place_id INT,
    FOREIGN KEY (place_id) REFERENCES places(id)
)