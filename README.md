# Django-Assignment

The Code will satisfy the defined requirements.

1. Users has to Enter Username,Mail,Password,Address and Mobile and validations like username is only characters, Password should contain atleast one special Character and Mobile Number has to be of length 10
2. Credentials have to be sent to mails.
3. An  API that lets the users to Login
4. An API to get all the users details in JSON Fomat

Tech Stack: Django Framework, Python
Database: JSON 

## To Run This Project
Step 1: Clone the Repository
  ```
  git clone https://github.com/THRINADH43/Django-Assignment.git

  ```
Step 2: Change Directory to Django-Assignment
```
cd Django-Assignment   
```
Step 3: Install the Requirements
```
pip install -r  requirements.txt    
```
Step 4: Change Modification in "settings.py" under "Assignment_Django". This step is needed to send mails. Remember google disabled sending 3rd party mails from personal account. So, You have to Configure SMTP provider credentials 
![image](https://user-images.githubusercontent.com/74821042/230353620-fbc3dd5a-6a6f-4d10-b192-9d429a460d59.png)


Step 5: Run the Server

```
     py manage.py runserver    
```

Step 6: The Index is Located at:
```
http://127.0.0.1:8000/assignment/index/
```
step 7: To View the User Data in JSON navigate to:
```
http://localhost:8000/assignment/userview/
```

Step 8: To Login. Use this
```
http://127.0.0.1:8000/assignment/logindata/
```
