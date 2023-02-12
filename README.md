# 🚀 Django User Management 

## Acknowledgements
- This project is a part of the [Gaza Sky Geeks ](https://gazaskygeeks.com/) Training program.
<p align="center">
<img src="https://gazaskygeeks.com/wp-content/uploads/2020/05/gsg-website-logo-colored-280-50.png" width="40%">
</p>

## Introduction
A Django application that allows users to register, log in, reset, and change their passwords. 

## Features 📌
- User registration with the option to create a new user
- User login and logout 
- Password change and reset 
- Sending password reset emails to actual email addresses 
- Authenticate using an external service 

## Back-end
- The back-end of the application is built using Django (Python Framework)

## URLs 🌍
- `admin/` for administrative goal
- `accounts/login/` for logging a user into your application 
- `accounts/logout/` for logging a user out of your application
- `accounts/password_change/` for changing a password 
- `accounts/password_change/done/` for confirming a password change 
- `accounts/password_reset/` for requesting a password reset email 
- `accounts/password_reset/done/` for confirming a password reset email was sent
- `accounts/reset/<uidb64>/<token>/` for setting a new password using a password reset link
- `accounts/reset/done/` for confirming a password reset 

## User Registration 📝
Django doesn’t provide user registration by default. However, Django offers forms that can be used in your projects such as `UserCreationForm` which contains all the necessary fields to create a new user, excluding the email field. 

## How to Add URLs 💻
To add these URLs to your project, you will need to include them in your project's URL configuration file. 

## Usage

To use this flashcard app, follow these steps:

1. Clone the repository to your local machine: 
`git clone https://github.com/Mahmoud-Hijjeh/userManagement_django.git`.
2. Create a virtual environment: `python3 -m venv venv`.
3. Activate the virtual environment: `source venv/bin/activate`.
4. Install the required packages with `pip install -r requirements.txt`.
5. Apply migrations: `python manage.py migrate`.
6. Run the development server with `python manage.py runserver`.
7. In your web browser, go to `http://127.0.0.1:8000/` to access the app.

## Contribute 🤝
Feel free to contribute to this project by opening an issue or submitting a pull request. Let's build this together! 

## License 📄
This project is licensed under the [MIT License](LICENSE.md).

## Images 
![1](https://user-images.githubusercontent.com/107920651/218275159-d34ecbdc-2678-4527-a0c8-cd14e1dd6e21.PNG)
![2](https://user-images.githubusercontent.com/107920651/218275165-726ca422-9fe4-49f6-ba77-3dfbc2cc1059.PNG)
![3](https://user-images.githubusercontent.com/107920651/218275171-7f4fd5ac-3bf6-437d-bcc9-a100c363928d.PNG)
![4](https://user-images.githubusercontent.com/107920651/218275179-3e9670fe-3bc2-4e9e-bc43-0b02333288ba.PNG)
![5](https://user-images.githubusercontent.com/107920651/218275181-a85a94a9-d0f8-4579-8880-31601d7e715a.PNG)
![6](https://user-images.githubusercontent.com/107920651/218275184-95cfbfba-2dd0-4bf5-834b-95bd64c6073a.PNG)
![7](https://user-images.githubusercontent.com/107920651/218275190-940857ae-c5f9-4bcf-a6ba-e2dadc3cda9c.PNG)
![8](https://user-images.githubusercontent.com/107920651/218275187-dbb46b0d-331c-4c3f-a4e8-45b3696e5621.PNG)
