import pyodbc

# Definir la cadena de conexión
connection_string = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=KENEN;'
    'DATABASE=kenay_db;'
    'UID=hp;'
    'PWD=123'
)

# Establecer la conexión
try:
    conn = pyodbc.connect(connection_string)
    print("Conexión establecida con éxito.")
except pyodbc.Error as e:
    print("Error al conectar a la base de datos:", e)
