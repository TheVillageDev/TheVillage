CREATE TABLE IF NOT EXISTS `the_village`.`user` (
	`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	`username` VARCHAR(255) NOT NULL,
	`fortschritts_lvl` DOUBLE,
	`invite_link` VARCHAR(255),
	`atk_link` VARCHAR(255),
	`arbeiter_gesamt` INT,
	`truppen_gesamt` INT,
	`last_message_timestamp` TIMESTAMP,
	`inactive` BOOLEAN,
	`rand_key` VARCHAR(255),
	`id_clan_membership` INT,
	`id_hierarchy_lvl` INT NOT NULL
);

CREATE TABLE IF NOT EXISTS `the_village`.`building` (
	`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	`arbeiter` INT,
	`ende_arbeit` TIMESTAMP,
	`level` DOUBLE,
	`id_user` INT NOT NULL,
	`id_building_type` INT NOT NULL
);

CREATE TABLE IF NOT EXISTS `the_village`.`building_type` (
	`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	`id_zeitalter` INT
);

CREATE TABLE IF NOT EXISTS `the_village`.`building_type_name` (
	`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	`name` VARCHAR(255) NOT NULL,
	`description` VARCHAR(255),
	`max_arbeiter` INT,
	`id_building_type` INT NOT NULL,
	`id_zeitalter` INT
);

CREATE TABLE IF NOT EXISTS `the_village`.`zeitalter` (
	`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	`min_fortschritts_lvl` DOUBLE
);

CREATE TABLE IF NOT EXISTS `the_village`.`produktion` (
	`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	`id_item_type` INT NOT NULL,
	`id_building_type` INT NOT NULL
);

CREATE TABLE IF NOT EXISTS `the_village`.`item_type` (
	`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	`name` VARCHAR(255) NOT NULL,
	`id_zeitalter_availability_von` INT,
	`id_zeitalter_availability_bis` INT
);

CREATE TABLE IF NOT EXISTS `the_village`.`resource_production` (
	`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	`id_resource` INT NOT NULL,
	`id_building_type` INT NOT NULL
);

CREATE TABLE IF NOT EXISTS `the_village`.`building_type_rechnung` (
	`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	`id_rechnung` INT NOT NULL,
	`id_building_type` INT NOT NULL
);

CREATE TABLE IF NOT EXISTS `the_village`.`rechnung` (
	`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL
);

CREATE TABLE IF NOT EXISTS `the_village`.`zeitalter_building_type_requirement` (
	`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	`min_level` DOUBLE,
	`id_building_type` INT NOT NULL,
	`id_zeitalter` INT NOT NULL
);

CREATE TABLE IF NOT EXISTS `the_village`.`resource_stack` (
	`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	`amount_resource` INT NOT NULL,
	`id_resource` INT NOT NULL,
	`id_user` INT,
	`id_rechnung` INT
);

CREATE TABLE IF NOT EXISTS `the_village`.`resource` (
	`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	`name` VARCHAR(255) NOT NULL,
	`id_zeitalter_availability_von` INT,
	`id_zeitalter_availability_bis` INT
);

CREATE TABLE IF NOT EXISTS `the_village`.`item_stack` (
	`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	`amount_item` INT NOT NULL,
	`id_user` INT NOT NULL,
	`id_item_type` INT NOT NULL
);

CREATE TABLE IF NOT EXISTS `the_village`.`kampf` (
	`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	`angreifer_truppen` INT NOT NULL,
	`verteidiger_truppen` INT,
	`gewonnen` BOOLEAN,
	`timestamp` TIMESTAMP NOT NULL,
	`id_user_angreifer` INT NOT NULL,
	`id_user_verteidiger` INT NOT NULL
);

CREATE TABLE IF NOT EXISTS `the_village`.`friendlist` (
	`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	`name` VARCHAR(255) NOT NULL,
	`description` VARCHAR(255),
	`id_user` INT NOT NULL
);

CREATE TABLE IF NOT EXISTS `the_village`.`friendlist_user` (
	`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	`id_user` INT NOT NULL,
	`id_friendlist` INT NOT NULL
);

CREATE TABLE IF NOT EXISTS `the_village`.`user_role` (
	`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	`id_permission` INT NOT NULL,
	`id_user` INT NOT NULL,
	`id_hierarchy_lvl_availability_bis` INT
);

CREATE TABLE IF NOT EXISTS `the_village`.`hierarchy_lvl` (
	`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	`name` VARCHAR(255) NOT NULL,
	`description` VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS `the_village`.`hierarchy_role` (
	`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	`id_permission` INT NOT NULL,
	`id_hierarchy_lvl_availability_von` INT NOT NULL,
	`id_hierarchy_lvl_availability_bis` INT
);

CREATE TABLE IF NOT EXISTS `the_village`.`permission` (
	`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	`name` VARCHAR(255) NOT NULL,
	`description` VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS `the_village`.`clan_membership` (
	`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	`id_clan_authority_lvl` INT NOT NULL,
	`id_clan` INT NOT NULL
);

CREATE TABLE IF NOT EXISTS `the_village`.`clan` (
	`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	`name` VARCHAR(255) NOT NULL,
	`description` VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS `the_village`.`clan_freund` (
	`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	`id_clan_1` INT NOT NULL,
	`id_clan_2` INT NOT NULL
);

CREATE TABLE IF NOT EXISTS `the_village`.`clan_feind` (
	`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	`id_clan_1` INT NOT NULL,
	`id_clan_2` INT NOT NULL
);

CREATE TABLE IF NOT EXISTS `the_village`.`clan_authority_lvl` (
	`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	`name` VARCHAR(255) NOT NULL,
	`description` VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS `the_village`.`clan_role` (
	`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	`id_clan_authority_lvl_availability_von` INT NOT NULL,
	`id_clan_authority_lvl_availability_bis` INT,
	`id_clan_permission` INT NOT NULL
);

CREATE TABLE IF NOT EXISTS `the_village`.`clan_permission` (
	`id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	`name` VARCHAR(255) NOT NULL,
	`description` VARCHAR(255)
);


