movies=# create database module;
CREATE DATABASE
movies=# \c module
Ви тепер під'єднані до бази даних "module" як користувач "postgres".
module=# CREATE TABLE users (
module(#     id SERIAL,
module(#     name VARCHAR(255) NOT NULL,
module(#     pwd VARCHAR(255) NOT NULL,
module(#     email VARCHAR(255) NOT NULL,
module(#     gender VARCHAR(255) NOT NULL
module(# );
CREATE TABLE
module=# INSERT INTO users (name, pwd, email, gender) VALUES
module-#     ('Vasya', '21341234qwfsdf', 'mmm@mmail.com', 'm'),
module-#     ('Alex', '21341234', 'mmm@gmail.com', 'm'),
module-#     ('Alexey', 'qq21341234Q', 'alexey@gmail.com', 'm'),
module-#     ('Helen', 'MarryMeeee', 'hell@gmail.com', 'f'),
module-#     ('Jenny', 'SmakeMyb', 'eachup@gmail.com', 'f'),
module-#     ('Lora', 'burn23', 'tpicks@gmail.com', 'f');
INSERT 0 6
module=# select * from users;
 id |  name  |      pwd       |      email       | gender
----+--------+----------------+------------------+--------
  1 | Vasya  | 21341234qwfsdf | mmm@mmail.com    | m
  2 | Alex   | 21341234       | mmm@gmail.com    | m
  3 | Alexey | qq21341234Q    | alexey@gmail.com | m
  4 | Helen  | MarryMeeee     | hell@gmail.com   | f
  5 | Jenny  | SmakeMyb       | eachup@gmail.com | f
  6 | Lora   | burn23         | tpicks@gmail.com | f
(6 рядків)


module=# SELECT
module-#     CONCAT('This is ', name, ', ',
module(#            CASE WHEN gender = 'm' THEN 'he' ELSE 'she' END,
module(#            ' has email ', email) AS info
module-# FROM users;
                     info
-----------------------------------------------
 This is Vasya, he has email mmm@mmail.com
 This is Alex, he has email mmm@gmail.com
 This is Alexey, he has email alexey@gmail.com
 This is Helen, she has email hell@gmail.com
 This is Jenny, she has email eachup@gmail.com
 This is Lora, she has email tpicks@gmail.com
(6 рядків)


module=# SELECT
module-#     CASE gender
module-#         WHEN 'm' THEN 'We have ' || COUNT(*) || ' boys!'
module-#         WHEN 'f' THEN 'We have ' || COUNT(*) || ' girls!'
module-#     END AS "Gender information"
module-# FROM users
module-# GROUP BY gender;
 Gender information
--------------------
 We have 3 boys!
 We have 3 girls!
(2 рядки)


module=# create table word (id serial, word varchar(255), vocabulary_id integer);
CREATE TABLE
module=# create table vocabulary (id serial, name varchar(255), info text);
CREATE TABLE
module=# INSERT INTO vocabulary
module-#        (name)
module-# VALUES
module-#        ('animals'),
module-#        ('school'),
module-#        ('nature'),
module-#        ('human'),
module-#        ('SF');
INSERT 0 5
module=# INSERT INTO word
module-#        (word, vocabulary_id)
module-# VALUES
module-#        ('turtle', 1),
module-#        ('pig', 1),
module-#        ('dog', 1),
module-#        ('cat', 1),
module-#        ('lizard', 1),
module-#        ('cow', 1),
module-#        ('rabbit', 1),
module-#        ('frog', 1),
module-#        ('headgehog', 1),
module-#        ('goat', 1);
INSERT 0 10
module=# INSERT INTO word
module-#        (word, vocabulary_id)
module-# VALUES
module-#        ('desk', 2),
module-#        ('book', 2),
module-#        ('chalk', 2),
module-#        ('pen', 2),
module-#        ('pencil', 2),
module-#        ('copybook', 2),
module-#        ('lesson', 2),
module-#        ('teacher', 2),
module-#        ('pupils', 2),
module-#        ('school', 2);
INSERT 0 10
module=# INSERT INTO word
module-#        (word, vocabulary_id)
module-# VALUES
module-#        ('ray', 3),
module-#        ('thunder', 3),
module-#        ('sun', 3),
module-#        ('field', 3),
module-#        ('hill', 3),
module-#        ('mountain', 3),
module-#        ('river', 3),
module-#        ('forest', 3),
module-#        ('grass', 3),
module-#        ('rain', 3);
INSERT 0 10
module=# INSERT INTO word
module-#        (word, vocabulary_id)
module-# VALUES
module-#        ('hair', 4),
module-#        ('nail', 4),
module-#        ('finger', 4),
module-#        ('eye', 4),
module-#        ('tooth', 4),
module-#        ('knee', 4),
module-#        ('elbow', 4),
module-#        ('leg', 4),
module-#        ('arm', 4),
module-#        ('head', 4);
INSERT 0 10
module=# INSERT INTO word
module-#        (word, vocabulary_id)
module-# VALUES
module-#        ('engine', 5),
module-#        ('steel', 5),
module-#        ('power', 5),
module-#        ('nuclear', 5),
module-#        ('shotgun', 5),
module-#        ('laser', 5),
module-#        ('flight', 5),
module-#        ('energy', 5),
module-#        ('Moon', 5),
module-#        ('splace', 5);
INSERT 0 10
module=# SELECT v.name, COUNT(w.id) AS words
module-# FROM vocabulary v
module-# JOIN word w ON v.id = w.vocabulary_id
module-# GROUP BY v.id, v.name;
  name   | words
---------+-------
 SF      |    10
 human   |    10
 nature  |    10
 school  |    10
 animals |    10
(5 рядків)


module=#