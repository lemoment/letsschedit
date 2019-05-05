<img src="/documentation/logo_20190419.png" width="128">

# Let's Sched It
A free service which helps you find the best time for a group to meet, conveniently.

## Installation & Setup
To setup the development environment, all required packages must be present.

### [Prerequisite] MariaDB
MariaDB is required to run the RESTful application. Installation varies depending on the system on which you plan on hosting the API server. You can read installation instructions on the [official guide](https://downloads.mariadb.org/mariadb/repositories/#mirror=rackspace). The following methods are known to work:

#### Ubuntu 18.04 LTS
```sh
  $ su -
  $ apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8
  $ add-apt-repository 'deb [arch=amd64,arm64,ppc64el] http://mirror.rackspace.com/mariadb/repo/10.3/ubuntu bionic main'
  $ apt update
  $ apt install mariadb-server
```

#### Arch Linux
```sh
  $ su -
  $ pacman -S mariadb
  $ mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
  $ '/usr/bin/mysql_secure_installation'
  $ systemctl start mariadb.service
  $ systemctl enable mariadb.service
```

#### macOS
You're on your own, but I'm very sorry.

### Dependencies
To install the all required packages, you can simply run `python setup.py`. It will automatically check your system environment and install all the necessary Node.js and Python packages.

**Node.js Requirements:**
* vue
* eslint
* babel
* parcel
* Jquery
* vue-fullcalendar
* axios
* vue-gapi
* moment.js

**Python Requirements:**
* flask
* Flask-RESTful
* python-dotenv
* peewee
* PyMySQL

## Usage
You can start the frontend or backend servers by changing into the appropriate directory and launching the application with the correct program.
* Frontend: `npm run dev`
* Backend: `cd source/api && python app.py`

> Created by Elias Gabriel, Maalvika Bhat, Dieter Brehm, and Riya Aggarwal.
