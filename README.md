## Task one
### Get started
    $ bash env-prepare.sh
    $ docker network create bus
    $ docker compose build
    $ docker compose up


## Task two
### DB is 10.6.12-MariaDB-0ubuntu0.22.04.1

#### SQL for create tables
```
CREATE TABLE IF NOT EXISTS `short_names` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `status` int(11),
  PRIMARY KEY (`id`),
  KEY `name_ind` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `full_names` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `status` int(11),
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_uniq` (`name`),
  KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
```

#### SQL version one
```
UPDATE full_names
JOIN short_names ON full_names.name LIKE CONCAT(short_names.name, '.%')
AND SUBSTRING(full_names.name, LENGTH(short_names.name) + 2) NOT LIKE '%.%'
SET full_names.status = short_names.status;
```

#### SQL version two
```
CREATE INDEX short_names_index ON short_names (name);
CREATE INDEX full_names_index ON full_names (name);
UPDATE full_names
JOIN short_names ON full_names.name LIKE CONCAT(short_names.name, '.%')
AND SUBSTRING(full_names.name, LENGTH(short_names.name) + 2) NOT LIKE '%.%'
SET full_names.status = short_names.status;
```
