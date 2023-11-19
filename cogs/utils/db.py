import psycopg2

from decouple import config

def handle_list(values):
    if len(values) == 0:
        return f"'{values[0]}'"
    else:
        return "'" + "', '".join(map(str, values)) + "'"

##### TODO : ADD TITLE FIELD TO BOOK
class DBHandler:
    def __init__(self, conn=0, cur=0):
        self.conn = conn
        self.cur = cur

    def db_decorator(func):
        def wrapper(self, *args, **kwargs):
            self.conn = psycopg2.connect(config("DATABASE_URL"))
            self.cur = self.conn.cursor()
            func(self, *args)
            self.cur.close()
            self.conn.close()

        return wrapper

    @db_decorator
    def create_tables(self):
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS rare_words (
                id INT GENERATED ALWAYS AS IDENTITY,
                word VARCHAR(100) NOT NULL UNIQUE
            );
            """
        )
        self.conn.commit()

        # LUCILE
        self.cur.execute(
            """
            DROP TABLE IF EXISTS sprints;
            """
        )
        self.conn.commit()

        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS sprints (
                id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                serveur_id VARCHAR(100) NOT NULL UNIQUE,
                status INT,
                time_end TIMESTAMP NOT NULL
            );
            """
        )
        self.conn.commit()

        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS participants (
                id INT GENERATED ALWAYS AS IDENTITY,
                sprint_id INT NOT NULL,
                starting_words INT,
                ending_words INT,
                FOREIGN KEY (sprint_id)
                    REFERENCES sprints (id)
                    ON DELETE CASCADE
            );
            """
        )
        self.conn.commit()

        # self.cur.execute(
        #     """
        #     CREATE TABLE IF NOT EXISTS words_counts (
        #         id SERIAL PRIMARY KEY,
        #         sprint_id VARCHAR(100) NOT NULL UNIQUE,
        #         starting_words INT NOT NULL,
        #         ending_words INT
        #     );
        #     """
        # )
        # self.conn.commit()

    @db_decorator
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
        self.conn.commit()

    @db_decorator
    def fetch_random_word(self):
        self.cur.execute("""
            SELECT * FROM rare_words
            ORDER BY RANDOM()
            LIMIT 1""")
        word = self.cur.fetchone()

        return word

#     def __init__(self):
#         # Connect to server
#         self.connection = mysql.connector.connect(
#             host="senestre-coquecigrues.fr",
#             port=3306,
#             user=config("db_user"),
#             password=config("db_pw"),
#             database=config("db_name")
#             )
#         self.cur = self.connection.cursor()

#     def create_tables(self):
#         self.cur.execute(
#             """
#             CREATE TABLE IF NOT EXISTS rare_words (
#                 id INT AUTO_INCREMENT PRIMARY KEY,
#                 word VARCHAR(100) NOT NULL UNIQUE
#             );
#             """
#         )
#         self.connection.commit()
#         self.cur.execute(
#             """
#             CREATE TABLE IF NOT EXISTS books (
#                 id INT AUTO_INCREMENT PRIMARY KEY,
#                 link VARCHAR(255) NOT NULL UNIQUE
#             );
#             """
#         )
#         self.connection.commit()
#         self.cur.execute(
#             """
#             CREATE TABLE IF NOT EXISTS recs (
#                 id INT AUTO_INCREMENT PRIMARY KEY,
#                 member_id VARCHAR(255) NOT NULL,
#                 book_id INT NOT NULL,
#                 body TEXT(10000) NOT NULL,
#                 rec INT,
#                 FOREIGN KEY (book_id) REFERENCES books(id),
#                 CONSTRAINT UC_a_rec UNIQUE (member_id, book_id)
#             );
#             """
#         )
#         self.connection.commit()
#         self.cur.close()
#         self.connection.close()

#     def fetch_from_table(self, table, column, value, many=None):
#         self.cur.execute(
#             f"""
#             SELECT * FROM {table}
#             WHERE {column} = '{value}';
#             """
#         )

#         if not many:
#             result = self.cur.fetchone()
#         else:
#             result = self.cur.fetchall()

#         self.cur.close()
#         self.connection.close()

#         return result

#     def fetch_all_from_table(self, table):
#         self.cur.execute(
#             f"""
#             SELECT * FROM {table}
#             """
#         )

#         result = self.cur.fetchall()
#         self.cur.close()
#         self.connection.close()

#         return result


temp_loader = DBHandler()
temp_loader.create_tables()
