### Functionality
- API REST with Postgresql connection and Flask framework for Python (host=localhost/port=3000)
- App gives trought GET/POST methods a response in JSON format 
- index.html contains main methods for this REST API 


### Assumptions
- postal_codes.csv and paystats.csv were previously loaded into a PostgreSQL Database 
- Database implemented as a GeoDB, using PostGIS 3.1.2 (CREATE EXTENSION postgis;)
- Front End side can resolve Well-Known Text representation of the geometry for Polygons and Multipolygons

### install dependencies

```sh
pip install flask

pip install pygresql

pip install psycopg2
```

### Points to improve
- Implementation of validation for different dataTypes and Typo errors at routes
- Future implementation of GeoJson format for geometry representations
- Handle of multiple sessions and cache settings
- Improvement of Front End view
- Aggregation functionality that merges postal codes with paystat data 
