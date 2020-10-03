from mysqlMethod import sqlConnection

# --- Create a new connection to the database 
conn1 = sqlConnection("192.168.1.36", 3306, "chondan", "68083524chondan")

# --- Select database
conn1.execute("use chondan;")

# --- Insert Multiple value
# sql = "insert into user (name) values (%s)"
# var = [('Messi', ), ('Ronaldo', )]
# conn1.executemany(sql, var)

# --- Reset AUTO_INCREMENT
# conn1.execute("alter table user AUTO_INCREMENT = 11;")

# --- Select row
# conn1.execute("select * from user;")

# --- Where
# conn1.execute("select * from user where name like 'x%' or 1 = 1;") # Not safe
# sql = "select * from user where name like %s"
# name = ("M%", )
# conn1.execute(sql, name)

# --- Delelete
# conn1.execute("delete from user where name = %s", ('Aguero', ))

# --- Drop Table
# conn1.execute("create table newtable (id INT NOT NULL PRIMARY KEY, age INT, playername VARCHAR(30));")
# conn1.execute("show tables;")
# conn1.execute("drop table newtable;")
# conn1.execute("show tables;")
# -- Drop Only If Exist
# conn1.execute("drop table if exists newtable")

# ---- Limit the Result
# You can limit the number of records returned from the query, by using the 'LIMIT' statement
conn1.execute("select * from user limit 5;")
# -- Start From Another Position
conn1.execute("select * from user limit 5 offset 2;")

# ---- Join
# -- Join two or more tables
# You can combine rows from two or more tables, based on a related column between them, by using a JOIN statement
# conn1.execute("create table customers (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(30), fav INT);")
# conn1.execute("create table products (id INT PRIMARY KEY AUTO_INCREMENT, productName VARCHAR(30));")

# customer = [('John', 1), ('Peter', 2), ('Amy', 2), ('Hannah', None)]
# conn1.executemany("insert into customers (name, fav) values (%s, %s);", customer)
# conn1.execute("select * from customers;")

# product = [(1, "Chocolate Heaven"), (2, "Tasty Lemons"), (3, "Vanilla Dreams")]
# conn1.executemany("insert into products (id, productName) values (%s, %s);", product)
# conn1.execute("select * from products;")

# -- INNER JOIN
conn1.execute("select c.name, p.productName from customers c join products p on c.fav = p.id;")
conn1.execute("select c.name, p.productName from customers c left join products p on c.fav = p.id;")
conn1.execute("select c.name, p.productName from customers c right join products p on c.fav = p.id;")