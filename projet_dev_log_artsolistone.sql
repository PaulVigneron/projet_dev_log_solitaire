-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : mar. 22 mars 2022 à 12:34
-- Version du serveur : 10.4.22-MariaDB
-- Version de PHP : 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `projet_dev_log_artsolistone`
--

-- --------------------------------------------------------

--
-- Structure de la table `skins`
--

CREATE TABLE `skins` (
  `id_skins` int(11) NOT NULL,
  `photo_skins` varchar(50) NOT NULL,
  `name_skins` varchar(256) NOT NULL,
  `value_skins` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `photo_profil` varchar(50) NOT NULL,
  `name` varchar(256) NOT NULL,
  `email` varchar(256) NOT NULL,
  `nb_win` int(11) NOT NULL,
  `nb_equality` int(11) NOT NULL,
  `nb_lose` int(11) NOT NULL,
  `nb_xp` int(11) NOT NULL,
  `nb_pieces` int(11) NOT NULL,
  `nb_skins` int(11) NOT NULL,
  `ratio` int(11) NOT NULL,
  `special_lock` int(11) NOT NULL,
  `special_pioche` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `users_skins`
--

CREATE TABLE `users_skins` (
  `id_users` int(11) NOT NULL,
  `id_skins` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `skins`
--
ALTER TABLE `skins`
  ADD PRIMARY KEY (`id_skins`);

--
-- Index pour la table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `skins`
--
ALTER TABLE `skins`
  MODIFY `id_skins` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
