# create API with Permissions
1. create poetry poroject
2. add django and rest framework
3. create django project using `django-admin startproject 'projectname' .`
4. `python manage.py migrate`
5. `python manage.py createsuperuser`
6. create new app `python manage.py startapp 'appname'`
7. create model and then register it to the admin
8. add the app to the settings.py
9. `python manage.py makemigrations` then `python manage.py migrate`
10. create api folder:
11. create viewsets , add to it the APIViews
12. create serializers, create app serializer 
13. add serializer to viewsets
14. create urls file and include it to main project urls
15. create permissions , add permissions to viewset
----
### Docker
1. add Docker file 
2. add docker-compose.yml
3. run `poetry export -f requirments.txt --output requirments.txt`
4. if we want to use postgres add it to the .yml file
5. run `sudo docker compose build`
6. run `sudo docker compose up`
7. add postgres to settings.py DATABASE
8. run `poetry add psycopg2-binary`
9. use `sudo docker compose build` & `sudo docker compose up` again
10. we can use `sudo docker compose up -d` to make the server run in the background and we can use the terminal.
11. use `sudo docker compose run web python manage.py migrate` to migrate to the container 
12. user `sudo docker compose stop`& `sudo docker compose start` to stop the container w/o losing the database.



----
[pull request](https://github.com/SalimHass/drf-api-permissions-postgres/pull/1)
