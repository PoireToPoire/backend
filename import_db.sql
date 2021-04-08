-- Adminer 4.8.0 MySQL 8.0.23 dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP DATABASE IF EXISTS `cubesdb`;
CREATE DATABASE `cubesdb`;
USE `cubesdb`;

DROP TABLE IF EXISTS `address`;
CREATE TABLE `address` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userID` int NOT NULL,
  `country` varchar(25) NOT NULL DEFAULT '',
  `state` varchar(25) NOT NULL DEFAULT '',
  `city` varchar(25) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `userID2` (`userID`),
  CONSTRAINT `FK_address_user` FOREIGN KEY (`id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `events`;
CREATE TABLE `events` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userID` int NOT NULL,
  `addressID` int NOT NULL,
  `eventID` int NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_events_user` (`userID`),
  KEY `FK_events_address` (`addressID`),
  CONSTRAINT `FK_events_address` FOREIGN KEY (`addressID`) REFERENCES `address` (`id`),
  CONSTRAINT `FK_events_user` FOREIGN KEY (`userID`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `fiendlist`;
CREATE TABLE `fiendlist` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userID` int NOT NULL,
  `friendID` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_fiendlist_user` (`userID`),
  KEY `FK_fiendlist_user_2` (`friendID`),
  CONSTRAINT `FK_fiendlist_user` FOREIGN KEY (`userID`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_fiendlist_user_2` FOREIGN KEY (`friendID`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `group`;
CREATE TABLE `group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ownerID` int NOT NULL,
  `category` varchar(25) NOT NULL DEFAULT '',
  `name` varchar(25) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `FK_group_user` (`ownerID`),
  CONSTRAINT `FK_group_user` FOREIGN KEY (`ownerID`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `participant`;
CREATE TABLE `participant` (
  `id` int(10) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `userID` int NOT NULL,
  `eventID` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_participant_user` (`userID`),
  KEY `eventID` (`eventID`),
  CONSTRAINT `FK_participant_events` FOREIGN KEY (`eventID`) REFERENCES `events` (`id`),
  CONSTRAINT `FK_participant_user` FOREIGN KEY (`userID`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `post`;
CREATE TABLE `post` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userID` int NOT NULL,
  `parentID` int NOT NULL,
  `title` varchar(25) NOT NULL DEFAULT '',
  `content` varchar(25) NOT NULL DEFAULT '',
  `category` varchar(25) NOT NULL DEFAULT '',
  `type` tinyint NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `FK_post_user` (`userID`),
  KEY `FK_post_post` (`parentID`),
  CONSTRAINT `FK_post_post` FOREIGN KEY (`parentID`) REFERENCES `post` (`id`),
  CONSTRAINT `FK_post_user` FOREIGN KEY (`userID`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `type` int NOT NULL DEFAULT '1',
  `suspended` tinyint NOT NULL DEFAULT '0',
  `lastname` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `firstname` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `mail` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `birthdate` date NOT NULL,
  `bio` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `gender` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `image_path` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_as_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `userType` (`type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS `usertype`;
CREATE TABLE `usertype` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userID` int NOT NULL,
  `libelle` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `code` tinyint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_usertype_user` (`userID`),
  CONSTRAINT `FK_usertype_user` FOREIGN KEY (`userID`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- 2021-04-04 20:54:53

INSERT INTO `user` (`id`, `type`, `suspended`, `lastname`, `firstname`, `mail`, `birthdate`, `bio`, `gender`, `password`, `image_path`) VALUES
(1,	1,	0,	'Richard',	'Arthur',	'arthur.richard@protonmail.com',	'2021-03-28',	NULL,	'M',	'admin123',	'https://randomuser.me/api/portraits/thumb/men/1.jpg'),
(2,	1,	0,	'Dupont',	'Jean',	'jean.dupont@protonmail.com',	'2021-04-02',	NULL,	'M',	'jean123',	'https://randomuser.me/api/portraits/thumb/men/2.jpg'),
(4,	1,	0,	'Dupont',	'Marie',	'marie.dupont@protonmail.com',	'2021-04-04',	NULL,	'F',	'marie123',	'https://randomuser.me/api/portraits/thumb/women/1.jpg');