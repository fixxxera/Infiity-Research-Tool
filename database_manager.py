import hashlib
import sqlite3
import uuid


class DatabaseManager(object):
    def open_connection(self):
        self.conn = sqlite3.connect('users.db')
        self.c = self.conn.cursor()
        self.c.execute('CREATE TABLE IF NOT EXISTS users(username text NOT NULL UNIQUE, password text NOT NULL)')
        self.c.close()
        self.conn.close()

    def insert_user(self, username, password):
        self.conn = sqlite3.connect('users.db')
        self.c = self.conn.cursor()
        salt = uuid.uuid4().hex
        password = hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
        try:
            self.c.execute("INSERT INTO users(username, password) VALUES (?, ?)", (username, password))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            return True
        except sqlite3.IntegrityError:
            self.conn.commit()
            self.c.close()
            self.conn.close()
            return False

    def login(self, username, password):
        self.conn = sqlite3.connect('users.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT username, password FROM users WHERE username='" + username + "'")
        data = self.c.fetchone()
        if data is None:
            return False
        else:
            saved, salt = data[1].split(':')
            match = (saved == hashlib.sha256(salt.encode() + password.encode()).hexdigest())
            if match:
                return True
            else:
                return False

    def check_accounts(self):
        self.conn = sqlite3.connect('users.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM users")
        data = self.c.fetchall()
        self.conn.commit()
        self.c.close()
        self.conn.close()
        return len(data)

    def get_account(self):
        self.conn = sqlite3.connect('users.db')
        self.c = self.conn.cursor()
        self.c.execute("SELECT * FROM users")
        data = self.c.fetchone()
        self.conn.commit()
        self.c.close()
        self.conn.close()
        return data[0]

    def open_records_connection(self):
        self.conn = sqlite3.connect('records.db')
        self.c = self.conn.cursor()
        self.c.execute('CREATE TABLE IF NOT EXISTS carnival_uk(dest_name text, dest_code text, vessel_id text, '
                       'cruise_id text, cruise_line_name text, brochure_name text, number_of_nights text, '
                       'sail_date real, return_date real, inside_price real, oceanview_price real, balcony_proce '
                       'real, suite_price real, download_date real)')
        self.c.execute('CREATE TABLE IF NOT EXISTS carnival_au(dest_name text, dest_code text, vessel_id text, '
                       'cruise_id text, cruise_line_name text, brochure_name text, number_of_nights text, '
                       'sail_date real, return_date real, inside_price real, oceanview_price real, balcony_proce '
                       'real, suite_price real, download_date real)')
        self.c.execute('CREATE TABLE IF NOT EXISTS costa(dest_name text, dest_code text, vessel_id text, '
                       'cruise_id text, cruise_line_name text, brochure_name text, number_of_nights text, '
                       'sail_date real, return_date real, inside_price real, oceanview_price real, balcony_proce '
                       'real, suite_price real, download_date real)')
        self.c.execute('CREATE TABLE IF NOT EXISTS royal(dest_name text, dest_code text, vessel_id text, '
                       'cruise_id text, cruise_line_name text, brochure_name text, number_of_nights text, '
                       'sail_date real, return_date real, inside_price real, oceanview_price real, balcony_proce '
                       'real, suite_price real, download_date real)')
        self.c.execute('CREATE TABLE IF NOT EXISTS hal(dest_name text, dest_code text, vessel_id text, '
                       'cruise_id text, cruise_line_name text, brochure_name text, number_of_nights text, '
                       'sail_date real, return_date real, inside_price real, oceanview_price real, balcony_proce '
                       'real, suite_price real, download_date real)')
        self.c.execute('CREATE TABLE IF NOT EXISTS celebrity(dest_name text, dest_code text, vessel_id text, '
                       'cruise_id text, cruise_line_name text, brochure_name text, number_of_nights text, '
                       'sail_date real, return_date real, inside_price real, oceanview_price real, balcony_proce '
                       'real, suite_price real, download_date real)')
        self.c.execute('CREATE TABLE IF NOT EXISTS po_au(dest_name text, dest_code text, vessel_id text, '
                       'cruise_id text, cruise_line_name text, brochure_name text, number_of_nights text, '
                       'sail_date real, return_date real, inside_price real, oceanview_price real, balcony_proce '
                       'real, suite_price real, download_date real)')
        self.c.execute('CREATE TABLE IF NOT EXISTS oceania(dest_name text, dest_code text, vessel_id text, '
                       'cruise_id text, cruise_line_name text, brochure_name text, number_of_nights text, '
                       'sail_date real, return_date real, inside_price real, oceanview_price real, balcony_proce '
                       'real, suite_price real, download_date real)')
        self.c.execute('CREATE TABLE IF NOT EXISTS ncl(dest_name text, dest_code text, vessel_id text, '
                       'cruise_id text, cruise_line_name text, brochure_name text, number_of_nights text, '
                       'sail_date real, return_date real, inside_price real, oceanview_price real, balcony_proce '
                       'real, suite_price real, download_date real)')
        self.c.close()
        self.conn.close()

    def add_records(self, sailings):
        if "Carnival Cruise Lines" in sailings[0][5]:
            for sail in sailings:
                print(sail)
