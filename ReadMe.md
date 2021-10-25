# LMS_DEMO.
**This project is kind of Book Management System project is maintaining the book's stock and availability for the students, other type of user.
project developed with django , python and delivering the APIs, having some test cases, as per the requirements .
for getting repository [ click here](https://github.com/nakushwah/nakushwah.git). for this project using sqlite3 database** 

* ###### Requirements :-
    Python>=3.6\
    Django>=3.2\
    djangorestframework==3.12.4\
    djangorestframework-simplejwt==5.0.0

* ###### Setup project  :-
    **steps**
    1. clone the repo  [.....CLick Here.....](https://github.com/nakushwah/nakushwah.git)
    2. get in the directory and open the terminal or command prompt with that path find the `manage.py`file and `requirements.txt` file 
    3. install all the requirements using `pip3 install -r requirements.txt` this command.
    4. make sure all migrations `python3 manage.py makemigrations` and then migrate `python3 manage.py migrate` it.
    5. for running the whole project use `python3 manage.py runserver` once server run successful congrats project setup done 🙂
  

_Project having  two APPS (Book, UserAuth) , one main project's directory (LMS), each app having its test cases for testing the serializers and APIS_

_For Running the TestCases run the command in `./manage.py test <file_path>` (use the (.)dot inplace (/) slash)._


* ###### APIs :-
  _**UserAuth's :-**_\
  1. **GET** `api\ListCreateUser` for getting all the user's list 
      * ```
        "email": "kumar1243@gmail.com",
        "username": "kumar1234",
        "first_name": "nk",
        "last_name": "a",
        "city": "kghjh",
        "contact": 123456789,
        "Address": "ds",
        "education": "dsdfds",
        "user_roles": "Author",
        "id": "6499defd-8044-44df-bef5-5dd2342d81d5"

  2. **POST** `api'listCreateUser` for creating users 
      * ```
        payload {
        "email": "kumar1243@gmail.com",
        "username": "NDK123",
        "first_name": "kumar21",
        "last_name": "ndk22",
        "city": "Indore",
        "contact": 2134567890,
        "Address": "india",
        "education": "BE",
        "password": <"passworrd">,
        "user_roles": "Author/Student"        
        }
    
  3. **PUT, DELETE, GET** `api/UpdateUser/<pk>` pk stands for id. And payload will be same as given above   
  4. **POST** `api/loginView/`
     ```
     input:-
        
           "username": "NDK123",
           "password": password,
     response:- 
           "refresh": "token_value",
           "access": "token_value"
     
  5. **POST** `api/RegisterView/`
    ``` {
    "email": "kumar1243@gmail.com",
    "username": "NDK123",
    "first_name": "kumar21",
    "last_name": "ndk22",
    "password": password,
    "password2": confirm password,
    ```
    
  6. **POST** `api/LogoutView/` 
    
    * 
      ```
      {
      "refresh_token":"token_value"
      }
      ```
  7. **GET** `book/get_books/` for getting all book's list 
     * ```
          output :- {
          "id": "4321baf4-0340-4e51-af66-2f8d61c3532e",
          "title": "fsf",
          "author": "admin@gmail.com",
          "issue_to_user": "narendrakush@gmail.com",
          "issue_from": "2021-10-25T16:10:00Z",
          "issue_to": "2021-10-25T16:10:00Z",
          "published_date": "2021-10-25T14:16:00Z",
          "price": 0.0,
          "penalty": 0
          }
       ```
  8. **POST** `book/get_books/` :-
      * ```
          {
          "title": "fsf",
          "author": "admin@gmail.com",
          "issue_to_user": "narendrakush@gmail.com",
          "issue_from": "2021-10-25T16:10:00Z",
          "issue_to": "2021-10-25T16:10:00Z",
          "published_date": "2021-10-25T14:16:00Z",
          "price": 0.0,
          "penalty": 0
          }
        ```
  9. **GET , PUT , DELETE**  `edit_books/<pk>/` _pk=id_ payload will be same as point viii.


###### run the test file:
  1. for UserAuth Test file `./manage.py test UserAuth.test`
  2. for Book Test File `./manage.py test Book.test`


**TO DO** :- 
1. AUTO LogOUT
2. Authorized Test Cases
3. email verification 
