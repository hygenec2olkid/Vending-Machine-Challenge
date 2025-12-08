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
    img_url VARCHAR(512),
    CHECK (price >= 0),
    CHECK (quantity >= 0)
);

INSERT INTO product_inventory (name, price, quantity, img_url) VALUES
('Sparkling Water', 150, 10, "https://images.mango-prod.siammakro.cloud/product-images/7248016179395-55c3023a-55e7-4676-9fe6-e0797fef9793.jpeg?eo-img.resize=w%2F1080&eo-img.format=webp"),
('Potato Crisps', 100, 5, "https://images.mango-prod.siammakro.cloud/product-images/6761213755587-b02cbc75-768b-4d9e-8db7-d8198bbc4dac.jpeg?eo-img.resize=w%2F1080&eo-img.format=webp"),
('Cola Can', 200, 15, "https://images.mango-prod.siammakro.cloud/product-images/6761214836931-dfb8c29d-949b-44a4-b7a5-e8c02dbe697a.jpeg?eo-img.resize=w%2F1080&eo-img.format=webp"),
('Diet Lemonade', 210, 8, "https://images.mango-prod.siammakro.cloud/product-images/6814746706115-9bb16bf9-ab40-4c45-8239-71a23ca3e978.jpeg?eo-img.resize=w%2F1080&eo-img.format=webp"),
('Orange Juice', 250, 6, "https://images.mango-prod.siammakro.cloud/product-images/7078661685443-ae05f8e4-e597-4a46-9e1f-4ef45656813c.jpeg?eo-img.resize=w%2F1080&eo-img.format=webp"),
('Espresso Shot', 300, 4, "https://images.mango-prod.siammakro.cloud/product-images/6761200812227-18283405-61ac-4c15-b7db-6efe2b635664.jpeg?eo-img.resize=w%2F1080&eo-img.format=webp"),
('Milk Chocolate', 180, 12, "https://o2o-static.lotuss.com/products/117944/162585400.jpg"),
('Dark Chocolate', 220, 7, "https://images.mango-prod.siammakro.cloud/SOURCE/fe98c40e8c80436896b020613490db3b?eo-img.resize=w%2F1080&eo-img.format=webp"),
('Peanut Butter Cups', 190, 9, "https://down-th.img.susercontent.com/file/th-11134207-7r98r-lzc4uluk7kw1d8.webp"),
('Gum (Mint)', 75, 20, "https://images.mango-prod.siammakro.cloud/SOURCE/3eb724cc7c914761b97dcd8b9376b71e?eo-img.resize=w%2F1080&eo-img.format=webp"),
('Gummy Worms', 120, 10, "https://images.mango-prod.siammakro.cloud/product-images/7325024616643-edffbdd2-4800-4f41-b9d4-67ef8873b96f.jpeg?eo-img.resize=w%2F1080&eo-img.format=webp"),
('Almond Mix', 350, 5, "https://images.mango-prod.siammakro.cloud/SOURCE/402d76a840ea469c88958d02458a89ce?eo-img.resize=w%2F1080&eo-img.format=webp"),
('Protein Bar', 400, 3, "https://shop.biotechusa.com/cdn/shop/files/Protein_bar_double_choco.png?v=1710404349"),
('Fruit Leather', 160, 10, "https://images.mango-prod.siammakro.cloud/product-images/7352709054659-92860e3f-ca3b-432d-ad3e-62aee3dccab7.jpeg?eo-img.resize=w%2F1080&eo-img.format=webp"),
('Pain Reliever', 500, 2, "https://images.mango-prod.siammakro.cloud/product-images/717973247939295-04574935-32e1-44ad-bfbd-c239a22b7e47.jpeg?eo-img.resize=w%2F1080&eo-img.format=webp"), 
('Hand Sanitizer', 320, 4, "https://images.mango-prod.siammakro.cloud/SOURCE/e84718e623e84631807ca1aebfd761f5?eo-img.resize=w%2F1080&eo-img.format=webp"),
('Small Notebook', 175, 5, "https://down-th.img.susercontent.com/file/sg-11134201-7rdy5-mbp8u4hjoi8e5a.webp"),
('Energy Drink', 290, 11, "https://images.mango-prod.siammakro.cloud/SOURCE/62edeeaf63b94cc4a5f812673a0fd8de?eo-img.resize=w%2F1080&eo-img.format=webp"),
('Water Bottle (Large)', 275, 9, "https://images.mango-prod.siammakro.cloud/product-images/6814746017987-5df99555-8614-473d-b3b4-b48c65f9a355.jpeg?eo-img.resize=w%2F1080&eo-img.format=webp"),
('Licorice Bites', 130, 8, "https://images.mango-prod.siammakro.cloud/product-images/7350146564291-146a9c82-4125-4cb5-b2e8-515106f99840.jpeg?eo-img.resize=w%2F1080&eo-img.format=webp")
ON DUPLICATE KEY UPDATE name = name;