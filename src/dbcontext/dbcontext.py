import psycopg2
from psycopg2.extras import Json as pgJson

class DBcontext():
    def __init__(self, config):
        self.connectionstring = config.PG_DB_CONNECTION_STRING 

    def run_query(self, query):
        conn = psycopg2.connect(self.connectionstring) #подключаемся к БД через конфиг

        q = conn.cursor() # через курсор мы отправляем запосы к БД 'SELECT', 'UPDATE' and etc
        q.execute(query)

        res = q.fetchone() # одна строка
        conn.close() #закрываем соединение 
        return (res)
    
'''
cursor.fetchone() — вернуть одну строку
cursor.fetchall() — вернуть все строки
cursor.fetchmany(size=10) — вернуть указанное количество строк
'''