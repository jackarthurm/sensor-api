# Sensors
A RESTful Django web API for managing sensor resources and their measurement data records

Implemented with a typical Django application architecture: DRF API views -> DRF serializer schema -> Django ORM object model -> SQL database.

Includes a very basic unit conversion framework which ensures all measurement data is persisted to the database in SI units.

## Getting started

- Set the environment variable `DATABASE_URL` to a database connection string, for example `postgres://postgres:password@127.0.0.1:5432/dbname`
- Run the Django development server with `python manage.py runserver`
- Run the test suite with `python manage.py test`

## Using the Django-admin site

- Create an admin account with `python manage.py createsuperuser`
- Login at `/admin`

## Browsing the REST API

- Navigate to `/api/sensor` to GET the list of sensors and POST new sensors
- Navigate to `/api/sensor/<sensor ID>` to GET a sensor
- Navigate to `/api/data for the list of measurements, to POST a new measurement or to PATCH a new batch of measurements to the list
- Navigate to `/api/data?sensor=<sensor name> for the list of measurements, filtered by sensor
