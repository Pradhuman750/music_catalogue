# music_catalogue

The music_catalogue is responsible to create Artist,Album,Track and Playlist.


### Steps to install and run order services on your local machine
* Run `$ pip install virtualenv` command to install virtual environment
* Run `$ virtualenv env -p python3` command to Create Virtual environment
* Run `$ source env/bin/activate` command to activate virtual environment
* Run `$ git clone https://github.com/Pradhuman750/music_catalogue.git` command for cloning the project
* Run `$ cd music_catalogue` command for jump into the project directory
* Run `$ pip install -r requirements.txt` command to Install project requirement file
* Run `$ python manage.py migrate` command to apply migrations on your local machine
* Run `$ python manage.py runserver` command to run project on your local machine
    
### Running the Tests
* Run `$ python3 manage.py test` command for run all test cases