--Создать скрипт user.sql.
--Создать таблицу
--Добавить 5 записей
--Получить всех пользователей с вашим именем
--Получить всех пользователей младше 25
--Получить всех пользователей в возрасте от 15 до 18


CREATE TABLE user (
   id integer primary key autoincrement,
   firstname varchar(255),
   lastname varchar(255),
   age integer
)

INSERT INTO user (firstname, lastname, age)
values ('max', 'ivanov', 25),
('max', 'petrov', 17),
('vasya', 'petrov', 16),
('pyatro', 'petrovich', 20),
('max', 'makar', 23);
