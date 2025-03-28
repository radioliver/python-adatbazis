import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="mysql"
)

DATABASE = "mydatabase"

mycursor = mydb.cursor()
#adatbázis létrehozása
mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE}")

#adatbázisok lekérése
print("\nAdatbázisok:\n")
mycursor.execute("SHOW DATABASES")
i = 1
for x in mycursor:
  print(f"{i}. {x[0]}")
  i+=1

#atabázis használata
mycursor.execute(f"USE {DATABASE}")

#táblák létrehozása
#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
"""
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record inserted.")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
"""
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

print("\n------------------------------------------\n")
print("Minden:\n")
for x in myresult:
  print(f"{x[0]} {x[1]} ")

print("\n------------------------------------------\n")
print("Név és cím:\n")
mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(f"{x[0]} - {x[1]}")

print("\n------------------------------------------\n")
print("Ahol a cím: Park Lane 38:\n")
sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(f"{x[0]} - {x[1]}")

print("\n------------------------------------------\n")
print("Amelyben benne van a 'way' szó:\n")

sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(f"{x[0]} - {x[1]}")
print("\n------------------------------------------\n")


