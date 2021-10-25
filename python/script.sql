CREATE SCHEMA renewableenergy DEFAULT CHARACTER SET utf8mb4 DEFAULT COLLATE utf8mb4_0900_ai_ci;
USE renewableenergy;

CREATE TABLE pais (
  id_pais INT NOT NULL AUTO_INCREMENT,
  nome_pais VARCHAR(50) NOT NULL,
  PRIMARY KEY (id_pais),
  UNIQUE KEY nome_pais_un (nome_pais)
);

CREATE TABLE pais_producao (
  id_rel INT NOT NULL AUTO_INCREMENT,
  id_pais INT NOT NULL,
  ano INT NOT NULL,
  producao DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (id_rel),
  UNIQUE KEY id_pais_ano_un (id_pais, ano),
  CONSTRAINT id_pais_fk
    FOREIGN KEY (id_pais)
    REFERENCES pais (id_pais)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
);
