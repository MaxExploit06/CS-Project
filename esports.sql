-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: esports
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `information`
--

DROP TABLE IF EXISTS `information`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `information` (
  `Tag` int NOT NULL,
  `Player_ID` varchar(10) NOT NULL,
  `Role` varchar(10) DEFAULT NULL,
  `Player_Score` int DEFAULT NULL,
  `Player_Name` varchar(20) DEFAULT NULL,
  `Region` varchar(5) DEFAULT NULL,
  `Regional_Rank` int DEFAULT NULL,
  `Password` int DEFAULT NULL,
  PRIMARY KEY (`Tag`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `information`
--

LOCK TABLES `information` WRITE;
/*!40000 ALTER TABLE `information` DISABLE KEYS */;
INSERT INTO `information` VALUES (1052,'Thanos','Sidekick',90,'Marson','SEA',6,1052),(1111,'Faker','Slayer',100,'Jin Woo','KR',1,1111),(3607,'Pain','Survivor',92,'Aamil','JP',3,3607),(5256,'Risen','Riviver',86,'Lance','JP',10,5256),(5562,'Fowl','Marksman',96,'Brian','KR',4,5562),(6982,'Max','Airstriker',96,'Paul','JP',2,6982),(7488,'Fallen','Slayer',99,'Aiden','EU',1,7488),(8008,'Pheonix','Reviver',69,'Rachael','EU',13,8008);
/*!40000 ALTER TABLE `information` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schedule`
--

DROP TABLE IF EXISTS `schedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `schedule` (
  `League` varchar(10) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Participant` varchar(5) DEFAULT NULL,
  `Prize` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schedule`
--

LOCK TABLES `schedule` WRITE;
/*!40000 ALTER TABLE `schedule` DISABLE KEYS */;
INSERT INTO `schedule` VALUES ('Worlds','2023-07-07','team1',2000000),('LCK','2024-03-24','team2',750000),('ZeyPlay','2023-12-01','team2',250000),('DPC NA','2024-01-01','team1',500000),('Scrims','2023-06-13','team1',9000);
/*!40000 ALTER TABLE `schedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `team1`
--

DROP TABLE IF EXISTS `team1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `team1` (
  `Tag` int DEFAULT NULL,
  `Player_ID` varchar(10) NOT NULL,
  `Role` varchar(10) DEFAULT NULL,
  `Player_Score` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `team1`
--

LOCK TABLES `team1` WRITE;
/*!40000 ALTER TABLE `team1` DISABLE KEYS */;
INSERT INTO `team1` VALUES (5562,'Fowl','Marksman',96),(7488,'Fallen','Slayer',99),(6982,'Max','Airstriker',96),(1052,'Thanos','Sidekick',90);
/*!40000 ALTER TABLE `team1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `team2`
--

DROP TABLE IF EXISTS `team2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `team2` (
  `Tag` int DEFAULT NULL,
  `Player_ID` varchar(10) NOT NULL,
  `Role` varchar(10) DEFAULT NULL,
  `Player_Score` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `team2`
--

LOCK TABLES `team2` WRITE;
/*!40000 ALTER TABLE `team2` DISABLE KEYS */;
INSERT INTO `team2` VALUES (3607,'Pain','Survivor',92),(5256,'Risen','Reviver',86),(4711,'Venerable','Marauder',88),(1111,'Faker','Slayer',100);
/*!40000 ALTER TABLE `team2` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-26 10:32:51
