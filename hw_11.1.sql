test=# create database movies;
CREATE DATABASE
test=# \c movies
Ви тепер під'єднані до бази даних "movies" як користувач "postgres".
movies=# CREATE TABLE actors (actor_id SERIAL, name VARCHAR(255) NOT NULL);
CREATE TABLE
movies=# CREATE TABLE directors (director_id SERIAL, name VARCHAR(255) NOT NULL);
CREATE TABLE
movies=# CREATE TABLE movies (movie_id SERIAL, title VARCHAR(255) NOT NULL);
CREATE TABLE
movies=# INSERT INTO actors (name) VALUES
movies-#     ('Robert Downey Jr.'),
movies-#     ('Chris Evans'),
movies-#     ('Scarlett Johansson'),
movies-#     ('Chris Hemsworth'),
movies-#     ('Mark Ruffalo');
INSERT 0 5
movies=# INSERT INTO directors (name) VALUES
movies-#     ('Jon Favreau'),
movies-#     ('Joss Whedon'),
movies-#     ('Russo brothers'),
movies-#     ('Taika Waititi');
INSERT 0 4
movies=# INSERT INTO movies (title) VALUES
movies-#     ('Iron Man'),
movies-#     ('The Avengers'),
movies-#     ('Thor: Ragnarok'),
movies-#     ('Black Panther'),
movies-#     ('Avengers: Endgame');
INSERT 0 5
movies=# select * from actors;
 actor_id |        name
----------+--------------------
        1 | Robert Downey Jr.
        2 | Chris Evans
        3 | Scarlett Johansson
        4 | Chris Hemsworth
        5 | Mark Ruffalo
(5 рядків)


movies=# select * from directors;
 director_id |      name
-------------+----------------
           1 | Jon Favreau
           2 | Joss Whedon
           3 | Russo brothers
           4 | Taika Waititi
(4 рядки)


movies=# select * from movies;
 movie_id |       title
----------+-------------------
        1 | Iron Man
        2 | The Avengers
        3 | Thor: Ragnarok
        4 | Black Panther
        5 | Avengers: Endgame
(5 рядків)