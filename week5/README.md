## Task 2: Create database and table in your MySQL server
* Create a new database named website.
```
mysql> CREATE DATABASE website;
```
![task2-1](https://github.com/Claire-HS/WeHelp-Stage1/raw/main/week5/screenshot/task2-1.png)

* Create a new table named member, in the website database
```
mysql> CREATE TABLE member(\
    -> id BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT 'Unique ID',\
    -> name VARCHAR(255) NOT NULL COMMENT 'Name',\
    -> username VARCHAR(255) NOT NULL COMMENT 'Username',\
    -> password VARCHAR(255) NOT NULL COMMENT 'Password',\
    -> follower_count INT UNSIGNED NOT NULL DEFAULT 0 COMMENT 'Follower Count',\
    -> time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Signup Time');
```
![task2-2.1](https://github.com/Claire-HS/WeHelp-Stage1/raw/main/week5/screenshot/task2-2.1.png)
![task2-2.2](https://github.com/Claire-HS/WeHelp-Stage1/raw/main/week5/screenshot/task2-2.2.png)

## Task 3: SQL CRUD
* INSERT a new row to the member table where name, username and password must be set to test. INSERT additional 4 rows with arbitrary data.
```
mysql> INSERT INTO member(name, username, password) VALUES('test', 'test', 'test');
mysql> INSERT INTO member(name, username, password, follower_count) VALUES('LingKw', 'Ling', 'LO0511', FLOOR(RAND() * 1000));
mysql> INSERT INTO member(name, username, password, follower_count) VALUES('OrmKn', 'Orm', 'LO0527', FLOOR(RAND() * 1000));
mysql> INSERT INTO member(name, username, password, follower_count) VALUES('JessicaJung', 'Jessica', 'Je0418', FLOOR(RAND() * 1000));
mysql> INSERT INTO member(name, username, password, follower_count) VALUES('TaeriKim', 'Taeri', 'Tr0424', FLOOR(RAND() * 1000));
```
![task3-1](https://github.com/Claire-HS/WeHelp-Stage1/raw/main/week5/screenshot/task3-1.png)

* SELECT all rows from the member table.
```
mysql> SELECT * FROM member;
```
![task3-2](https://github.com/Claire-HS/WeHelp-Stage1/raw/main/week5/screenshot/task3-2.png)

* SELECT all rows from the member table, in descending order of time.
```
mysql> SELECT * FROM member ORDER BY time DESC;
```
![task3-3](https://github.com/Claire-HS/WeHelp-Stage1/raw/main/week5/screenshot/task3-3.png)

* SELECT total 3 rows, second to fourth, from the member table, in descending order of time. Note: it does not mean SELECT rows where id are 2, 3, or 4.
```
mysql> SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;
```
![task3-4](https://github.com/Claire-HS/WeHelp-Stage1/raw/main/week5/screenshot/task3-4.png)

* SELECT rows where username equals to test.
```
mysql> SELECT * FROM member WHERE username = 'test';
```
![task3-5](https://github.com/Claire-HS/WeHelp-Stage1/raw/main/week5/screenshot/task3-5.png)

* SELECT rows where name includes the es keyword.
```
mysql> SELECT * FROM member WHERE name LIKE '%es%';
```
![task3-6](https://github.com/Claire-HS/WeHelp-Stage1/raw/main/week5/screenshot/task3-6.png)

* SELECT rows where both username and password equal to test.
```
mysql> SELECT * FROM member WHERE username = 'test' AND password = 'test';
```
![task3-7](https://github.com/Claire-HS/WeHelp-Stage1/raw/main/week5/screenshot/task3-7.png)

* UPDATE data in name column to test2 where username equals to test.
```
mysql> UPDATE member SET name = 'test2' WHERE username = 'test';
```
![task3-8](https://github.com/Claire-HS/WeHelp-Stage1/raw/main/week5/screenshot/task3-8.png)

## Task 4: SQL Aggregation Functions
* SELECT how many rows from the member table.
```
mysql> SELECT COUNT(*) FROM member;
```
![task4-1](https://github.com/Claire-HS/WeHelp-Stage1/raw/main/week5/screenshot/task4-1.png)

* SELECT the sum of follower_count of all the rows from the member table.
```
mysql> SELECT SUM(follower_count) FROM member;
```
![task4-2](https://github.com/Claire-HS/WeHelp-Stage1/raw/main/week5/screenshot/task4-2.png)

* SELECT the average of follower_count of all the rows from the member table.
```
mysql> SELECT AVG(follower_count) FROM member;
```
![task4-3](https://github.com/Claire-HS/WeHelp-Stage1/raw/main/week5/screenshot/task4-3.png)

* SELECT the average of follower_count of the first 2 rows, in descending order offollower_count, from the member table.
```
mysql> SELECT AVG(follower_count) FROM (SELECT follower_count FROM member ORDER BY follower_count DESC LIMIT 2) AS top_2_followers;
```
![task4-4](https://github.com/Claire-HS/WeHelp-Stage1/raw/main/week5/screenshot/task4-4.png)

## Task 5: SQL JOIN
* Create a new table named message, in the website database. 
```
mysql> CREATE TABLE message(\
    -> id BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT 'Unique ID',\
    -> member_id BIGINT NOT NULL COMMENT 'Member ID for Message Sender',\
    -> content VARCHAR(255) NOT NULL COMMENT 'Content',\
    -> like_count INT UNSIGNED NOT NULL DEFAULT 0 COMMENT 'Like Count',\
    -> time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Publish Time',\
    -> FOREIGN KEY(member_id) REFERENCES member(id));
```
![task5-1](https://github.com/Claire-HS/WeHelp-Stage1/raw/main/week5/screenshot/task5-1.png)

* SELECT all messages, including sender names. We have to JOIN the member table to get that.
```
mysql> SELECT message.id, message.content, message.like_count, message.time, member.name AS sender_name FROM message\
    -> LEFT JOIN member ON message.member_id = member.id\
    -> ORDER BY message.time DESC;
```
![task5-2](https://github.com/Claire-HS/WeHelp-Stage1/raw/main/week5/screenshot/task5-2.png)

* SELECT all messages, including sender names, where sender username equals to test. We have to JOIN the member table to filter and get that.
```
mysql> SELECT message.id, message.content, message.like_count, message.time, member.name AS sender_name, member.username AS sender_username FROM message\
    -> INNER JOIN member ON message.member_id = member.id\
    -> WHERE member.username = 'test'\
    -> ORDER BY message.time DESC;
```
![task5-3](https://github.com/Claire-HS/WeHelp-Stage1/raw/main/week5/screenshot/task5-3.png)

* Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages where sender username equals to test.
```
mysql> SELECT member.username, AVG(message.like_count) AS average_like_count FROM message\
    -> INNER JOIN member ON message.member_id = member.id\
    -> WHERE member.username = 'test';
```
![task5-4](https://github.com/Claire-HS/WeHelp-Stage1/raw/main/week5/screenshot/task5-4.png)

* Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages GROUP BY sender username.
```
mysql> SELECT member.username, AVG(message.like_count) AS average_like_count FROM message\
    -> INNER JOIN member ON message.member_id = member.id\
    -> GROUP BY member.username;
```
![task5-5](https://github.com/Claire-HS/WeHelp-Stage1/raw/main/week5/screenshot/task5-5.png)
