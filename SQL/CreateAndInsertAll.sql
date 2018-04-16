DROP TABLE IF EXISTS Customer;
DROP TABLE IF EXISTS News_Favorites;

CREATE TABLE Customer(
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `firstname` varchar(255) NOT NULL,
    `middlename` varchar(255),
    `lastname` varchar(255) NOT NULL,
    `email` varchar(255) NOT NULL UNIQUE,
    `username` varchar(255) NOT NULL UNIQUE,
    `passwordHash` BINARY(64) NOT NULL
);

CREATE TABLE News_Favorites(
  `customerID` INT NOT NULL,
  `title` varchar(255) NOT NULL,
  `author` varchar(255) NOT NULL,
  `body` MEDIUMTEXT,
  FOREIGN KEY (`customerID`) REFERENCES Customer(`id`)
);

INSERT INTO `Customer` (`id`, `firstname`, `middlename`, `lastname`, `email`, `username`) VALUES
  (10000000, 'Tristin', 'William', 'Snyder', 'twsbqb@mail.missouri.edu', 'twsbqb');
