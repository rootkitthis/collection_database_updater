#!/usr/bin/python
import psycopg2
from config import config
#takes input to update movie list
def movie_user_input():
    title = input("Enter Title: ")
    disctype = input("Enter Disc Type: ")
    genre = input("Enter Genre: ")
    movierating = input("Enter Movie Rating: ")
    releaseyear = int(input("Enter Release Year: "))
    return title, disctype, genre, movierating, releaseyear

#takes input to update comicbook list
def comic_user_input():
    title = input("Enter Comic Book Title: ")
    issuenumber = input("Enter Comic Book Issue Number(s): ")
    tradeorsingle = input("Is it a trade or single issue:  ")
    return title, issuenumber, tradeorsingle

#function used to connect to sql and run sql queries to update movie database
def movieconnect(title, disctype, genre, movierating, releaseyear):
    conn = None
    try:
        # reads connection file
        params = config()
        #connection to database
        connect = psycopg2.connect(**params)
          
       #create cursor for entry of query
        cursor = connect.cursor()

        # enters sql query
        sql_query = "INSERT INTO movies (title, disctype, genre, movierating, releaseyear) VALUES (%s, %s, %s, %s, %s)"

        # executes query
        cursor.execute(sql_query, (title, disctype, genre, movierating, releaseyear))

        #saves query and closes connection 
        connect.commit()
        cursor.close()
        connect.close()
        print("Movie Database Updated Successfully!")

    except (Exception, psycopg2.Error) as error:
        print(f"Error: {error}")
        if connect:
            connect.rollback()

#function used to connect to sql and run sql queries to update comic book databse
def comicconnect(title, issuenumber, tradeorsingle):
    conn = None
    try:
        # reads connection file
        params = config()
        #connection to database
        connect = psycopg2.connect(**params)
          
       #create cursor for entry of query
        cursor = connect.cursor()

        # enters sql query
        sql_query = "INSERT INTO comics (title, issuenumber, tradeorsingle) VALUES (%s, %s, %s)"

        # executes query
        cursor.execute(sql_query, (title, issuenumber, tradeorsingle))

        #saves query and closes connection 
        connect.commit()
        cursor.close()
        connect.close()
        print("Comic Book Database Updated Successfully!")

    except (Exception, psycopg2.Error) as error:
        print(f"Error: {error}")
        if connect:
            connect.rollback()

#function to update movie datbase
def movieupdate():
    for _ in range(number_movies):
        title, disctype, genre, movierating, releaseyear = movie_user_input()
        movieconnect(title, disctype, genre, movierating, releaseyear)

#function to update comic book datbase
def comicupdate(number_comics):
    for _ in range(number_comics):
        title, issuenumber, tradeorsingle = comic_user_input()
        comicconnect(title, issuenumber, tradeorsingle)

t = input('Are you adding movies or comics to your collection (Type m for movies or type c for comics.)? ')

if t == "m":
   number_movies = int(input("How many many movies are you adding?"))
   movieupdate()
elif t == "c":
    number_comics = int(input("How many comics are you adding?"))
    comicupdate(number_comics)
else:
    if t != "m" or "c":
        print("Run Program again and Type m for movies or type c for comics.")
