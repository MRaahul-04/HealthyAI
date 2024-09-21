# HealthyAI
AI Healthcare, mental health and appointment booking bot


##### Database Configuration and Setup ####
1.1. Create MySQL Database and Tables

1. Open phpMyAdmin at http://localhost/phpmyadmin.
2. Create a database named healthyai_db.
3. Run the following SQL scripts to create tables in the healthyai_db database:


##### SQL configuration #####

-- Create users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

-- Create conversations table
CREATE TABLE conversations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    message TEXT,
    response TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Create appointments table
CREATE TABLE appointments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    name VARCHAR(100),
    date DATE,
    time TIME,
    reason TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);


