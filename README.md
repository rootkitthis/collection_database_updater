# Collection Database Updater
I created this as a way to keep track of all the things I collect such as movies and comic books. 

For a long time I have used an excel file to keep track of all the comic books and movies that I currently own and but was wanting to build something a bit more advanced using python and some other skills that I have been developing over time.  

The basis of this project is to use a python script that takes input from myself based on various factors and updates a database stored on a postgreSQL server that is stored locally on my network. 

# Python Modules Needed

 - psycopg2
	 - Psycopg is the most popular PostgreSQL database adapter for the Python programming language. Its main features are the complete implementation of the Python DB API 2.0 specification and the thread safety (several threads can share the same connection). It was designed for heavily multi-threaded applications that create and destroy lots of cursors and make a large number of concurrent INSERTS or UPDATES.
	 - More information about the module can be found [here](https://psycopg.org/).

 - configparser
	 - This module provides the `ConfigParser`class which implements a basic configuration language which provides a structure similar to what’s found in Microsoft Windows INI files. You can use this to write Python programs which can be customized by end users easily.
	 - More information about this module can be found [here](https://docs.python.org/3/library/configparser.html).

# Installation of Modules

    pip3 install pyscopg2

# The Setup

I created a database.ini file so I can easily manipulate server configurations with minimal python code changes.   


-   **database**: the name of the database we want to connect to.
-   **host**: refers to the database server's IP address or URL.
-   **user**: refers to the name of the PostgreSQL user.
-   **password**: password that matches the PostgreSQL user.
-   **port**: the PostgreSQL server's port number on localhost – default is typically 5432.
