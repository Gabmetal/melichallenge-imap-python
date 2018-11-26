CREATE SCHEMA `MeliChallenge` DEFAULT CHARACTER SET utf8 ;
USE MeliChallenge;
CREATE TABLE `email_devops` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` datetime DEFAULT NULL,
  `subject` varchar(255) DEFAULT NULL,
  `from` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
