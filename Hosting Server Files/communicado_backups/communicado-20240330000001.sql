-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: db-mysql-nyc3-62851-do-user-15997349-0.c.db.ondigitalocean.com    Database: communicado
-- ------------------------------------------------------
-- Server version	8.0.30

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '889cfd5f-dfdd-11ee-8a8f-36e7f7308032:1-19636';

--
-- Table structure for table `Admin`
--

DROP TABLE IF EXISTS `Admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Admin` (
  `userID` int NOT NULL,
  `officeNo` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`userID`),
  CONSTRAINT `Admin_ibfk_1` FOREIGN KEY (`userID`) REFERENCES `users` (`userID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Admin`
--

LOCK TABLES `Admin` WRITE;
/*!40000 ALTER TABLE `Admin` DISABLE KEYS */;
INSERT INTO `Admin` VALUES (4,'101');
/*!40000 ALTER TABLE `Admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customer`
--

DROP TABLE IF EXISTS `Customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customer` (
  `userID` int NOT NULL,
  `phoneNumber` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`userID`),
  CONSTRAINT `Customer_ibfk_1` FOREIGN KEY (`userID`) REFERENCES `users` (`userID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer`
--

LOCK TABLES `Customer` WRITE;
/*!40000 ALTER TABLE `Customer` DISABLE KEYS */;
INSERT INTO `Customer` VALUES (3,'000-000-0001');
/*!40000 ALTER TABLE `Customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `EventOrganizer`
--

DROP TABLE IF EXISTS `EventOrganizer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `EventOrganizer` (
  `userID` int NOT NULL,
  `phoneNumber` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`userID`),
  CONSTRAINT `EventOrganizer_ibfk_1` FOREIGN KEY (`userID`) REFERENCES `users` (`userID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EventOrganizer`
--

LOCK TABLES `EventOrganizer` WRITE;
/*!40000 ALTER TABLE `EventOrganizer` DISABLE KEYS */;
INSERT INTO `EventOrganizer` VALUES (1,'123-456-7890'),(2,'987-654-3210'),(60,'09310913'),(61,'982'),(62,'2502491012'),(63,'23'),(64,'2502591031'),(65,'2501213');
/*!40000 ALTER TABLE `EventOrganizer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$dsvYWcl1rzCAGBrhhdyltH$wHGvSsWWw1C24MNuUEgLusmEwhpQY83txa/GebeRTWg=','2024-03-15 09:05:08.131505',1,'Comunicado','','','communicado48@gmail.com',1,1,'2024-03-11 23:28:54.483271');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookedEvent`
--

DROP TABLE IF EXISTS `bookedEvent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bookedEvent` (
  `eventID` int NOT NULL,
  `quantity` int DEFAULT NULL,
  `isPaid` tinyint(1) DEFAULT NULL,
  `ID` int DEFAULT NULL,
  `referenceNumber` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`eventID`),
  KEY `ID` (`ID`),
  CONSTRAINT `bookedEvent_ibfk_1` FOREIGN KEY (`eventID`) REFERENCES `events` (`eventID`),
  CONSTRAINT `bookedEvent_ibfk_2` FOREIGN KEY (`ID`) REFERENCES `users` (`userID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookedEvent`
--

LOCK TABLES `bookedEvent` WRITE;
/*!40000 ALTER TABLE `bookedEvent` DISABLE KEYS */;
/*!40000 ALTER TABLE `bookedEvent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2024-03-13 21:08:31.246503','1','events object (1)',2,'[{\"changed\": {\"fields\": [\"Capacity\"]}}]',7,1),(2,'2024-03-14 01:45:06.541366','9','hello',3,'',10,1),(3,'2024-03-14 01:45:55.620572','8','hello',3,'',10,1),(4,'2024-03-14 01:46:16.328180','7','hello',3,'',10,1),(5,'2024-03-14 01:46:16.654500','6','hello',3,'',10,1),(6,'2024-03-14 01:46:16.760847','5','hello',3,'',10,1),(7,'2024-03-28 17:41:06.526144','64','EventOrganizer object (64)',1,'[{\"added\": {}}]',8,1),(8,'2024-03-28 17:42:35.211620','64','EventOrganizer object (64)',1,'[{\"added\": {}}]',8,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(9,'pages','customer'),(8,'pages','eventorganizer'),(7,'pages','events'),(10,'pages','users'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-03-11 22:10:38.912755'),(2,'auth','0001_initial','2024-03-11 22:10:41.162381'),(3,'admin','0001_initial','2024-03-11 22:10:41.760068'),(4,'admin','0002_logentry_remove_auto_add','2024-03-11 22:10:41.903925'),(5,'admin','0003_logentry_add_action_flag_choices','2024-03-11 22:10:42.059242'),(6,'contenttypes','0002_remove_content_type_name','2024-03-11 22:10:42.672678'),(7,'auth','0002_alter_permission_name_max_length','2024-03-11 22:10:42.928807'),(8,'auth','0003_alter_user_email_max_length','2024-03-11 22:10:43.277730'),(9,'auth','0004_alter_user_username_opts','2024-03-11 22:10:43.436580'),(10,'auth','0005_alter_user_last_login_null','2024-03-11 22:10:43.689969'),(11,'auth','0006_require_contenttypes_0002','2024-03-11 22:10:43.830622'),(12,'auth','0007_alter_validators_add_error_messages','2024-03-11 22:10:44.008567'),(13,'auth','0008_alter_user_username_max_length','2024-03-11 22:10:44.304994'),(14,'auth','0009_alter_user_last_name_max_length','2024-03-11 22:10:44.556340'),(15,'auth','0010_alter_group_name_max_length','2024-03-11 22:10:44.856677'),(16,'auth','0011_update_proxy_permissions','2024-03-11 22:10:45.228741'),(17,'auth','0012_alter_user_first_name_max_length','2024-03-11 22:10:45.551993'),(18,'sessions','0001_initial','2024-03-11 22:10:45.944402');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('1tfw2cmopb0wtg2hftkbb9226ph6zrz1','eyJ1c2VyX2lkIjoyNiwidGVzdGNvb2tpZSI6IndvcmtlZCJ9:1rqJnl:Q1d-UZnZSMNdR3w714ipbnIww6p4o4qnzdjfw5hhHQk','2024-04-12 21:30:17.713710'),('8cnkjkxr6w01gbewton639b6qlix6wyb','.eJxVjDsOwjAQBe_iGlm7trG0lPScwdr1BweQLcVJhbg7iZQC2pl5760Cr0sN68hzmJK6KFSnXyYcn7ntIj243buOvS3zJHpP9GGHvvWUX9ej_TuoPOq2tkbEEDuPBAZsESfosikERciDi4nOmBKDtxYM5kgogrhhA0KM6vMFzVw3dA:1rkHgk:Pq_39aUj7DOEj8ZA_IFnYrKflfW2Ji-O2SlPPz2UtD0','2024-03-27 06:02:06.141269'),('8wfultdu1r9azpfx54jpjfxtziaulq5x','.eJxVjsEKgzAQRP8lZwnZJAa2x977DZLNrtVaDJiIh9J_r4KU9jrz5jEv1cW1Dt1aZOlGVhcFqvnNKKZJ5qPgR5zvWac812UkfSD6bIu-ZZbn9WT_BEMsw752lshi9AHQWON68gRebI-mJwzGJ8YWmKMJzhkLkhCIAPbYGsJ4vPp-DG2jqpSacp5G2eVbXiZh9f4AK1RDKA:1rqIHH:BemOLZ2Xx5ctaW3vdc93n8pcfIZk-ptvMDwLdtQo47E','2024-04-12 19:52:39.089925'),('d4h8ow7ny5zhyy9cp0esv262v9fk3lab','eyJ1c2VyX2lkIjoyNiwidGVzdGNvb2tpZSI6IndvcmtlZCJ9:1rqJaz:4GVh6rapQbh_GyQx0JS6EPrYmFrPRL1eWgCudWFtyZs','2024-04-12 21:17:05.355627'),('dm2swh6jhbqswtpybq3uofcyp0s6mf8w','.eJxVjDsOwjAQBe_iGlm7trG0lPScwdr1BweQLcVJhbg7iZQC2pl5760Cr0sN68hzmJK6KFSnXyYcn7ntIj243buOvS3zJHpP9GGHvvWUX9ej_TuoPOq2tkbEEDuPBAZsESfosikERciDi4nOmBKDtxYM5kgogrhhA0KM6vMFzVw3dA:1rkzP1:TO9UXjdv1FArygVixrD0gii5oNMYGxVOT9M3dUH-oEA','2024-03-29 04:42:43.854212'),('fuvvutk1czh4ir4vh2a6xue9chlzdh4e','.eJxVjDsOwjAQBe_iGlm7trG0lPScwdr1BweQLcVJhbg7iZQC2pl5760Cr0sN68hzmJK6KFSnXyYcn7ntIj243buOvS3zJHpP9GGHvvWUX9ej_TuoPOq2tkbEEDuPBAZsESfosikERciDi4nOmBKDtxYM5kgogrhhA0KM6vMFzVw3dA:1rjp7c:En8BiHJfP5g6YS7O4dmYtDfLr2wnGzpHvUkjRQ4c-5M','2024-03-25 23:31:56.472288'),('gwxpej0ia3kvq5gwo4y6npl7mv6ppz8s','.eJxVjDsOwjAQBe_iGlm7trG0lPScwdr1BweQLcVJhbg7iZQC2pl5760Cr0sN68hzmJK6KFSnXyYcn7ntIj243buOvS3zJHpP9GGHvvWUX9ej_TuoPOq2tkbEEDuPBAZsESfosikERciDi4nOmBKDtxYM5kgogrhhA0KM6vMFzVw3dA:1rl3Uy:bvgAggSk3QpVUFGsKcSjdR23kAK5fCtqziJSQyfATTs','2024-03-29 09:05:08.243681'),('hftkopuenzy22nzdy2hwlk47k7suzryz','.eJxVjDsOwjAQBe_iGlm7trG0lPScwdr1BweQLcVJhbg7iZQC2pl5760Cr0sN68hzmJK6KFSnXyYcn7ntIj243buOvS3zJHpP9GGHvvWUX9ej_TuoPOq2tkbEEDuPBAZsESfosikERciDi4nOmBKDtxYM5kgogrhhA0KM6vMFzVw3dA:1rkVos:IavRJ-lEksFNNvEuT145d8DZqIbkdcBOcD_adsjj-S8','2024-03-27 21:07:26.549111'),('ke8hamv0z7hln2ut0heunop98abbd25z','.eJxVjDsOwjAQBe_iGlm7trG0lPScwdr1BweQLcVJhbg7iZQC2pl5760Cr0sN68hzmJK6KFSnXyYcn7ntIj243buOvS3zJHpP9GGHvvWUX9ej_TuoPOq2tkbEEDuPBAZsESfosikERciDi4nOmBKDtxYM5kgogrhhA0KM6vMFzVw3dA:1rkGYC:-GSY5k6He3iaC35xTFyZZheZtkPi_KWOAF1ZpXzZiC4','2024-03-27 04:49:12.799219'),('lleffswatwt6ut5qwn8vshrvx86v4w48','.eJxVjDsOwjAQBe_iGlm7trG0lPScwdr1BweQLcVJhbg7iZQC2pl5760Cr0sN68hzmJK6KFSnXyYcn7ntIj243buOvS3zJHpP9GGHvvWUX9ej_TuoPOq2tkbEEDuPBAZsESfosikERciDi4nOmBKDtxYM5kgogrhhA0KM6vMFzVw3dA:1rktDP:RJWtrWP9Fme95bKE5Z-AEdCAk663P1wOwq9hLM_C6JE','2024-03-28 22:06:19.242471'),('rdi6e4ct1ci7u21id65xa091ryrhqin4','.eJxVjDsOwjAQBe_iGlm7trG0lPScwdr1BweQLcVJhbg7iZQC2pl5760Cr0sN68hzmJK6KFSnXyYcn7ntIj243buOvS3zJHpP9GGHvvWUX9ej_TuoPOq2tkbEEDuPBAZsESfosikERciDi4nOmBKDtxYM5kgogrhhA0KM6vMFzVw3dA:1rktDQ:6YptBXSWCPysWeQFbNkMcVBZ9PgOLqgCd6m0ixiB_2s','2024-03-28 22:06:20.188176'),('v96efafokpg9z3q0sb5pfbx84ya02d8c','eyJ1c2VyX2lkIjoyNiwidGVzdGNvb2tpZSI6IndvcmtlZCJ9:1rqK1N:KNOHGgmStXOLT6CUIhkecAhhejhUiC594EDJG1UpJvw','2024-04-12 21:44:21.227916'),('wu5h44jnu9w2bktcfdhiu842b8ozbnyo','.eJxVjDsOwjAQBe_iGlm7trG0lPScwdr1BweQLcVJhbg7iZQC2pl5760Cr0sN68hzmJK6KFSnXyYcn7ntIj243buOvS3zJHpP9GGHvvWUX9ej_TuoPOq2tkbEEDuPBAZsESfosikERciDi4nOmBKDtxYM5kgogrhhA0KM6vMFzVw3dA:1rkGYD:euTChdIv1tI8Hj_RTOZvxhuex7lyL_K64exmEcbUHbI','2024-03-27 04:49:13.939739');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `events`
--

DROP TABLE IF EXISTS `events`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `events` (
  `eventID` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `eventDateTime` datetime NOT NULL,
  `location` varchar(100) DEFAULT NULL,
  `capacity` int DEFAULT NULL,
  `category` varchar(50) DEFAULT NULL,
  `artist` varchar(100) DEFAULT NULL,
  `isVerified` tinyint(1) DEFAULT NULL,
  `adminID` int DEFAULT NULL,
  `eventOrganizerID` int DEFAULT NULL,
  `imageURL` varchar(100) DEFAULT NULL,
  `price` decimal(6,2) DEFAULT NULL,
  PRIMARY KEY (`eventID`),
  KEY `adminID` (`adminID`),
  KEY `eventOrganizerID` (`eventOrganizerID`),
  CONSTRAINT `events_ibfk_1` FOREIGN KEY (`adminID`) REFERENCES `Admin` (`userID`),
  CONSTRAINT `events_ibfk_2` FOREIGN KEY (`eventOrganizerID`) REFERENCES `EventOrganizer` (`userID`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events`
--

LOCK TABLES `events` WRITE;
/*!40000 ALTER TABLE `events` DISABLE KEYS */;
INSERT INTO `events` VALUES (1,'Music Concert','2024-03-10 18:00:00','Prospera Place',497,'Music','Taylor Swift',1,4,1,'musicconcert.jpg',1088.56),(2,'Art Exhibition','2024-04-15 10:00:00','Kelowna Art Gallery',200,'Art','None',1,4,2,'artexhibition.jpg',25.00),(3,'Food Festival','2024-05-20 12:00:00','Bernard Avenue',300,'Food',NULL,1,4,1,'foodfestival.jpg',31.66),(4,'Technology Conference','2024-06-25 09:00:00','Innovation Center',1000,'Tech',NULL,1,4,2,'technologyconference.jpeg',499.00),(5,'Fashion Show','2024-07-10 15:00:00','Delta Hotel Ballroom',400,'Fashion','Jill Setah',1,4,2,'fashionshow.jpeg',64.95),(11,'Liverpool Trophy Parade','2024-03-31 21:00:00','Downtown Kelowna',78000,'Sports','Jugen Klopp',0,NULL,NULL,'liverpooltrophyparade.jpeg',1490.05),(12,'Hiphop Party','2024-03-29 10:00:00','Distrikt Nightclub',200,'Party','NA',0,NULL,NULL,'hiphopparty.jpeg',68.58),(19,'Updated Event','2024-04-05 10:30:00','Update',90,'Event','',0,NULL,64,'',NULL),(20,'Canada Day Festival','2024-07-01 18:30:00','Waterfront Beach',500,'Festival','NA',0,NULL,65,NULL,NULL),(21,'Tulip Festival','2024-05-04 10:00:00','Abbotsford',200,'Festival','NA',0,NULL,64,NULL,NULL),(22,'UBC Opera Under the Stars','2024-08-10 19:30:00','UBC Okanagan Courtyard',300,'Music','Beethoven',0,NULL,65,'',NULL),(23,'New event test','2024-04-01 04:04:00','100 street',9,'9','9',0,NULL,64,'',NULL),(24,'test','2024-04-04 04:04:00','9',9,'9','9',0,NULL,65,'',NULL),(25,'test','2024-04-04 04:04:00','5',55,'5','5',0,NULL,65,'',NULL),(26,'ggG','2024-04-04 04:04:00','r',9,'9','9',0,NULL,65,'',NULL);
/*!40000 ALTER TABLE `events` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `userID` int NOT NULL AUTO_INCREMENT,
  `role` varchar(50) DEFAULT NULL,
  `username` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `address` varchar(200) NOT NULL,
  `password` varchar(100) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`userID`)
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Event Organizer','john_doe','john@example.com','123 Main St, Anytown','password123','John Doe'),(2,'Event Organizer','jane_smith','jane@example.com','456 Elm St, Otherville','password456','Jane Smith'),(3,'Customer','bob_jones','bob@example.com','789 Oak St, Anothercity','password789','Bob Jones'),(4,'Admin','admin1','admin1@example.com','Admin Office, City Center','adminpass','Gurpreet Singh Chadda'),(24,'customer','prathamshah','prathamkshah130503@gmail.com','775 Academy Way','pbkdf2_sha256$600000$hauM4exQlEyaQ8dKr6wsjF$slTYpEdkA9kDtw9yzAzKsJ45tOre817ryOlmi0uu5Ko=','Pratham Shah'),(25,'organiser','ojussharma','ojussharma@gmail.com','775 Academy Way','pbkdf2_sha256$600000$SNoyTzHDj8ri9FnQkjfKsx$HB3wMO8wZbYDTf1zVQY7CwAIsQrvuUwFs7K1H1Qmiqs=','Ojus Sharma'),(26,'customer','mahigangal','gangalmahi@gmail.com','840 academy way','pbkdf2_sha256$600000$Cy6JqTSiH0ciYsm97f61Mm$Or7ye6eysklfFi5fujCGCABTOsxvlcrvNA66oVaimYQ=','Mahi Gangal'),(27,'organiser','sparshkhanna','sparshkhanna@gmail.com','775 Academy Way','pbkdf2_sha256$600000$Kh9x2mz7jiebmwZWtpYpHW$l/GKQE9pLag01Ay4QOdAiw1tsZPfudUeWWTJccDN1n0=','Sparsh Khanna'),(28,'customer','mithishravisankargeetha','mithishravisankargeetha@gmail.com','802 Academy Way','pbkdf2_sha256$600000$HuITIiQggo20aXUoU8IpXi$SqEfRppsAVj0JjmQlNiaBlz0pq8UFmbMylfuZ0VDU0M=','Mithish Ravisankar Geetha'),(29,'customer','rossgeller','rossgeller@gmail.com','75 shanti vihar','pbkdf2_sha256$600000$030iKRV6Km1wOFWk8570h5$wlEl7J7JNnDmY/nYX7UZNlGf2yLu+zAo2INI6kHh7dg=','Ross Geller'),(30,'customer','joeytribbiani','joeytribbiani@gmail.com','545 Grove Street, New York','pbkdf2_sha256$600000$QVLzXfvBqF5o3j12GFjAUv$ewgZTbmTPIH7Pyz54R4spfBMQYyOJDYSQOOQlggKp9M=','Joey Tribbiani'),(32,'organiser','Org1','org1@gmail.com','Kelowna','pbkdf2_sha256$600000$RIZydIkEok9hIIiNABD2OF$UhvunINbT+0Ki6RZ2Wg5gDqq0pl4qUa1E4nee+7g5F8=','Organizer 1'),(33,'customer','Mithish','mithish@gmail.com','Kelowna','pbkdf2_sha256$600000$RU0PkaFUFcTS8yIjzKaP3B$9Q7BW1QOWr2N09018ayqcOWF6QLylfRMwtRjY94XeJU=','Mithish'),(34,'EventOrganizer','Org2','org@gmail.com','Kelowna','pbkdf2_sha256$600000$Th12mlaZ9r4djWFMkINiU8$n7XAo90UYlELN0BzCl8fDf8pGGXOrhgGKWBV+Bh25P4=','Org2'),(35,'Event Organizer','Event org 3','org@org.com','Vancouver','pbkdf2_sha256$600000$M78g9L1UQzJd3qiU0gGJKb$W0uzfGvoAqqYVfytlTHMkzNYxWln6jIE3Nsp+F6QSsQ=','Org3'),(40,'Event Organizer','Event org 3','org@org.com','Vancouver','pbkdf2_sha256$600000$U0O4ho5R232cSw4NLMRq84$SDkZs/7UkPC6eVq8is+M69vA1gKdrsmcOqLLZzprv/E=','Org3'),(41,'Event Organizer','EventOrg9','org@org.com','Dubai','pbkdf2_sha256$600000$F7gfSIUM6AqsPlmXhXcOZw$jpMvYFT/ia0H9rxKYQn0Cb/Qmq+whdS6JiEwLKvstbQ=','Org 9'),(42,'Event Organizer','EventOrg9','org@org.com','Dubai','pbkdf2_sha256$600000$0GiS7ymM0ApfF86gTL1cY1$hPtdB4aYOIBGeGJEcFo3jfHvpKCGbFkAPojZ/lQWbQE=','Org 9'),(43,'Event Organizer','EventOrg9','org@org.com','Dubai','pbkdf2_sha256$600000$5Fk5vANKRgMpH7T6rWtx21$Hv8bjO+sfIyGFA1sbAhm2XWIYz8DhY1s7cqj0AvNtqo=','Org 9'),(44,'Event Organizer','event org 3','sa@gmail.com','sandllaksdjlj','pbkdf2_sha256$600000$s00nDFApI6oKfUbkvSe7ar$JdpITAI0n2o6U/NOKKTbUgFKaYzFHIvatC/bEBd6Tu0=','org 3'),(45,'EventOrganizer','eventorg344025988','asf@ga.com','sdkj','pbkdf2_sha256$600000$Lq2rrsopWXPdTRQiPoEP7D$Xem9LkDyNbvP0iZk4Fk0+IwEAC3wJynyOmcFfn5mhBk=','org124'),(46,'EventOrganizer','eventorg344025988','asf@ga.com','sdkj','pbkdf2_sha256$600000$mu5Eq5sFclQQeL3z2MKyjs$81fOeodEZZqhR0AG/MEiE1D2D2PmGiVCjW6ylW5Q7E4=','org124'),(47,'EventOrganizer','org0000000','0002!@fmail.com','kl','pbkdf2_sha256$600000$aHYfCpGJhzLnjpaXjpbv54$m3ULL7EfDvdu5WASOBclDwr2J3cJl3TPs+mEXDURorg=','00'),(48,'EventOrganizer','blah','blah@blah.com','blah','pbkdf2_sha256$600000$BI6lmySIcaUQzNcI5jSJt1$97N0GbcQP8xbGFEjBA8Mbj15FrMZhFAEG2okKGuTnu0=','blah'),(49,'EventOrganizer','test','t@gmal.com','sd','pbkdf2_sha256$600000$ULsipnCoRebD60sfHJKSRS$iUYVqB90Gnq4bbQZlEQ8JiDIIRNTFvCchm0NqZOETNg=','ttjk'),(50,'EventOrganizer','org10000000','orgggg@g.com','skdfj','pbkdf2_sha256$600000$1s5h9sNWP6Sje3CXeyA1qj$2RlHqPHUV84dHwFuqcvQvd6RiDpnkSzFwHbzlqLdF88=','org1000000'),(51,'EventOrganizer','sadkfhasfkh','kjhdfs@gakjf.com','sajkdfakjsfd','pbkdf2_sha256$600000$3WtqQNu6TORM5CEElKKoS0$VxC1kdvdcGIvMTaNvQ9YNF+cKydCWSoXaScwE2haK/Y=','jlhksdlhfskldfhkjl'),(52,'EventOrganizer','sadkfhasfkh','kjhdfs@gakjf.com','sajkdfakjsfd','pbkdf2_sha256$600000$yfbFGv1fJLpM6VmyyqptlN$iHHUXWP3pKPVYwIfHCZCowCKcnmqugNFDHirGbLG7Jk=','jlhksdlhfskldfhkjl'),(53,'EventOrganizer','asddafs','skladahslfdh@gmail.com','skdasfdkj','pbkdf2_sha256$600000$QcaMDVRR2zNWAR0ADTcVdP$mnrGCMTCEm0K9LzArT6sNQ0MoLPQCEgPSaXneuUT5Fg=','sdlkfhskldfh'),(54,'EventOrganizer','kjsdakhas','ksdjfhkjsf@gha.com','lksadfjlkafj','pbkdf2_sha256$600000$QK4QjZGaNOzCfdBFzzRIxq$fjNDGFKm0IPRwFd/777GgQmJKcHX9tIbVGFINTuS1eE=','kjsdhfkjsdfhjkh'),(55,'EventOrganizer','kjdsfhakjsdfh','dkjshf@gahksj.com','askjdfasjfk','pbkdf2_sha256$600000$Nwjy5pivPKm4tfup6dDor0$HkU8cE6m8z49noF3SuQHcAy1OW8P0KKQaTVEGjGnjHE=','kjdshfkajsdfhkj'),(56,'EventOrganizer','jfhksjdhkj','klhsdfkhsf@gmail.com','ksdhfaksfhkjh','pbkdf2_sha256$600000$CglyE2KDxW2GvFkWXpwea0$DPpSXpq1yZviCUCJYVdLZVToqgV+gOoUReZUGp/P6BM=','kjsdhlakshflk'),(57,'EventOrganizer','adkasdhkhdskjahkjads','kssdkfh@gmail.com','asdkfhkashjfkjh','pbkdf2_sha256$600000$dJnOhRSQEhrN0qNU6nzwEK$aYyZLClW8gMw9vkXXUsbtxpMKp/qOiYyTs/bsrJ69Ok=','kadhslkashkalhfakdlsjh'),(58,'EventOrganizer','sdkhjsdfkjh','sdkjhsakjfh2gahsk@gmail.com','kjasdfhksjlh','pbkdf2_sha256$600000$uPt0m9YSxxV2uiuxqF8u8l$D4iFlxEhtpr1DA3QFZs6mCnrmPZ/fcUkRq5Y/mknsCQ=','kdsfksjfdhkjh'),(59,'EventOrganizer','sdilhasli','sdlkahfsakjhldf@gmail.com','aksdjakjlshdf','pbkdf2_sha256$600000$frQMsuy4mdr8cEybcHGLa8$3mcpp5mEzxkK3p7aF+CylowpiNJyH/HUo5Xx/v+gFYA=','klsjadhfklsajfhklh'),(60,'EventOrganizer','sdilhasli','sdlkahfsakjhldf@gmail.com','aksdjakjlshdf','pbkdf2_sha256$600000$I5heMJlGlpf3FLvcetQQkD$QI8UltZZEh37nBgebdiOs6Q2lM/BP1y6blo8pqfyz8k=','klsjadhfklsajfhklh'),(61,'EventOrganizer','hhhh','hhh@hhh.com','hhhh','pbkdf2_sha256$600000$QF0G2CyWqaNuN1Kuy1nBLe$WYvoqmeF+u4ja4+Opyddoplm4oTjwM+aHh8Gqf3GsBs=','hhhh'),(62,'EventOrganizer','Organizer4','org@gmail.com','Burnaby','pbkdf2_sha256$600000$W5nKp6MvEyMnwuOhHKviMy$s6k5+N963SqKQddqQGulpQy7fAWF6KXxQDvat+GAfD8=','Organizer 4'),(63,'EventOrganizer','Evento3','vent@gmia.com','ev','pbkdf2_sha256$600000$sunNiQyXGubaQS3YN1FuhE$f6/zS/X70wpc+sGCk25VLiwG4FFRtXjUna4b+3omYYI=','evento3'),(64,'EventOrganizer','mithsEventOrg','miths17@org.com','Kelowna ','pbkdf2_sha256$600000$oAwK9JBsY7nuHk34Juk8Fr$OtSSTJcCG1WgPG8UHSJ4jIJs7hutxECE+oZF5onqToc=','Mithish-EventOrganizer '),(65,'EventOrganizer','TestOrganizer','test@hello.com','test','pbkdf2_sha256$600000$8ar1SFnNEbxaWzx5tHReIb$mzUkY4ZQRTn5zZ/ZGULmFMa0t6lP40CAnjYz77ZxSuU=','TestOrganizer');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-30  0:00:25
