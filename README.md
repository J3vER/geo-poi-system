# Sistema de Registro de Puntos de Interés 

Este proyecto consiste en una aplicación web contenerizada que permite registrar y consultar puntos de interés con información geográfica, utilizando una base de datos con capacidades geoespaciales. El sistema fue desarrollado como práctica de uso de Docker, Docker Compose y arquitectura basada en microservicios.

##  Arquitectura del sistema

El sistema está compuesto por los siguientes servicios:

- **Base de Datos**: PostgreSQL con extensión PostGIS para manejo de datos geoespaciales.
- **Backend**: API REST desarrollada en Python con Flask.
- **Proxy Web**: Nginx como punto de entrada único al sistema.

Todos los servicios se ejecutan en contenedores Docker independientes y se comunican mediante una red interna definida en Docker Compose.

##  Tecnologías utilizadas

- Docker & Docker Compose
- PostgreSQL + PostGIS

## Acceso a la aplicacion
[text](http://localhost)
[text](http://localhost/points)
[text](http://localhost/points?category=cultural)