--	Создать файл book.sql. Создать таблицу Book. Атрибуты:
--	id(integer primary key autoincrement),
--	title(varchar), pages(int),
--	author(varchar), price(float)

CREATE TABLE Book (
	id integer primary key autoincrement,
	title varchar,
	pages int,
	author varchar,
	price float

);

ALTER TABLE book ADD COLUMN release_year int;

INSERT INTO Book (title, pages, author, price, release_year)
values ('master', 380, 'Bulgakov', 25, 1965)
('harry', 600, 'Rolling', 35, 2001),
('skot', 300, 'Oryel', 30, 1956),
('norvegian wood', 200, 'murakami', 40, 1995),
('dva kapitana', 500, 'kaverin', 20, 1955)

select release_year, title, price FROM Book;

select title, release_year,price FROM Book
WHERE release_year = 2001;

UPDATE Book set price = 10
WHERE release_year = 2001;

DELETE FROM Book WHERE price >=35;
