# AssystantDjangoProject
 

#### Create a virtualenv 
`virtualenv venv`


#### Activate the env

##### linux
`source venv/bin/activate`

##### window
`venv\Scripts\activate`




## Now run following commands on activated virtualenv


#### Install required packages
`pip install -r requirements.txt`


### Run Server
`python manage.py runserver



## API Endpoints

### API ROOT
#### http://127.0.0.1:8000/api/


# Task:

## 1. Create CRUD endpoints for Student
## http://127.0.0.1:8000/api/student/

## 2. 2. Create custom create and update for student to create instance in the form of
## http://127.0.0.1:8000/api/student/

## 3. Display full_name as a field in any of the list endpoint, retrieve as a read_only field combining first_name and last_name
## http://127.0.0.1:8000/api/student/

## 4. Write a  Django orm to list students in the form of below output, and create an endpoint to display the same
## http://127.0.0.1:8000/api/count/
