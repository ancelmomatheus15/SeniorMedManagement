Abrir o banco
-> sudo mysql –u username –p

user: root
senha: 102030
db: zenboIntegrationDB

#banco de dados
CREATE DATABASE zenboIntegrationDB;
USE zenboIntegrationDB;

#tabelas
CREATE TABLE medic (
id INT(6) ZEROFILL UNSIGNED AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(50) NOT NULL,
specialty VARCHAR(50) NOT NULL,
addressStreet VARCHAR(50) NOT NULL,
addressNumber VARCHAR(50) NOT NULL,
addressZip VARCHAR(50) NOT NULL
);

CREATE TABLE hospital (
id INT(6) ZEROFILL UNSIGNED AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(50) NOT NULL,
addressStreet VARCHAR(50) NOT NULL,
addressNumber VARCHAR(50) NOT NULL,
addressZip VARCHAR(50) NOT NULL
);

CREATE TABLE medication (
id INT(6) ZEROFILL UNSIGNED AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(50) NOT NULL,
dosage VARCHAR(50) NOT NULL,
frequency VARCHAR(50) NOT NULL,
description VARCHAR(500) NOT NULL
);

CREATE TABLE user (
id INT(6) ZEROFILL UNSIGNED AUTO_INCREMENT PRIMARY KEY,
userName VARCHAR(100) NOT NULL,
birthDate Date NOT NULL,
city VARCHAR(50) NOT NULL,
country VARCHAR(3) NOT NULL,
gender VARCHAR(1) NOT NULL,
phone VARCHAR(50) NOT NULL,
mail VARCHAR(50) NOT NULL
);

CREATE TABLE appointment (
id INT(6) ZEROFILL UNSIGNED AUTO_INCREMENT PRIMARY KEY,
user INT(6) ZEROFILL UNSIGNED REFERENCES user(id),
hora int NOT NULL,
data DATE NOT NULL,
hospital INT(6) ZEROFILL UNSIGNED REFERENCES hospital(id),
medic INT(6) ZEROFILL UNSIGNED REFERENCES medic(id),
descricao VARCHAR(50) NOT NULL,
);

CREATE TABLE treatment (
id INT(6) ZEROFILL UNSIGNED AUTO_INCREMENT PRIMARY KEY,
user INT(6) ZEROFILL UNSIGNED REFERENCES user(id),
medication INT(6) ZEROFILL UNSIGNED REFERENCES medication(id),
data_inicio DATE NOT NULL,
data_fim DATE NOT NULL,
last_occurrence DATE NOT NULL,
medic INT(6) ZEROFILL UNSIGNED REFERENCES medic(id),
descricao VARCHAR(50) NOT NULL,
monitorado varchar(1),
atendido varchar(50) 
);


