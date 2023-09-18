## medical laboratory test, patient and staff management API

A solution that manages customers, staff, tests and all activities of a medical laboratory facility.


# INTRODUCTION
This is a django rest api that keeps track of every result that is given to a patient in a medical organization.

## Programming Language Used:
* Python Programming Language

## Technologies Used:
All of the following are technologies used in this project:

| Backend | Django |
| -------- | ----------- |
| Api | Django REST framework |
| -------- | ----------- |
| Project Management and Version Control | Github |
| -------- | ----------- |
| Database | sqlite |
| -------- | ----------- |
| Test of Endpoints | Postman |

## users
| STAFF | ADMIN |

## super-admin activities and permissions
[__Register__]- staff can register by filling up thr registeration form by giving their details like email, firstname, lastname, password and username.

[__Login__] - Only Registered staff can login using just their username and password.

[__Logout__] - Login staff can logout using their token.

[__CreateCustomer__] - staff can create customer account.

[__ViewCustomerDetails__] - staff can view customer details.

[__UpdateCustomerDetails__] - staff can update customer details.

## staff activities and permissions

[__Login__] - Only Registered staff can login using just their username and password.

[__Logout__] - Login staff can logout using their token.

[__CreateCustomer__] - staff can create customer account.

[__addtest__] - staff can view customer details.




## admin activities and login
[__Register__]- admin can register by filling up the registeration form by giving their details like email, firstname, lastname, password and username.

[__Login__] - Only Registered admin can login using just their username and password.

[__Logout__] - Login admin can logout using their token.

[__Viewstaff__] - admin can view registered staff.

[__DeleteStaff__] - admin can delete registered staff.

[__CreateCustomer__] - admin can create customer account.

[__ViewCustomerDetails__] - admin can view customer details.

[__UpdateCustomerDetails__] - admin can update customer details.

[__DeleteCustomer__] - admin can delete customer account.


## EndPoints Test
* Application used for testing the endpoints - *POSTMAN*

[__REGISTER ENDPOINT__]

USER REGISTERATION TEST. 
| Request | POST |
| -------- | ----------- |
| Url | POST  http://127.0.0.1:8000/diagnostic/register/ |
| -------- | ----------- |
| Select body, and then click on form-data | fill in these keys  : username, password, email, first_name and last_name *fill in your values for the keys and send* |
| -------- | ----------- |
| status | 200_OK - Registeration was successful.|
| -------- | ----------- |
| status | 400 Bad Request - Error in registeration |



[__LOGIN ENDPOINT__]

LOGIN REGISTERATION TEST.

| Request | POST |
| -------- | ----------- |
| Url | POST  http://127.0.0.1:8000/diagnostic/login/ |
| -------- | ----------- |
| Select body, and then click on form-data | fill in these keys  : username and password *fill in your values for the keys and send* |
| -------- | ----------- |
| status | 200_OK - Login was successful.|
| -------- | ----------- |
| status | 400 Bad Request - Error in login |


[__CREATE CUSTOMER ENDPOINT__]

CREATE CUSTOMER ENDPOINT TEST.

| Request | POST |
| -------- | ----------- |
| Url | POST  http://127.0.0.1:8000/diagnostic/customer/ |
| -------- | ----------- |
| Select headers | create this key  : Authorization | fill in your token  : in these format *Token <input token here>* |
| -------- | ----------- |
| Select body, and then click on x-www-form-urlencoded | create in these keys  : old_password, new-password *fill in your values for the keys and send* |
| -------- | ----------- |
| status | 200_OK - Password Updated successfully.|
| -------- | ----------- |
| status | 401 Unauthorized, 400 Bad request |

[__VIEW CUSTOMERS ENDPOINT__]

VIEW CUSTOMER ENDPOINT TEST.

| Request | GET |
| -------- | ----------- |
| Url | GET  http://127.0.0.1:8000/diagnostic/customer/ |
| -------- | ----------- |
| Select headers | fill in your token  : in these format *Token <input token here>* |
| -------- | ----------- |
| status | 200_OK - Userdetail was successful.|
| -------- | ----------- |
| status | 400 Bad Request - Error in Userdetail |


[__UPDATE ENDPOINT__]

UPDATE ENDPOINT TEST.

| Request | PUT |
| -------- | ----------- |
| Url | PUT  http://127.0.0.1:8000/diagnostic/customer/ |
| -------- | ----------- |
| Select headers | create this key  : Authorization | fill in your token  : in these format *Token <input token here>* |
| -------- | ----------- |
| status | 204 No content - Logout successful.|
| -------- | ----------- |
| status | 401 Unauthorized (invalid token), 400 Bad request |

[__DELETE ENDPOINT__]

DELETE ENDPOINT TEST.

| Request | DELETE |
| -------- | ----------- |
| Url | DELETE  http://127.0.0.1:8000/diagnostic/customer/ |
| -------- | ----------- |
| Select headers | create this key  : Authorization | fill in your token  : in these format *Token <input token here>* |
| -------- | ----------- |
| status | 204 No content - Logout successful.|
| -------- | ----------- |
| status | 401 Unauthorized (invalid token), 400 Bad request |


## Project Status
Project is : *in progress*

## Collaboration 
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated** 🤝

## Dependencies
asgiref==3.7.2
cffi==1.15.1
cryptography==41.0.3
Django==4.2.5
django-rest-knox==4.2.0
djangorestframework==3.14.0
pdfkit==1.0.0
pycparser==2.21
pytz==2023.3.post1
sqlparse==0.4.4
typing_extensions==4.7.1
tzdata==2023.3

### Getting Started
Setting up project locally is a pretty easy step.

1. Clone the repo
  ```sh
  git clone https://github.com/Kis123mas/API-AUTHENTICATION.git
  ```
2. Move into the project directory
  ```
  cd authentication
  ```
3. Create a virtual environment
  ```
  python -m virtualenv venv 
  ```
4. Activate the virtual environment
  ```
  venv\Scripts\activate
  ```
6. Install pip dependencies
  ```
  pip install -r requirements.txt
  ```
8. Make Migrations
  ```
  py manage.py makemigrations
  ```
9. Migrate to Database
  ```
  py manage.py migrate
  ```
10. Create a superuser
   ```
   py manage.py createsuperuser
   ```
11. Run Server
   ```
   py manage.py runserver
   ```

<br/>