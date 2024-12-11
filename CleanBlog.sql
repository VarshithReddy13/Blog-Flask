-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 11, 2024 at 05:58 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `CleanBlog`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(11) NOT NULL,
  `Name` text NOT NULL,
  `phone_no` varchar(15) NOT NULL,
  `msg` text NOT NULL,
  `date` datetime NOT NULL,
  `email` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `Name`, `phone_no`, `msg`, `date`, `email`) VALUES
(1, 'varshith', '1234567890', 'jhbvbj', '2024-11-16 13:25:52', 'myemail@gmail.com'),
(2, 'hi', '8263728362', 'hjbhebfbhbdk', '2024-11-16 18:04:07', 'kjefbhj@gmail.com'),
(3, 'ee', '1231231234', 'allu bhaai', '2024-11-16 18:05:49', 'allu@gmail.com'),
(4, 'hi', '83783748', 'jfjhfbjhb', '2024-11-16 18:24:25', 'bfjbfjer'),
(5, '389378497', '28928893', '283728372837', '2024-11-16 18:24:44', '2389387'),
(6, 'madhu', '9191827364', 'majdb', '2024-11-16 21:45:03', 'mau@gmail.com'),
(7, 'Varshith Reddy', '09000622300', 'hello', '2024-11-17 15:55:21', 'Varshithreddi5@gmail.com'),
(8, 'Varshith Reddy', '09000622300', 'hello', '2024-11-17 15:59:57', 'Varshithreddi5@gmail.com'),
(9, 'Varshith Reddy', '09000622300', 'hello', '2024-11-17 16:00:06', 'Varshithreddi5@gmail.com'),
(10, 'Varshith Reddy', '09000622300', 'jbfnknefjkenfjn', '2024-11-20 16:12:22', 'Varshithreddi5@gmail.com'),
(11, 'Varshith Reddy', '09000622300', 'jbfnknefjkenfjn', '2024-11-20 16:19:12', 'Varshithreddi5@gmail.com'),
(12, 'Varshith Reddy', '09000622300', 'jbfnknefjkenfjn', '2024-11-20 16:19:20', 'Varshithreddi5@gmail.com'),
(13, 'Varshith Reddy', '09000622300', 'jbfnknefjkenfjn', '2024-11-20 16:19:59', 'Varshithreddi5@gmail.com'),
(14, 'Varshith Reddy', '09000622300', 'varsh\r\n', '2024-11-20 16:20:11', 'Varshithreddi5@gmail.com'),
(15, 'Varshith Reddy', '09000622300', 'varsh\r\n', '2024-11-20 16:22:57', 'Varshithreddi5@gmail.com'),
(16, 'Varshith Reddy', '09000622300', 'uhiwbeifbiwebfbh', '2024-11-20 16:23:08', 'Varshithreddi5@gmail.com'),
(17, 'Varshith Reddy', '09000622300', 'uhiwbeifbiwebfbh', '2024-11-20 16:25:20', 'Varshithreddi5@gmail.com'),
(18, 'Varshith Reddy', '09000622300', 'xred hello', '2024-11-20 16:25:35', 'Varshithreddi5@gmail.com'),
(19, 'Varshith Reddy', '09000622300', 'hello\r\n', '2024-11-23 15:22:39', 'Varshithreddi5@gmail.com'),
(20, 'hi', '1234', 'a-z', '2024-12-08 22:03:17', 'hello@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `title` text NOT NULL,
  `tag_line` text NOT NULL,
  `slug` varchar(25) NOT NULL,
  `content` text NOT NULL,
  `img_url` varchar(150) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `tag_line`, `slug`, `content`, `img_url`, `date`) VALUES
(1, 'First post', 'first-post', 'first-post', 'hi hello', 'first-post.jpg', '2024-12-10 17:38:33'),
(2, 'Natwar Singh writes on champion of the downtrodden Dr BR Ambedkar', 'champion-br-ambedkar', 'champion-br-ambedkar', 'He,for the first thirty five years of his life was subjected to the most appalling humiliations, brutal discrimination and indignities for being an untouchable. The dice was loaded against him right from his birth.\r\n\r\nHe was born in a Mahar family on 14 April 1893. He died at the age of fifty six on 6th December 1956. He made it to the Elphiston College in Bombay. He could neither buy books nor clothes. He was lent books by one of his professors who also gave him clothes.\r\nAt the age of 22, he was given scholarship by the enlightened Gaikward of Baroda, which enable him to join Columbia University in New York. He passed his M.A and obtained a PhD with high distinction. Similarly he did exceptionally at the London School of Economics. THE LOT of the untouchables in India were worse then that of Negros (Blacks) in America.\r\n\r\n\r\nThis was a blot on Hinduism which outraged Gandhiji. He called them Harijans, now referred to as Dalits. Ambedkar considered Gandhi\'s approach to the problem of untouchability and untouchables both flawed and wooly. The two clashed at the second Round Table Conference in 1931. Ambedkar denigrated Gandhi in sharp language. \"Unfortunately, the Congress chose Mr. Gandhi as its representative.', 'br-ambedkar.jpg', '2024-12-09 08:14:47');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
