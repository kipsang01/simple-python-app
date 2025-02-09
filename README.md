# SIMPLE DJANGO REST FRAMEWORK APP
This is a simple DRF app that displays a large application's development process and deployment automation.

This App assumes you have already set the server e.g. an AWS ec2 instance and you have a database set.

Check this project [app with infrastructure](https://github.com/kipsang01/rest-api) that sets infrastructure using Terraform and deploys it in EKS. 
## USAGE
#### Authorization
Uses OIDC built on top of OAuth2.0.  
All OAuth2.0 url paths apply with prefix `/o/`, check the documentation [here](https://django-oauth-toolkit.readthedocs.io/en/2.3.0/oidc.html)  

Get token endpoint
- url: ``localhost:8000/o/token``
  - POST :
    - params: ``username, password``
    - returns: ``access_token, refresh_token,``
####  Customers
Customers endpoint. Accepts ``GET, POST, PUT, DELETE``  
Authorization: ```Bearer <token>```
  - GET:
    - list-url: ``localhost:8000/api/customers/``
    - specific-url: ``localhost:8000/api/customers/<customer_id>/``
    - response: ``status_code: 200 ``  


  - POST:
    - url: ``localhost:8000/api/customers/`` 
    - params: 
      - ``name``: optional
      - ``code``: required
      - ``phone_number``: required
    - response: ``status_code: 201 `` 


  - DELETE:
    - url: ``localhost:8000/api/customers/<customer_id>/``
    - params: ``none``
    - response: ``status_code: 204``
  
####  Orders
Customers endpoint. Accepts ``GET, POST, PUT, DELETE``  
Authorization: ```Bearer <token>```
  - GET:
    - list-url: ``localhost:8000/api/orders/``
    - specific-url: ``localhost:8000/api/customers/<order_id>/``
    - response: ``status_code: 200 ``  


  - POST:
    - url: ``localhost:8000/api/orders/`` 
    - params: 
      - ``customer``: int,  required
      - ``item``: string, required
      - ``amount``: float, required
    - response: ``status_code: 200 ``

  - DELETE:
    - url: ``localhost:8000/api/orders/<order_id>/``
    - params: ``none``
    - response: ``status_code: 204``
  

## DEVELOPMENT
To run in development environment:
- Clone the project
- create ``.env`` file with the following variables:
  - DATABASE_NAME
  - DATABASE_USER
  - DATABASE_PASSWORD
  - DATABASE_HOST
  - DATABASE_PORT
  - AFRICASTALKING_API_KEY
  - AFRICASTALKING_USERNAME
  - AFRICASTALKING_SENDER_ID
  - DEBUG_MODE
  - DJANGO_ALLOWED_HOSTS
  - DJANGO_SECRET_KEY
  - OIDC_RSA_PRIVATE_KEY
  - >To get `AFRICASTALKING` credentials visit [africastalking](https://developers.africastalking.com/).

- create postgres database.
- pip install requirements:
  - ``pip install -r requirements.txt``
- run migration commands:
  - ``python manage.py makemigrations``
  - ``python manage.py migrate``
- to create superuser:
  - ``python manage.py createsuperuser --username=<username> --email=<email> --password=<password>``
- run django server:
  - ``python manage.py runserver``
- to run tests:
  - ``coverage manage.py test``
    
### Integration and Deployment
This application is configured to use github actions for continuous integration and deployed to a server running in any cloud platform.
Add the following to repository secrets:  
- DATABASE_NAME
- DATABASE_USER
- DATABASE_PASSWORD
- DATABASE_HOST
- DATABASE_PORT
- AFRICASTALKING_API_KEY
- AFRICASTALKING_USERNAME
- AFRICASTALKING_SENDER_ID
- DJANGO_SECRET_KEY
- OIDC_RSA_PRIVATE_KEY

And this to repository variables:
- DEBUG_MODE
- DJANGO_ALLOWED_HOSTS

The application is configured to run tests on every push to the repository and deploy to the server on every merge to the main branch.






