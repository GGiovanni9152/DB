import psycopg2

# Параметры подключения
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database= "postgres",
    user= "postgres",
    password= 123456
)

# Чтение SQL-файлов
with open("migrations/ddl.sql", "r", encoding="utf-8") as ddl_file, open("migrations/dml.sql", "r",encoding="utf-8") as dml_file:
    ddl_sql = ddl_file.read()
    dml_sql = dml_file.read()

# Выполнение SQL
try:
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(ddl_sql)
            cursor.execute(dml_sql)
    print("Инициализация завершена успешно!")
except Exception as e:
    print(f"Ошибка инициализации: {e}")
finally:
    conn.close()
