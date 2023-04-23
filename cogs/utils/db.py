import mysql.connector

from decouple import config


class DBHandler:
    def __init__(self):
        # Connect to server
        self.connexion = mysql.connector.connect(
            host="senestre-coquecigrues.fr",
            port=3306,
            user=config("db_user"),
            password=config("db_pw"),
            database=config("db_name")
            )
        self.cur = self.connexion.cursor()

    def create_table():
        pass
# # Execute a query
# cur.execute("SELECT CURDATE()")

# # Fetch one result
# row = cur.fetchone()
# print("Current date is: {0}".format(row[0]))

# # Close connection
# cnx.close()