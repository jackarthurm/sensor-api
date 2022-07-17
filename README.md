# Sensors
A RESTful Django web API for managing sensor resources and their measurement data records

Implemented with a typical application architecture: DRF API views -> DRF serializer schema -> Django ORM object model -> SQL database.

Includes a very basic unit conversion framework which ensures all measurement data is persisted to the database in SI units.

Includes a bulk data endpoint for creating multiple measurements at once.

## Getting started

- Set the environment variable `DATABASE_URL` to a database connection string, for example `postgres://postgres:password@127.0.0.1:5432/dbname`
- Run the Django development server with `python manage.py runserver`
- Run the test suite with `python manage.py test`
