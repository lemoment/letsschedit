<img src="/documentation/logo.svg" width="128">

# Let's Sched It
A free service which helps you find the best time for a group to meet, conveniently.

## Development Dependencies

### Web Server
**Node.js Requirements:**
* vue
* eslint
* babel
* parcel

### RESTful API Server
**Python Requirements:**
* flask
* Flask-RESTful
* python-dotenv
* peewee
* PyMySQL

## Installation & Setup
To setup the development environment, all required packages must be present. To install the all required packages, you can simply run `python setup.py`. It will automatically check your system environment and install all the necessary Node.js and Python packages.

### MariaDB
MariaDB is required to run the RESTful application. Installation varies depending on the system on which you plan on hosting the API server. You can read installation instructions on the [official guide](https://downloads.mariadb.org/mariadb/repositories/#mirror=rackspace). To install it on Arch Linux:

```sh
  $ su -
  $ pacman -S mariadb
  $ mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
  $ '/usr/bin/mysql_secure_installation'
  $ systemctl start mariadb.service
  $ systemctl enable mariadb.service
```

## Usage
You can start the frontend or backend servers by changing into the appropriate directory and launching the application with the correct program.
* Frontend: `npm run dev`
* Backend: `cd source/api && python app.py`

> Created by Elias Gabriel, Maalvika Bhat, Dieter Brehm, and Riya Aggarwal.
