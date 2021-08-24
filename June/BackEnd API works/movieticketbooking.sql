-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 25, 2021 at 01:07 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `movieticketbooking`
--

-- --------------------------------------------------------

--
-- Table structure for table `ownerdetail`
--

CREATE TABLE `ownerdetail` (
  `id` int(11) NOT NULL,
  `ownerName` varchar(30) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ownerdetail`
--

INSERT INTO `ownerdetail` (`id`, `ownerName`, `email`, `password`) VALUES
(1, 'kausic', 'kausic.m@eunimart.com', 'kausic'),
(2, 'balu', 'balu@gmail.com', 'balu'),
(3, 'mathan', 'mathan@gmail.com', 'mathan'),
(4, 'manickam', 'manickam@gmail.com', 'manickam');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`name`, `email`, `password`) VALUES
('kausic', 'kausicm30@gmail.com', 'kausic'),
('balu', 'balu@gmail.com', 'kausic'),
('jai', 'jai@gmail.com', 'kausic'),
('mathan', 'mathan@gmail.com', 'kausic'),
('akshai', 'akshai@gmail.com', 'kausic'),
('manickam', 'manickam@gmail.com', 'kausic'),
(NULL, NULL, NULL),
('govardhanan', 'gova@gmail.com', 'gova'),
(NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `seatbooking`
--

CREATE TABLE `seatbooking` (
  `email` varchar(50) DEFAULT NULL,
  `moviename` varchar(50) DEFAULT NULL,
  `movietime` varchar(50) DEFAULT NULL,
  `nooftickets` varchar(50) DEFAULT NULL,
  `seatnumbers` varchar(50) DEFAULT NULL,
  `totalamount` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `seatbooking`
--

INSERT INTO `seatbooking` (`email`, `moviename`, `movietime`, `nooftickets`, `seatnumbers`, `totalamount`) VALUES
('kausicm30@gmail.com', 'Master', '2.00pm', '3', '29,30,31', '450'),
('balu@gmail.com', 'Master', '2.00pm', '2', '15,16', '300'),
('mathan@gmail.com', 'Drishyam 2', '8.00pm', '4', '17,18,23,24', '600'),
('kausicm30@gmail.com', 'WAR', '8.00am', '4', '3,4,5,6', '600'),
('balu@gmail.com', 'KGF', '5.00pm', '4', '13,18,27,39', '600'),
('balu@gmail.com', 'GodzillavsKong', '11.00am', '4', '11,12,21,22', '600'),
('kausicm30@gmail.com', 'Master', '2.00pm', '3', '3,4,5', '450'),
('kausicm30@gmail.com', 'KGF', '5.00pm', '4', '7,8,15,16', '600'),
('kausicm30@gmail.com', 'KGF', '5.00pm', '2', '23,24', '300'),
('kausicm30@gmail.com', 'WAR', '8.00am', '4', '21,22,29,30', '600'),
('jai@gmail.com', 'KGF', '5.00pm', '3', '4,5,6', '450'),
('kausicm30@gmail.com', 'GodzillavsKong', '11.00am', '3', '3,4,5', '450'),
('balu@gmail.com', 'GodzillavsKong', '11.00am', '2', '6,14', '300'),
('balu@gmail.com', 'Master', '2.00pm', '4', '1,2,10,11', '600');

-- --------------------------------------------------------

--
-- Table structure for table `theatredetail`
--

CREATE TABLE `theatredetail` (
  `id` int(11) NOT NULL,
  `ownerdetail_id` int(11) DEFAULT NULL,
  `moviename` varchar(20) DEFAULT NULL,
  `time` varchar(10) DEFAULT NULL,
  `theatrename` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `theatredetail`
--

INSERT INTO `theatredetail` (`id`, `ownerdetail_id`, `moviename`, `time`, `theatrename`) VALUES
(1, 1, 'KGF2', '2.00PM', 'Pheonix Theatre'),
(2, 2, 'Master', '2.00PM', 'NKP Theatre'),
(3, 3, 'Godzill vs Kong', '2.00PM', 'Vijayan Theatre'),
(12, 2, 'KGF2', '5.00pm', 'NKP Theatre'),
(13, 2, 'F9', '9.00am', 'NKP Theatre'),
(14, 1, 'F9', '9.00am', 'Pheonix Theatre'),
(15, 1, 'Master', '5.00pm', 'Pheonix Theatre'),
(16, 3, 'F9', '9.00am', 'Vijiyan Theatre');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `ownerdetail`
--
ALTER TABLE `ownerdetail`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `theatredetail`
--
ALTER TABLE `theatredetail`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `ownerdetail`
--
ALTER TABLE `ownerdetail`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `theatredetail`
--
ALTER TABLE `theatredetail`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
