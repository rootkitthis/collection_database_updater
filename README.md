
# Collection Database Updater
I created this as a way to keep track of all the things I collect such as movies and comic books. 

For a long time I have used an excel file to keep track of all the comic books and movies that I currently own and but was wanting to build something a bit more advanced using python and some other skills that I have been developing over time.  

The basis of this project is to use a python script that takes input from myself based on various factors and updates a database stored on a postgreSQL server that is stored locally on my network. 

# Tools and Environment configuration I am using

 - MacOS
 - Brackets - used to create database.ini
 - Proxmox - used to house postgreSQL server running via CasaOS 
 - Visual Studio Code - Used to create python scripts 

# Python Modules Needed

 - psycopg2
	 - Psycopg is the most popular PostgreSQL database adapter for the Python programming language. Its main features are the complete implementation of the Python DB API 2.0 specification and the thread safety (several threads can share the same connection). It was designed for heavily multi-threaded applications that create and destroy lots of cursors and make a large number of concurrent INSERTS or UPDATES.
	 - More information about the module can be found [here](https://psycopg.org/).

 - configparser
	 - This module provides the `ConfigParser`class which implements a basic configuration language which provides a structure similar to what’s found in Microsoft Windows INI files. You can use this to write Python programs which can be customized by end users easily.
	 - More information about this module can be found [here](https://docs.python.org/3/library/configparser.html).

# Installation of Modules

 - psycopg2
	 - For me I was able to successfully install pyscopg2 by running the following command via Terminal: `pip3 install pyscopg2` or `pip install psycopg2`depending on your OS configuration.
	 - For a more detailed installation process follow steps laid out [here](https://www.psycopg.org/docs/install.html).

 - configparser
	 - For confiparser I didn't need to install any modules but in the event that you need it you can use the following terminal command: `pip3 install configparser` or `pip install configparser`depending on your OS Configuration. 

# PostgreSQL configuration

I cleaned all my current spreadsheets housing my entire movie collection an exported the file as a .csv file.  I then setup a table for movies on my database with the following columns and dat types : 

 - title = text data type
 - disctype = text data type
 - genre = text data type 
 - movierating = text data type 
 - releaseyear = integer data type*

I then imported the .csv file so all my data is viewable via sql. 

# database.ini Setup
I started by using brackets to create a database.ini file.  This file will be used so I can easily manipulate server information without needing to edit any of my python files that uses this file. 

The database.ini file is a simple file that consists of the following information:

-   **database**: the name of the database we want to connect to.
-   **host**: refers to the database server's IP address or URL.
-   **user**: refers to the name of the PostgreSQL user.
-   **password**: password that matches the PostgreSQL user.
-   **port**: the PostgreSQL server's port number on localhost – default is typically 5432.

The final file looked like (*fields are manipulated for security/privacy reasons)*: 

    [postgresql]
    host=192.168.1.25
    port=5432
    database=filler
    user=password1235

I then saved this file in a folder on my desktop. 

# config python script

Reference [this](https://github.com/rootkitthis/collection_database_updater/blob/main/config.py) for the full code. 

This code defines a function called `config` that reads and parses a configuration file (the  'database.ini' file we created) using the `ConfigParser` module. It retrieves configuration parameters from a specified section and returns them as a dictionary. If the specified section is not found in the configuration file, it raises an exception.

I store this file in the same folder as the database.ini file

# collection_database_updater python script
Reference [this](https://github.com/rootkitthis/collection_database_updater/blob/main/collection_database_updater.py) for the full code.

This code appears to be a Python script for updating two different types of databases: one for movies and another for comic books. It uses the `psycopg2` library for connecting to a PostgreSQL database and a separate configuration file (`config.py`) to store database connection parameters. The script takes user input to add entries to either the movie or comic book database, and it provides error handling for database operations. Additionally, it handles invalid user input and prompts the user to try again.
