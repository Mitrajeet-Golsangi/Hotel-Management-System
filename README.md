# Hotel-Management-System

A web application to implement the hotel management system

## Method for setting up the Django Project

1. Create a git repository using `git init`
2. Add the remote repository using `git add origin https://github.com/Mitrajeet-Golsangi/Hotel-Management-System.git`
3. Pull your required branch using `git pull --set-upstream origin branch_name`
4. Now run `pip install virtualenv` in command prompt
5. Create a virtual environment using `virtualenv dbms_cp`
6. Activate the virtual environment using `dbms_cp\Scripts\activate`
7. Now, run `pip install -r requirements.txt`
8. After setup is complete, add the environment file shared to the collaborators in root directory
9. Done !

## Method for Setting up PostgreSQL in Django Application

1. Install PostgreSQL 14.3 from [here](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
2. Follow the [download instructions](https://www.enterprisedb.com/docs/supported-open-source/postgresql/installer/02_installing_postgresql_with_the_graphical_installation_wizard/01_invoking_the_graphical_installer/)
3. Now search 'Edit the system environment variables' in Windows
4. click on 'Environment Vairables' button
5. In new window Click on 'New' to create a new vairable
6. Make it's name as 'PSQL_PAS' (case sensitive)
7. In the value provide the password which you provided while installation of PostgreSQL
8. Click 'OK' for all the open windows
9. Restart any running applications in order for changes to take effect
10. Open pgAdmin 4 on you computer
11. Click Servers(1)
12. Right click on PostgreSQL 14 and create new database named 'hotel_management_system'
13. Now, open the command prompt in the location of the django project
14. Run the following command 'py manage.py migrate'
15. After successful migration, check your database in postgreSQL
16. In Servers(1) > PostgreSQL 14 > hotel_management_system > schemas > tables you will see multiple new tables used by default by django
17. Done ! You are all set with postgreSQL
