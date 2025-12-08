CREATE TABLE IF NOT EXISTS coin_stock (
    coin INT PRIMARY KEY,
    quantity INT NOT NULL DEFAULT 0,
    CHECK (coin > 0)
);

INSERT INTO coin_stock (coin, quantity) VALUES
(1, 100),
(5, 50),
(10, 20),
(20, 10),
(50, 10),
(100, 10),
(500, 10),
(1000, 10)
ON DUPLICATE KEY UPDATE quantity = quantity; 

CREATE TABLE IF NOT EXISTS product_inventory (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    price INT NOT NULL,
    quantity INT NOT NULL DEFAULT 0,
    CHECK (price >= 0),
    CHECK (quantity >= 0)
);

INSERT INTO product_inventory (name, price, quantity) VALUES
('Sparkling Water', 150, 10),
('Potato Crisps', 100, 5),
('Cola Can', 200, 15),
('Diet Lemonade', 210, 8),
('Orange Juice', 250, 6),
('Espresso Shot', 300, 4),
('Milk Chocolate', 180, 12),
('Dark Chocolate', 220, 7),
('Peanut Butter Cups', 190, 9),
('Gum (Mint)', 75, 20),
('Gummy Worms', 120, 10),
('Almond Mix', 350, 5),
('Protein Bar', 400, 3),
('Fruit Leather', 160, 10),
('Pain Reliever', 500, 2), 
('Hand Sanitizer', 320, 4),
('Small Notebook', 175, 5),
('Energy Drink', 290, 11),
('Water Bottle (Large)', 275, 9),
('Licorice Bites', 130, 8)
ON DUPLICATE KEY UPDATE name = name;