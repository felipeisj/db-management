CREATE DATABASE parking2;

CREATE TABLE user(
  id_user INT AUTO_INCREMENT,
  name VARCHAR(50),
  PRIMARY KEY (id_user),
  FOREIGN KEY fk_estacionamiento2(id_estacionamiento) REFERENCES estacionamiento(id_estacionamiento));

CREATE TABLE estacionamiento(
  id_estacionamiento INT AUTO_INCREMENT,
  name VARCHAR(50),
  direccion VARCHAR(20),
  PRIMARY KEY (id_estacionamiento)),
  FOREIGN KEY fk_tarifa(id_tarifa) REFERENCES tarifa(id_tarifa));

CREATE TABLE tarifa(
  id_tarifa INT AUTO_INCREMENT,
  tipo_tarifa VARCHAR(20),
  costo_tarifa SMALLINT,
  PRIMARY KEY (id_tarifa));
CREATE TABLE utiliza(
  id_utiliza SMALLINT,
  inicio VARCHAR(30),
  termino VARCHAR(30),
  FOREIGN KEY (fk_user(id_user)) REFERENCES user(id_user),
  FOREIGN KEY (fk_estacionamiento(id_estacionamiento)) REFERENCES estacionamiento(id_estacionamiento),
  PRIMARY KEY (id_utiliza));
USE parking2;
INSERT INTO user(id_user, name) VALUES ("1", "Felipe");
INSERT INTO user(id_user, name) VALUES ("2", "Ignacio");
INSERT INTO user(id_user, name) VALUES ("3", "Salazar");

INSERT INTO estacionamiento(id_estacionamiento, name, direccion) VALUES ("1", "yungay", "yungay2701-2790");

INSERT INTO tarifa(id_tarifa, tipo_tarifa, costo_tarifa) VALUES ("1", "minutos","50");
INSERT INTO tarifa(id_tarifa, tipo_tarifa, costo_tarifa) VALUES ("2", "horas","50");
INSERT INTO tarifa(id_tarifa, tipo_tarifa, costo_tarifa) VALUES ("3", "minutos","65");

INSERT INTO utiliza(id_utiliza, inicio, termino) VALUES (1, "20:50", "21:45");

SELECT * FROM tarifa WHERE costo_tarifa=50;
SELECT * FROM user;
