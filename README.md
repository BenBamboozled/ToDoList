# ToDoList
A simple To Do List web application. I wanted a personal todo list that I can update from anywhere on the internet connected to a database. Although there are many todo apps available on the internet, I thought this would be a good way to learn the django framework, and other web devoplment skills. This is my first time using the django framework.

## Build With
-Python
-Django Framework 
-Javascript / jQUERY 
-Html
-CSS

## Requirements
-A machine or virtual machine with Python installed(I used python 3.7.2) (I used linux but windows could be used during dev)
-virtualenv(not nesscarily required but good practice)
-All other requirements including django and dependencies are listed in [requirements.txt](https://github.com/BenBamboozled/ToDoList/blob/master/requirements.txt)

### Setup
After python is installed on your machine you can install virtual env
```
python3 -m pip install --user virtualenv
```
Create a new directory for the project and create a virtual environment
```
python3 -m venv env
```
Now you can clone the git in the new directory
```
git clone https://github.com/BenBamboozled/ToDoList.git
```
**NOTE**: If using a virtualenv make sure it is in the .gitignore file

Now activate the virtualenv
```
source env/bin/activate
```
Once the environment is active you can install all other requirements through
```
pip install -r requirements.txt
```
## Deployment
-Ubuntu Server , I used a VPS but you could use a local server for a local list
-[Gunicorn](https://gunicorn.org/) used for wsgi / http server
-[Nginx](https://www.nginx.com/) used to proxy pass to gunicorn
-Postgres Database

**NOTE**:A SQLite database is used If debug is set to true in settings.py, else it will use postgres in production
**NOTE**: You will also need to create a config file with secretkeys. In settings.py for obvious reasons the config file is not included this git.

Deployement will vary depending on tools used, but for my setup the documentation on [DigitalOcean]() helped me a ton!










