import mysql.connector

from decouple import config

def handle_list(values):
    if len(values) == 0:
        return f"'{values[0]}'"
    else:
        return "'" + "', '".join(map(str, values)) + "'"

##### TODO : ADD DECORATOR
##### TODO : ADD TITLE FIELD TO BOOK
class DBHandler:
    def __init__(self):
        # Connect to server
        self.connection = mysql.connector.connect(
            host="senestre-coquecigrues.fr",
            port=3306,
            user=config("db_user"),
            password=config("db_pw"),
            database=config("db_name")
            )
        self.cur = self.connection.cursor()

    def create_tables(self):
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS rare_words (
                id INT AUTO_INCREMENT PRIMARY KEY,
                word VARCHAR(100) NOT NULL UNIQUE
            );
            """
        )
        self.connection.commit()
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS books (
                id INT AUTO_INCREMENT PRIMARY KEY,
                link VARCHAR(255) NOT NULL UNIQUE
            );
            """
        )
        self.connection.commit()
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS recs (
                id INT AUTO_INCREMENT PRIMARY KEY,
                member_id VARCHAR(255) NOT NULL,
                book_id INT NOT NULL,
                body TEXT(10000) NOT NULL,
                rec INT,
                FOREIGN KEY (book_id) REFERENCES books(id),
                CONSTRAINT UC_a_rec UNIQUE (member_id, book_id)
            );
            """
        )
        self.connection.commit()
        self.cur.close()
        self.connection.close()

    def insert_into_table(self, table, values):
        if table == "rare_words":
            fields = "word"
        elif table == "books":
            fields = "link"
        elif table == "recs":
            fields = "member_id, book_id, body, rec"

        self.cur.execute(
            f"INSERT INTO {table}({fields}) VALUES({handle_list(values)})"
        )
        self.connection.commit()
        self.cur.close()
        self.connection.close()

    def fetch_from_table(self, table, column, value, many=None):
        self.cur.execute(
            f"""
            SELECT * FROM {table}
            WHERE {column} = '{value}';
            """
        )

        if not many:
            result = self.cur.fetchone()
        else:
            result = self.cur.fetchall()

        self.cur.close()
        self.connection.close()

        return result

    def fetch_all_from_table(self, table):
        self.cur.execute(
            f"""
            SELECT * FROM {table}
            """
        )

        result = self.cur.fetchall()
        self.cur.close()
        self.connection.close()

        return result

    def fetch_random_word(self):
        self.cur.execute("""
            SELECT * FROM rare_words
            ORDER BY RAND()
            LIMIT 1""")
        word = self.cur.fetchone()
        self.cur.close()
        self.connection.close()

        return word


temp_loader = DBHandler()
temp_loader.create_tables()
