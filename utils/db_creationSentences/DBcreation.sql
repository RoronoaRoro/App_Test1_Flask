-- MySQL Script generated by MySQL Workbench
-- Sun Apr 16 22:09:36 2023
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema App_Test1_Flask
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema App_Test1_Flask
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `App_Test1_Flask` DEFAULT CHARACTER SET utf8 ;
USE `App_Test1_Flask` ;

-- -----------------------------------------------------
-- Table `App_Test1_Flask`.`region`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `App_Test1_Flask`.`region` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `App_Test1_Flask`.`comuna`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `App_Test1_Flask`.`comuna` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(200) NOT NULL,
  `region_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_comuna_region1_idx` (`region_id` ASC),
  CONSTRAINT `fk_comuna_region1`
    FOREIGN KEY (`region_id`)
    REFERENCES `App_Test1_Flask`.`region` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `App_Test1_Flask`.`donacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `App_Test1_Flask`.`donacion` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `comuna_id` INT NOT NULL,
  `calle_numero` VARCHAR(80) NOT NULL,
  `tipo` ENUM('fruta', 'verdura', 'otro') NOT NULL,
  `cantidad` VARCHAR(10) NOT NULL,
  `fecha_disponibilidad` TIMESTAMP NOT NULL,
  `descripcion` VARCHAR(80) NULL,
  `condiciones_retirar` VARCHAR(80) NULL,
  `nombre` VARCHAR(80) NOT NULL,
  `email` VARCHAR(80) NOT NULL,
  `celular` VARCHAR(15) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_donacion_comuna1_idx` (`comuna_id` ASC),
  CONSTRAINT `fk_donacion_comuna1`
    FOREIGN KEY (`comuna_id`)
    REFERENCES `App_Test1_Flask`.`comuna` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `App_Test1_Flask`.`foto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `App_Test1_Flask`.`foto` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `ruta_archivo` VARCHAR(300) NOT NULL,
  `nombre_archivo` VARCHAR(300) NOT NULL,
  `donacion_id` INT NOT NULL,
  PRIMARY KEY (`id`, `donacion_id`),
  INDEX `fk_foto_donacion1_idx` (`donacion_id` ASC),
  CONSTRAINT `fk_foto_donacion1`
    FOREIGN KEY (`donacion_id`)
    REFERENCES `App_Test1_Flask`.`donacion` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `App_Test1_Flask`.`pedido`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `App_Test1_Flask`.`pedido` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `comuna_id` INT NOT NULL,
  `tipo` ENUM('fruta', 'verdura', 'otro') NOT NULL,
  `descripcion` VARCHAR(80) NOT NULL,
  `cantidad` VARCHAR(10) NOT NULL,
  `nombre_solicitante` VARCHAR(80) NOT NULL,
  `email_solicitante` VARCHAR(80) NOT NULL,
  `celular_solicitante` VARCHAR(15) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_pedido_comuna1_idx` (`comuna_id` ASC),
  CONSTRAINT `fk_pedido_comuna10`
    FOREIGN KEY (`comuna_id`)
    REFERENCES `App_Test1_Flask`.`comuna` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;