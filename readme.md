# Login Page Creation

Installation
- 
- install django, django-simple-captcha via pip.

      pip install django
      
      pip install django-simple-captcha

- Add **captcha** to **INSTALLED_APPS** in **settings.py**.

- create table for captcha by migrating.
      
        py manage.py migrate

  - Make an entry by adding captcha path to project level url

        urlpatterns = [
            path('captcha/', include('captcha.urls')),
        ]

problem :
- 
create html page for logging into Employee notification system.
 
Business :
- 
Design a page to verify whether the user is valid account holder or not.

Solution :
- 
- 
- Navigate to templates folder and create a html page login.html in  Employee_Note subfolder
- create tags for username and password input fields.
- 