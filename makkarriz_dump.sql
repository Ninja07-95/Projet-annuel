-- Création de la base de données
CREATE DATABASE IF NOT EXISTS `makkarriz` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `makkarriz`;

-- Table `utilisateur`
DROP TABLE IF EXISTS `utilisateur`;
CREATE TABLE IF NOT EXISTS `utilisateur` (
  `id_utilisateur` BIGINT NOT NULL AUTO_INCREMENT,
  `nom` VARCHAR(100) NOT NULL,
  `email` VARCHAR(191) NOT NULL,
  `role` ENUM('Admin', 'DevSecOps', 'Développeur') NOT NULL,
  `mot_de_passe` VARCHAR(255) NOT NULL COMMENT 'Mot de passe hashé',
  `date_creation` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_utilisateur`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Table `analyse_test`
DROP TABLE IF EXISTS `analyse_test`;
CREATE TABLE IF NOT EXISTS `analyse_test` (
  `id_analyse` BIGINT NOT NULL AUTO_INCREMENT,
  `langage` ENUM('PHP', 'Python', 'Rust') NOT NULL,
  `date_analyse` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `id_utilisateur` BIGINT COMMENT 'Utilisateur qui a lancé l\'analyse',
  `chemin_fichier` VARCHAR(255) NOT NULL COMMENT 'Chemin du fichier analysé',
  PRIMARY KEY (`id_analyse`),
  KEY `id_utilisateur` (`id_utilisateur`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Table `vulnerabilite`
DROP TABLE IF EXISTS `vulnerabilite`;
CREATE TABLE IF NOT EXISTS `vulnerabilite` (
  `id_vulnerabilite` BIGINT NOT NULL AUTO_INCREMENT,
  `type` ENUM('SQL Injection', 'XSS', 'Path Traversal', 'RCE') NOT NULL,
  `description` TEXT NOT NULL,
  `fichier` VARCHAR(255) NOT NULL COMMENT 'Fichier où la vulnérabilité a été détectée',
  `ligne_code` INT NOT NULL COMMENT 'Ligne de code concernée',
  `id_analyse` BIGINT COMMENT 'Analyse associée',
  PRIMARY KEY (`id_vulnerabilite`),
  KEY `id_analyse` (`id_analyse`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Table `rapport`
DROP TABLE IF EXISTS `rapport`;
CREATE TABLE IF NOT EXISTS `rapport` (
  `id_rapport` BIGINT NOT NULL AUTO_INCREMENT,
  `format` ENUM('PDF', 'JSON', 'XML', 'HTML') NOT NULL,
  `chemin_fichier` VARCHAR(255) NOT NULL COMMENT 'Chemin du fichier de rapport',
  `id_analyse` BIGINT COMMENT 'Analyse associée',
  PRIMARY KEY (`id_rapport`),
  KEY `id_analyse` (`id_analyse`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Table `historique`
DROP TABLE IF EXISTS `historique`;
CREATE TABLE IF NOT EXISTS `historique` (
  `id_historique` BIGINT NOT NULL AUTO_INCREMENT,
  `id_utilisateur` BIGINT COMMENT 'Utilisateur qui a effectué l\'action',
  `action` TEXT NOT NULL COMMENT 'Description de l\'action',
  `date_action` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_historique`),
  KEY `id_utilisateur` (`id_utilisateur`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Contraintes de clés étrangères
ALTER TABLE `analyse_test`
  ADD CONSTRAINT `fk_analyse_utilisateur` FOREIGN KEY (`id_utilisateur`) REFERENCES `utilisateur` (`id_utilisateur`) ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE `vulnerabilite`
  ADD CONSTRAINT `fk_vulnerabilite_analyse` FOREIGN KEY (`id_analyse`) REFERENCES `analyse_test` (`id_analyse`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `rapport`
  ADD CONSTRAINT `fk_rapport_analyse` FOREIGN KEY (`id_analyse`) REFERENCES `analyse_test` (`id_analyse`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `historique`
  ADD CONSTRAINT `fk_historique_utilisateur` FOREIGN KEY (`id_utilisateur`) REFERENCES `utilisateur` (`id_utilisateur`) ON DELETE SET NULL ON UPDATE CASCADE;
