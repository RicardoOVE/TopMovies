-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema topmovies
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema topmovies
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `topmovies` DEFAULT CHARACTER SET utf8 ;
USE `topmovies` ;

-- -----------------------------------------------------
-- Table `topmovies`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `topmovies`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(150) NULL,
  `nickname` VARCHAR(150) NULL,
  `email` VARCHAR(150) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `topmovies`.`movies`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `topmovies`.`movies` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `imdbid` VARCHAR(255) NULL,
  `type` VARCHAR(45) NULL,
  `y` VARCHAR(45) NULL,
  `plot` TEXT NULL,
  `liked` INT NULL,
  `disliked` INT NULL,
  `favorited` INT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `topmovies`.`interactions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `topmovies`.`interactions` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `comment` TEXT NULL,
  `liked` TINYINT NULL,
  `disliked` TINYINT NULL,
  `favorited` TINYINT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `user_id` INT NOT NULL,
  `movie_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_interactions_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_interactions_movies1_idx` (`movie_id` ASC) VISIBLE,
  CONSTRAINT `fk_interactions_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `topmovies`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_interactions_movies1`
    FOREIGN KEY (`movie_id`)
    REFERENCES `topmovies`.`movies` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
