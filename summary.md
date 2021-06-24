### Step by Step

- Based on the representation of the wireframe and the two datasets, I implemented different functions written in Python using Flask as a framework for web development.

- Due to the nature of the implementation of the functions, the model that I implemented was an API REST where all requests (POST, GET,..) would be resolved by server side.

- Implemented index.html as a frame to handle the request simulating a client side in order to retrieve relevant data.


### Main Functionalities in <index.html>

- The data retrieved by html client are focused on next considerations:

* Get All Polygons. 
  - Here all the polygons for postal_codes are retrieved in JSON format, using for it ST_AsText function from PostGIS extension previously installed on PostgreSQL DataBase

* Get Total Amount (Postal code, Age and gender). 
  - All the data grouped by Postal code, Age and gender are obtained in JSON format

* Obtain Total Amount by Date. 
  - Through selection of dates(start and end) the total paid amount for this period will be retrieved

* Obtain Total Amount by Gender. 
  - Through selection of Gender(Female and Male) the total paid amount for this categories will be retrieved

* Obtain Total Amount by Postal. 
  - CodeThrough selection of Postal Codes(from postal codes for data availables on data source) the total paid amount for this postal codes will be retrieved

* Obtain Total Amount by AgeThrough selection of  range of age(from data from data source) the total paid amount for this ranges will be retrieved
