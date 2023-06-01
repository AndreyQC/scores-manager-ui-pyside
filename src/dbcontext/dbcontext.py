import psycopg2
from psycopg2.extras import Json as pgJson

class DBcontext():
    def __init__(self, config):
        self.connectionstring = config.PG_DB_CONNECTION_STRING

    def run_query(self, query):
        conn = psycopg2.connect(self.connectionstring)

        q = conn.cursor()
        q.execute(query)

        res = q.fetchone()
        conn.close()
        return (res)