## Basclef Medical Diagnostics System
A solution that manages customers, staff, tests and all activities of a medical laboratory facility.


# INTRODUCTION
This is a django rest api that keeps track of every result that is given to a patient in a medical organization.

## Programming Language Used:
*Python Programming Language

## Technologies Used:
All of the following are technologies used in this project:
# Laboratory Management System


## Description

This Django web application is designed for managing laboratory tests, customers, and staff members.

## Technologies Used

- **Django**: Django is a high-level Python web framework that provides various tools and libraries for building web applications.

- **Django REST framework**: Django REST framework is an extension for Django that simplifies the creation of RESTful APIs. It's used for creating API endpoints in the project.

- **Python**: The project is written in Python, which is the primary programming language for Django.

- **PDFKit**: PDFKit is used for generating PDF documents from HTML and CSS. It is configured with the `wkhtmltopdf` executable for PDF generation.

- **BOOSTRAP and CSS**: These are fundamental technologies for building web pages and styling them.

- **JavaScript**: While it's not explicitly mentioned in the provided code, JavaScript is often used in web applications for client-side interactivity.

- **Database (SQLITE)**: Django typically uses relational databases (e.g., PostgreSQL, MySQL, SQLite) for data storage. The specific database used in the project is sqlite\
## Installation and Usage

1. Clone this repository to your local machine.

```bash
git clone https://github.com/your-username/laboratory-management-system.git

## users
| STAFF | ADMIN(superuser) |

## admin activities and permissions
Summarizing the different views and permissions:

This is a Django project that includes various views and APIs for managing user registration, authentication, and other related functionalities. Below, you'll find a summary of the different views and their associated user permissions in this project.

## Views and Permissions

# Application Permissions

This README provides an overview of the permissions associated with various links and actions in our application.

## User Permissions

### User Profile Link
- **Permission**: Read (View)
- **Description**: Users can view their own profile information.

### ADD PATIENT Link
- **Permission**: Create (Add)
- **Description**: Users can add new patient records.

### CREATE TEST Link
- **Permission**: Create (Add)
- **Description**: Users can create new tests.

## Superuser Permissions

The following permissions are only applicable to superusers who have additional privileges:

### LIST OF PATIENTS Link
- **Permission**: Read (View)
- **Description**: Superusers can view a list of all patient records.

### LIST OF STAFFS Link
- **Permission**: Read (View)
- **Description**: Superusers can view a list of all staff members.

### REGISTER STAFF Link
- **Permission**: Create (Add)
- **Description**: Superusers can register new staff members.

### LIST OF TEST Link
- **Permission**: Read (View)
- **Description**: Superusers can view a list of all tests.

## Other Actions

### LOGOUT Link
- **Permission**: Perform Action (Logout)
- **Description**: Users can log out of their accounts.

These permissions determine what actions users and superusers are allowed to perform within the application. Please make sure to configure your application's authentication and authorization system accordingly.



## EndPoints
* Application used for testing the endpoints - *DRF (Django Rest Framework) Test*


## URL Patterns

### Landing Page
- URL: `/`
- View: `LandingAPI`
- Description: This is the landing page of our application.

### Download View
- URL: `/download`
- View: `views.download`
- Description: Allows users to download something.

### PDF Generation View
- URL: `/pdf/`
- View: `views.generatePDF`
- Description: Generates a PDF.

### Dashboard
- URL: `/dashboard/`
- View: `DashboardAPI`
- Description: Provides access to the user's dashboard.

### User Registration
- URL: `/register/`
- View: `RegisterAPI`
- Description: Allows users to register for an account.

### User Login
- URL: `/login/`
- View: `LoginAPI`
- Description: Allows users to log in to their accounts.

### User Logout
- URL: `/logout/`
- View: `views.user_logout`
- Description: Logs the user out of their account.

### Staff List View
- URL: `/staff/`
- View: `StaffListView`
- Description: Lists staff members.

### Staff Tests View
- URL: `/staff/<int:staff_id>/tests/`
- View: `views.staff_tests`
- Description: Lists tests associated with a specific staff member.

### Create Customer View
- URL: `/create-customer/`
- View: `CreateCustomerView`
- Description: Allows the creation of customer records.

### Customer List View
- URL: `/customers/`
- View: `CustomerListView`
- Description: Lists customer records.

### Customer Detail View
- URL: `/customers/<int:pk>/`
- View: `CustomerDetailView`
- Description: Displays details of a specific customer record.

### Create Test View
- URL: `/create-test/`
- View: `CreateTestView`
- Description: Allows the creation of test records.

### Test List View
- URL: `/test-list/`
- View: `TestListView`
- Description: Lists test records.

### Test Detail View
- URL: `/test/<int:pk>/`
- View: `TestDetailView`
- Description: Displays details of a specific test record.

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
  git clone https://github.com/Kis123mas/alx_project.git
  ```
2. Move into the project directory
  ```
  cd medicallab
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