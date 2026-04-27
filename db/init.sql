CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE points_of_interest (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    category TEXT,
    location GEOGRAPHY(POINT, 4326)
);

INSERT INTO points_of_interest (name, description, category, location)
VALUES
('Parque Central', 'Centro histórico de la ciudad', 'cultural', ST_MakePoint(-90.5069, 14.6407)),
('Museo Nacional', 'Museo de historia', 'cultural', ST_MakePoint(-90.5132, 14.6415)),
('Gasolinera Shell', 'Estación de servicio 24h', 'servicio', ST_MakePoint(-90.5201, 14.6352)),
('Restaurante El Buen Sabor', 'Comida típica', 'gastronómico', ST_MakePoint(-90.5098, 14.6376)),
('Mirador Natural', 'Vista panorámica', 'natural', ST_MakePoint(-90.5305, 14.6501));