CREATE DATABASE communicado;
USE communicado;

CREATE TABLE users (
    userID INT AUTO_INCREMENT PRIMARY KEY,
    role VARCHAR(50),
    username VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    address VARCHAR(200) NOT NULL,
    password VARCHAR(100) NOT NULL
);

CREATE TABLE EventOrganizer (
    userID INT PRIMARY KEY,
    phoneNumber VARCHAR(30),
    FOREIGN KEY (userID) REFERENCES users(userID)
);

CREATE TABLE Customer (
    userID INT PRIMARY KEY,
    phoneNumber VARCHAR(30),
    FOREIGN KEY (userID) REFERENCES users(userID)
);

CREATE TABLE Admin (
    userID INT PRIMARY KEY,
    officeNo VARCHAR(30),
    FOREIGN KEY (userID) REFERENCES users(userID)
);

CREATE TABLE events (
    eventID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    eventDateTime DATETIME NOT NULL,
    location VARCHAR(100),
    capacity INT,
    category VARCHAR(50),  -- Added a length for VARCHAR
    artist VARCHAR(100),   -- Added a length for VARCHAR
    isVerified BOOLEAN,
    adminID INT,
    eventOrganizerID INT,
    FOREIGN KEY (adminID) REFERENCES Admin(userID),
    FOREIGN KEY (eventOrganizerID) REFERENCES EventOrganizer(userID)
);

CREATE TABLE bookedEvent (
    eventID INT PRIMARY KEY,
    quantity INT,
    isPaid BOOLEAN,
    ID INT,
    referenceNumber VARCHAR(40),
    FOREIGN KEY (eventID) REFERENCES events(eventID),
    FOREIGN KEY (ID) REFERENCES users(userID)
);

INSERT INTO users (userID, role, username, email, address, password) VALUES
(1, 'Event Organizer', 'john_doe', 'john@example.com', '123 Main St, Anytown', 'password123'),
(2, 'Event Organizer', 'jane_smith', 'jane@example.com', '456 Elm St, Otherville', 'password456'),
(3, 'Customer', 'bob_jones', 'bob@example.com', '789 Oak St, Anothercity', 'password789'),
(4, 'Admin', 'admin1', 'admin1@example.com', 'Admin Office, City Center', 'adminpass');

INSERT INTO EventOrganizer (userID, phoneNumber) VALUES
(1, '123-456-7890'),
(2, '987-654-3210');

INSERT INTO Admin (userID, officeNo) VALUES
(4, '101');

INSERT INTO Customer (userID, phoneNumber) VALUES
(3, '000-000-0001');

INSERT INTO events (name, eventDateTime, location, capacity, category, artist, isVerified, adminID, eventOrganizerID) VALUES
('Music Concert', '2024-03-10 18:00:00', 'Prospera Place', 500, 'Music', 'Taylor Swift', true, 4, 1),
('Art Exhibition', '2024-04-15 10:00:00', 'Kelowna Art Gallery', 200, 'Art', null, true, 4, 2),
('Food Festival', '2024-05-20 12:00:00', 'Bernard Avenue', 300, 'Food', null, true, 4, 1),
('Technology Conference', '2024-06-25 09:00:00', 'Innovation Center', 1000, 'Tech', null, true, 4, 2),
('Fashion Show', '2024-07-10 15:00:00', 'Delta Hotel Ballroom', 400, 'Fashion', 'Jill Setah', true, 4, 2);

ALTER TABLE events ADD imageURL VARCHAR(100);

UPDATE events SET imageURL = 'musicconcert.jpg' WHERE eventID = 1;
UPDATE events SET imageURL = 'pages/static/artexhibition.jpg' WHERE eventID = 2;
UPDATE events SET imageURL = 'pages/static/foodfestival.jpg' WHERE eventID = 3;
UPDATE events SET imageURL = 'pages/static/technologyconference.jpeg' WHERE eventID = 4;
UPDATE events SET imageURL = 'pages/static/fashionshow.jpeg' WHERE eventID = 5;
