NEW DAWN FITNESS
------

![image](https://user-images.githubusercontent.com/56481190/204462894-c2c589dc-c158-4c9d-883a-bd51cc290b18.png)

----
For my milestone project 5 for Code Institute Diplome in Software development, I have chosen Project Example Idea 1 to build a fintess subscription application. It will be a online fitness and nutrion site. New Dawn provides a platform for people who are into fitness or are looking to get into the world of fitness. Ina world which so much fitness clutter New Dawn will help people who are looking for an easy and simple fitness formula with online subscritions and a selection of nutrion products. It will be developed using Django which is a high-level Python web framework and deployed using Heroku.

Heroku URL: https://new-dawn-fitness.herokuapp.com/

GitHub URL: https://github.com/colinshaw1/new_dawn_fitness

------
Owner
-------
The owner of this game is Colin Shaw. The goal is to help anyone who is looking at imporing or starting there fitness journey.

-------
Who is New Dawn Fitness for?
------
New Dawn Fitness is a new fitness site intended to help anyone who is intreseted in Fitness or looking to get into the world of fitness. If you are looking for some supplements or just looking to get a online plan then new dawn is for you. 

-------

How to use New Dawn
----
New Dawn Fitness is an easy to navigate site and can be on an device. From the home you can navivgate to to anywhere in the application. The navbar has a responsive search bar that will return results of any project from the applications database. Within the navabr you can go to the profile section and create an account or login to see your order history or update your profile settings. Also you have the shopping cart where you can go to checkout securly using stripes secuire checkout settings. Under the navar you have the products you can choose you want to view via catrgories. 

-----
Screenshots of Application
---------
Homepage
--
![image](https://user-images.githubusercontent.com/56481190/204462972-724fd66e-53a9-4a17-be7b-2c26d58d592a.png)

Protein Search 
---
![image](https://user-images.githubusercontent.com/56481190/204463038-a63a4e27-67a6-476c-b8bc-ef09bd375e70.png)

![image](https://user-images.githubusercontent.com/56481190/204463125-009309a4-b5c5-4fd1-956b-832c4ab41640.png)

Products details
--
![image](https://user-images.githubusercontent.com/56481190/204463197-14a4865c-40e2-4076-9c5d-ba8672c3d56d.png)

Add to bag
--
![image](https://user-images.githubusercontent.com/56481190/204463270-fd0dac8d-72e7-40f8-b687-537c9c7e1b53.png)

Shopping bag
---
![image](https://user-images.githubusercontent.com/56481190/204463354-94cdae76-92f2-446e-9212-f5eef2d811dd.png)


----
Agile Methodology
------

Start of planning Trello board
-----

![image](https://user-images.githubusercontent.com/56481190/204457165-d97a9b49-06aa-4d15-b1af-4bfead87580e.png)

---
Progress is underway as the products app is been started
----

![image](https://user-images.githubusercontent.com/56481190/204457409-31908cb5-eb17-45e3-97c4-5dc318ceeb18.png)
---
Products app is done and we move onot the checkout app
-------

![image](https://user-images.githubusercontent.com/56481190/204457593-13e04c4b-4f99-4aec-8f4e-912515d0e6cf.png)
----

Development is nearly done
-------
![image](https://user-images.githubusercontent.com/56481190/204457736-a9c2b97f-419b-4520-9d6e-b02d4aa884df.png)

Application progressing and just a couple of tasks left to do.
------
![image](https://user-images.githubusercontent.com/56481190/204457941-236de66d-73b8-4e47-bae8-ef5ecb0a8cf8.png)

------
Everything finsihed just needs to be deployed on Heroku
------
![image](https://user-images.githubusercontent.com/56481190/204458191-a5377753-eb38-41a0-9f9d-b357c531e86d.png)


User Experience
---
Website users

• As a user, you want to be able to navigate clearly and hassle-free throughout the whole application.

• As a user, you want to be able to scroll and read the content on the website with no contrast.

• As a user, you want to be able to click on any link on the website to go to the source destination with no errors.

• As a user, you want to be able to fill out a comment and submit it with no issues.

-----
Strategy Plane
------

New Dawn Fitness was created and designed for for anyone looking to start or imprve there fitness journey. Anyone can easily set up an account and navigate though the application very easily. 

-------
Scope Plane

• Created in Django

• Home page has eight clickable links

• Click on the logo, search icon, profile icon, or checkout icon or the lets get started button in the home page to navgiate to the selected field

• New Dawn Fitness Logo navigates to the home page

• Search bar icon will return a search item from the list of products

• Profile icon will bring the user to the profile app section, in this section userscan regiser for an account, login or logout. Once logged in order hsitorys can be checked and profile settings updated.

• Checkout icon will bring users to the checkout section were they can update an order and enter there details for a secure checkout using stripe.

• The products section will bring you to a selected product category. 

• The lets get started button will load the all products category.

------
Structure Plane
-------

• The application consists of nine folders which contain the html, css, pyton that helps the applcation run.
The the other appliaction folders Homepage, checkout, products, proifles and shoopping bags which hold the applications css, html, JavaScript and pyton files to help the applciation work via url links and views and models designed. 

Technologies used
------------
• Python is used to implement complex functions

• Django is used as it is a python based framework and its models, templates and views simplify complex tasks

• Git for storing files and deployment

• Heroku is used for final deployment

• Gitpod for design

-------
Resources
----
• Code institute for material and ideas

• Geeks for Geeks for information and ideas

• W3 Schools for information and ideas

• Slack for inspiration

• YouTube for tutorials

• Course content was used for some functionality from walkthoughs 

• Tutor support

---


Bugs

---
-----> Building on the Heroku-22 stack
-----> Using buildpack: heroku/python
-----> Python app detected
-----> No Python version was specified. Using the same version as the last build: python-3.10.8
       To use a different version, see: https://devcenter.heroku.com/articles/python-runtimes
-----> No change in requirements detected, installing from cache
-----> Using cached install of python-3.10.8
-----> Installing pip 22.3.1, setuptools 63.4.3 and wheel 0.37.1
-----> Installing SQLite3
-----> Installing requirements with pip
-----> $ python manage.py collectstatic --noinput
       Traceback (most recent call last):
         File "/tmp/build_77107db7/manage.py", line 22, in <module>
           main()
         File "/tmp/build_77107db7/manage.py", line 18, in main
           execute_from_command_line(sys.argv)
         File "/app/.heroku/python/lib/python3.10/site-packages/django/core/management/__init__.py", line 419, in execute_from_command_line
           utility.execute()
         File "/app/.heroku/python/lib/python3.10/site-packages/django/core/management/__init__.py", line 413, in execute
           self.fetch_command(subcommand).run_from_argv(self.argv)
         File "/app/.heroku/python/lib/python3.10/site-packages/django/core/management/base.py", line 354, in run_from_argv
           self.execute(*args, **cmd_options)
         File "/app/.heroku/python/lib/python3.10/site-packages/django/core/management/base.py", line 398, in execute
           output = self.handle(*args, **options)
         File "/app/.heroku/python/lib/python3.10/site-packages/django/contrib/staticfiles/management/commands/collectstatic.py", line 187, in handle
           collected = self.collect()
         File "/app/.heroku/python/lib/python3.10/site-packages/django/contrib/staticfiles/management/commands/collectstatic.py", line 114, in collect
           handler(path, prefixed_path, storage)
         File "/app/.heroku/python/lib/python3.10/site-packages/django/contrib/staticfiles/management/commands/collectstatic.py", line 338, in copy_file
           if not self.delete_file(path, prefixed_path, source_storage):
         File "/app/.heroku/python/lib/python3.10/site-packages/django/contrib/staticfiles/management/commands/collectstatic.py", line 248, in delete_file
           if self.storage.exists(prefixed_path):
         File "/app/.heroku/python/lib/python3.10/site-packages/storages/backends/s3boto3.py", line 467, in exists
           self.connection.meta.client.head_object(Bucket=self.bucket_name, Key=name)
         File "/app/.heroku/python/lib/python3.10/site-packages/botocore/client.py", line 530, in _api_call
           return self._make_api_call(operation_name, kwargs)
         File "/app/.heroku/python/lib/python3.10/site-packages/botocore/client.py", line 960, in _make_api_call
           raise error_class(parsed_response, operation_name)
       botocore.exceptions.ClientError: An error occurred (403) when calling the HeadObject operation: Forbidden
 !     Error while running '$ python manage.py collectstatic --noinput'.
       See traceback above for details.
       You may need to update application code to resolve this error.
       Or, you can disable collectstatic for this application:
          $ heroku config:set DISABLE_COLLECTSTATIC=1
       https://devcenter.heroku.com/articles/django-assets
 !     Push rejected, failed to compile Python app.
 !     Push failed
 
Unfortnutly this bug was not fixed on time and applcintions static files load for AWS, in heroku for deployment.

----

Version Control

-------
GitHub and GitPod to update and commit changed to my repository all commits tracked to mark progress
-----
Deployment

---
Planned deployment via Heroku.
