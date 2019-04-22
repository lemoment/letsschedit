#LetsSchedIt

A free service which helps you find the best time for a group to meet, conveniently and automatically.
![Mockup](documentation/Mockups/Desktop-Home-LeavesHalf.png)
Created by Elias Gabriel, Riya Aggarwal, Maalvika Bhat, and Dieter Brehm.


## Installation & Setup

### Web Server

### RESTful API Server

**Python Requirements:**
* flask
* Flask-RESTful
* python-dotenv
* MySQL-python
* peewee

To install the python requirement packages, you can simply run `pip install -r ./source/api/requirements.txt`.

MariaDB is required to run this application. Installation varies depending on the system on which you plan on hosting the backend server. To install it on Arch Linux:

```sh
	$ su -
	$ pacman -S mariadb
	$ mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
	$ '/usr/bin/mysql_secure_installation'
```


#### Backend - Deps  
* Flask  
* requires
* peewee
https://downloads.mariadb.org/mariadb/repositories/#mirror=rackspace

#### Frontend - Deps  
* vue.js
* eslint
* babel
* parcel 

The front end can be setup by running
`cd source/web`, then `npm install`

## Usage
From the project root directory, you must cd into the source directory with `cd ./source`. From there you can start the frontend or backend servers:
* Frontend: `cd source/web && npm run dev`
* Backend: `cd source/api && python app.py`

## Structure
![AR Diagram](documentation/ARDiagram.png)
