CREATE TABLE `NewTable` (
  `Nome` varchar(100) COLLATE utf8_general_mysql500_ci NOT NULL,
  `data` varchar(100) COLLATE utf8_general_mysql500_ci NOT NULL,
  `Prioridade` int(10) NOT NULL,
  `Concluida` tinyint(1) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_mysql500_ci