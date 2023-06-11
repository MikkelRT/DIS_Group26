# Wheels & Deals
The Wheels & Deals App is a web application that allows users to search for vehicles based on various criteria and view the search results. It provides a user-friendly interface for selecting car type, manufacturer, mileage, price, and leather seats preference.

## Features
- **Search Form**: The app presents a search form where users can select car type, manufacturer, mileage, price, and leather seats preference.
- **Database Connection**: The app connects to a PostgreSQL database to fetch search results based on the users input.
- **Search Results**: The search results are displayed in a table, showing car type, manufacturer, mileage, and price.
- **Choose Another Car**: Users can go back to the search form by clicking the "Choose another car" button.

## Requirements
- Flask
- PostgreSQL
- HTML
- CSS
- Python
- Psycopg2

In order to install Flask and Psycopg2 run the following command:
>$ pip install -r requirements.txt

## Run guide
1. Create a new database in pgAdmin.
2. Set the database and your password to pgadmin in app.py file.
3. Run table.sql and data.sql in your database in pgadmin.
4. Now see "Running in flask" or "Running in python"

## Running in flask
$ flask run

## Running in python 
$ python3 app.py

## Other
If the http:// doesn't work on Chrome please try another browser like Safari 


