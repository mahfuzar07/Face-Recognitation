-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 23, 2020 at 03:04 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.4.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `employee`
--

-- --------------------------------------------------------

--
-- Table structure for table `emp_table`
--

CREATE TABLE `emp_table` (
  `Designation` varchar(100) NOT NULL,
  `Id` int(10) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Gender` varchar(100) NOT NULL,
  `Contact_No` varchar(100) NOT NULL,
  `DOB` varchar(100) NOT NULL,
  `DOJ` varchar(100) NOT NULL,
  `NID_No` int(50) NOT NULL,
  `Address` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `emp_table`
--

INSERT INTO `emp_table` (`Designation`, `Id`, `Name`, `Email`, `Gender`, `Contact_No`, `DOB`, `DOJ`, `NID_No`, `Address`) VALUES
('', 0, '', '', '', '', '', '', 0, '\n'),
('CEO', 101, 'Md. Mahfuzar Rahman', 'mahfuzarcse@gmail.com', 'Male', '1773841134', '27/1/1997', '20/1/2022', 2147483647, 'Bogura\n\n\n\n'),
('CEO', 102, 'Md. Mahfuzar Rahman', 'mahfuzarcse@gmail.com', 'Male', '1773841134', '27/1/1997', '20/1/2022', 2147483647, 'Bogura\n\n\n\n\n');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `emp_table`
--
ALTER TABLE `emp_table`
  ADD PRIMARY KEY (`Id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
