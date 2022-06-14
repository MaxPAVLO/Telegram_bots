import psycopg2

conn = None
cur = None

try:
	conn = psycopg2.connect(
		host = "localhost",
		dbname = "demo",
		user = "postgres",
		password = 256809,
		port = 5433)

	cur = conn.cursor()

	insert_script = "INSERT INTO vapes VALUES(%s, %s, %s, %s)"
	insert_value = ("Pipe", "Кокосовый", 1500, 1000)

	cur.execute(insert_script, insert_value)

	conn.commit()

finally:
	if cur is not None:
		cur.close()

	if conn is not None:
		conn.close()