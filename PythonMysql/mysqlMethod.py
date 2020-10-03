import mysql.connector 

class sqlConnection:
    def __init__(self, host, port, user, password):
        try:
            self.conn = mysql.connector.connect(
                host = host,
                port = port, 
                user = user,
                password = password
            )
            self.mycursor = self.conn.cursor()
            print("Connected to the database!")
        except:
            print("Connection failed!")
    
    # Overloadin function
    def execute(self, sql, var=None):
        typeArray = sql.split(" ")
        # Define query method
        mode = str(typeArray[0]).lower()
        if var is not None:
            self.mycursor.execute(sql, var)
        else:
            self.mycursor.execute(sql)
        if (mode == "select" or mode == "show"):
            myresult = self.mycursor.fetchall()
            for result in myresult:
                print(result)
            print("Query OK! {} rows in set".format(self.mycursor.rowcount))
        elif (mode == "insert"):
            print("Query OK! {} rows inserted".format(self.mycursor.rowcount))
        elif (mode == "delete"):
            print("Query OK! {} rows deleted".format(self.mycursor.rowcount))
        elif (mode == "update"):
            print("Query OK! {} rows updated".format(self.mycursor.rowcount))
        else:
            print("Query Success!!")
        self.conn.commit()
        # Save change

    def executemany(self, sql, var):
        self.mycursor.executemany(sql, var)
        self.conn.commit()
        print("Query OK! {} rows affected".format(self.mycursor.rowcount))
    
    def closeConnection(self):
        self.conn.close()

# Important!: Notice the statement: conn.commit(). It is required to make the changes, otherwise no changes  are made to the table
        
# conn1 = sqlConnection("192.168.1.36", 3306, "chondan", "68083524chondan")
# conn1.execute("use chondan;")
# # conn1.execute("alter table user AUTO_INCREMENT = 11;")
# # conn1.execute("delete from user where id = 11;")
# conn1.execute("update user set name = 'Milner' where id = 9;")
# conn1.execute("select * from user;")

# --- Insert Multiple value
# sql = "insert into user (name) values (%s)"
# var = [('Messi', ), ('Ronaldo', )]
# conn1.executemany(sql, var)
# -- Important!: In Python, a tuple containing a single value must include a comma.
# -- For example, ('abc') is evaluated as a scalar while ('abc',) is evaluated as a tuple

# --- Prevent SQL Injection
# conn1.execute("select * from user where name like 'x%' or 1 = 1;") # Not safe
# -- When query values are provided by the user, you should escape the values
# -- This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.
# sql = "select * from user where name = 'Mane';"
# name = ('M%', )
