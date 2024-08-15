import sqlite3

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()
query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'firefox', 'firefox')"
# cursor.execute(query)
# query = "INSERT INTO sys_command VALUES (null,'settings', 'gnome-control-center')"
# cursor.execute(query)
# query = "INSERT INTO sys_command VALUES (null,'terminal', 'gnome-terminal')"
# cursor.execute(query)
# query = "INSERT INTO sys_command VALUES (null,'file explorer', 'nautilus')"
# cursor.execute(query)
# con.commit()

# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)
# query = "INSERT INTO web_command VALUES (null,'youtube', 'https://www.youtube.com/')"
# cursor.execute(query)
# query = "INSERT INTO web_command VALUES (null,'invertis erp', 'http://erp.invertisuniversity.ac.in:81/loginForm.aspx')"
# cursor.execute(query)
# query = "INSERT INTO web_command VALUES (null,'geek for geeks', 'https://www.geeksforgeeks.org/')"
# cursor.execute(query)
# query = "INSERT INTO web_command VALUES (null,'wikipedia', 'https://www.wikipedia.org/')"
# cursor.execute(query)
# query = "INSERT INTO web_command VALUES (null,'w3 schools', 'https://www.w3schools.com/')"
# cursor.execute(query)
# con.commit()