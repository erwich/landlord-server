CREATE TABLE `users` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `email` varchar(255) UNIQUE NOT NULL,
  `password` varchar(255) NOT NULL,
  `first_name` varchar(255),
  `last_name` varchar(255),
  `user_type` int NOT NULL
);

CREATE TABLE `user_types` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `label` varchar(100)
);

CREATE TABLE `properties` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `name` varchar(250),
  `address_1` varchar(255),
  `address_2` varchar(255),
  `city` varchar(250),
  `state` varchar(255),
  `zip` varchar(20),
  `municipality` varchar(255)
);

CREATE TABLE `user_properties` (
  `user_id` int NOT NULL,
  `property_id` int NOT NULL
);

CREATE TABLE `units` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `property_id` int,
  `name` varchar(255),
  `room_count` int
);

CREATE TABLE `users_units` (
  `user_id` int NOT NULL,
  `unit_id` int NOT NULL
);

CREATE TABLE `issues` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `title` varchar(100),
  `description` varchar(255),
  `status` int,
  `unit` int,
  `issue_type` int,
  `submitted` datetime NOT NULL,
  `priority` int
);

CREATE TABLE `issue_statuses` (
  `id` int PRIMARY KEY NOT NULL,
  `label` varchar(50)
);

CREATE TABLE `issue_status_history` (
  `issue_id` int NOT NULL,
  `previous_status` int NOT NULL,
  `new_status` int NOT NULL,
  `date` datetime NOT NULL
);

CREATE TABLE `issue_types` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `label` varchar(100)
);

CREATE TABLE `reports` (
  `user_id` int NOT NULL,
  `report_type` int NOT NULL,
  `reported_key` int NOT NULL,
  `description` varchar(255),
  `severity` int
);

CREATE TABLE `report_types` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `label` varchar(100)
);

CREATE TABLE `ratings` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `rating_user` int NOT NULL,
  `rated_key` int NOT NULL,
  `rating_type` int NOT NULL,
  `rating` int NOT NULL,
  `comment` varchar(255)
);

CREATE TABLE `rating_types` (
  `id` int PRIMARY KEY NOT NULL,
  `label` varchar(100)
);

CREATE TABLE `notifications` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `notification_type` varchar(255) NOT NULL,
  `text` varchar(255)
);

CREATE TABLE `notification_types` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `label` varchar(100)
);

ALTER TABLE `user_types` ADD FOREIGN KEY (`id`) REFERENCES `users` (`user_type`);

ALTER TABLE `user_properties` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `user_properties` ADD FOREIGN KEY (`property_id`) REFERENCES `properties` (`id`);

ALTER TABLE `units` ADD FOREIGN KEY (`property_id`) REFERENCES `properties` (`id`);

ALTER TABLE `users_units` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `users_units` ADD FOREIGN KEY (`unit_id`) REFERENCES `units` (`id`);

ALTER TABLE `issues` ADD FOREIGN KEY (`status`) REFERENCES `issue_statuses` (`id`);

ALTER TABLE `issues` ADD FOREIGN KEY (`unit`) REFERENCES `units` (`id`);

ALTER TABLE `issues` ADD FOREIGN KEY (`issue_type`) REFERENCES `issue_types` (`id`);

ALTER TABLE `issue_status_history` ADD FOREIGN KEY (`issue_id`) REFERENCES `issues` (`id`);

ALTER TABLE `issue_status_history` ADD FOREIGN KEY (`previous_status`) REFERENCES `issue_statuses` (`id`);

ALTER TABLE `issue_status_history` ADD FOREIGN KEY (`new_status`) REFERENCES `issue_statuses` (`id`);

ALTER TABLE `reports` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `reports` ADD FOREIGN KEY (`report_type`) REFERENCES `report_types` (`id`);

ALTER TABLE `ratings` ADD FOREIGN KEY (`rating_user`) REFERENCES `users` (`id`);

ALTER TABLE `ratings` ADD FOREIGN KEY (`rating_type`) REFERENCES `rating_types` (`id`);

ALTER TABLE `notifications` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `notifications` ADD FOREIGN KEY (`notification_type`) REFERENCES `notification_types` (`id`);
