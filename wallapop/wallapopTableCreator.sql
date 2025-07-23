DROP TABLE IF EXISTS products;

CREATE TABLE products (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status ENUM('available', 'sold', 'reserved') NOT NULL DEFAULT 'available',
    price DECIMAL(10, 2) NOT NULL,
    location VARCHAR(255),
    distance FLOAT,
    brand VARCHAR(255),
    model VARCHAR(255),
    version VARCHAR(255),
    year INT,
    kilometers INT,
    fuel ENUM('Gasoline', 'Diesel', 'Electric', 'Hybrid', 'Other'),
    gearbox ENUM('manual', 'automatic'),
    horsepower FLOAT,
    creation_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    modification_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    url VARCHAR(255) NOT NULL UNIQUE
);