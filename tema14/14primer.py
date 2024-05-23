import sqlite3

connection = sqlite3.connect("my_database.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Users ( 
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
""")
connection.commit()

cursor.execute("CREATE INDEX idx_email ON Users (email)")
connection.commit()

cursor.execute("INSERT INTO Users(username, email, age) VALUES (?, ?, ?)", ("newuser", "newuser@exaple.com", 28))
connection.commit()

cursor.execute("UPDATE Users SET age = ? WHERE username = ?", (29,"newuser"))
connection.commit()

cursor.execute("DELETE FROM Users WHERE Username = ?", ("newuser",))
connection.commit()

cursor.execute("SELECT * FROM Users")
users = cursor.fetchall()
for user in users:
    print(user)

cursor.execute("SELECT Username, age FROM Users WHERE age > ?",  (25,))
results = cursor.fetchall()

for row in results:
    print(row)

cursor.execute("SELECT age, AVG(age) FROM Users GROUP BY age")
result = cursor.fetchall()

cursor.execute("SELECT age, AVG(age) FROM Users GROUP BY age HAVING AVG(age) > 7", (30,))
filtered_results = cursor.fetchall()
for row in filtered_results:
    print(row)

cursor.execute("SELECT username, age FROM Users ORDER BY age DESC")
results = cursor.fetchall()

for row in result:
    print(row)

cursor.execute("""
SELECT username, age, AVG(age)
From Users
GROUP BY age
HAVING AVG(age)> ?
ORGER BY age DEC
""", (30,))
results = cursor.fetchall()

for row in results:
    print(row)

cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchall()[0]

print("Общее количество пользователей:", total_users)


cursor.execute("SELECT SUM(age) FROM Users")
total_age = cursor.fetchall()[0]

print("общая сумма возрастов пользователей:", total_age)

cursor.execute("SELECT AVG(age) FROM Users")
average_age = cursor.fetchall()[0]

print("средний возраст пользователей:", average_age)

cursor.execute("SELECT MIN(age) FROM Users")
min_age = cursor.fetchall()
print("минимальный возраст", min_age)

cursor.execute("SELECT MAX(age) FROM Users")
max_age = cursor.fetchall()
print("максимальный возраст",max_age)

cursor.execute("""
SELECT username, age
FROM Users
WHERE age = (SELECT MAX(age) FROM Users)
""")
oldest_users = cursor.fetchall()

for user in oldest_users:
    print(user)

cursor.execute("SELECT * FROM Users")
users = cursor.fetchall()

for user in users:
    print(user)

cursor.execute("SELECT * FROM Users")
first_user = cursor.fetchall()
print(first_user)

cursor.execute("SELECT * FROM Users")
first_five_users = cursor.fetchmany(5)
print(first_five_users)

cursor.execute("SELECT * FROM Users")
all_users = cursor.fetchall()
print(all_users)

cursor.execute("SELECT * FROM Users")
cursor = connection.cursor()

user_list = []
for user in users:
    user_dict = {
        "id":user[0],
        "username": user[1],
        "email": user[2],
        "age": user[3]
    }
user_list.append(user_dict)

for user in user_list:
    print(user)

cursor.execute("SELECT * FROM Users WHERE age IS NULL")
unknown_age_users = cursor.fetchall()

for user in unknown_age_users:
    print(user)

try:
    cursor.execute("BEGIN")

    cursor.execute("INSERT INTO Users (username, email) VALUES(?, ?)", ("user1", "user1@example.com"))
    cursor.execute("INSERT INTO Users (username, email) VALUES(?, ?)", ("user2", "user2@example.com"))

    cursor.execute("COMMIT")

except:

    cursor.execute("ROLLBACK")

query = "SELECT * FROM Users WHERE age > ?"
cursor.execute(query, (25,))
users = cursor.fetchall()

for user in users:
    print(user)

cursor.execute("CREATE VIEW ActivUsers AS SELECT * FROM Users WHERE is_active = 1")

cursor.execute("SELECT * FROM ActiveUsers")
active_users = cursor.fetchall()

for user in active_users:
    print(user)

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

cursor.execute("""
CREATE TRIGGER IN NOT EXISTS update_created_at
AFTER INSERT ON Users
BEGIN
UPDATE Users SET created_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
END;
""")




connection.close()

