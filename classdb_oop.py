#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

class Database():
    """docstring for ."""

    def __init__(self, db):
        # super(, self).__init__()
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS coursesdb4(id INTEGER PRIMARY KEY,firstName TEXT, lastName TEXT, age INTEGER);''')
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM coursesdb4")
        rows = self.cur.fetchall()
        return rows

    def insert(self, firstName, lastName, age):
        self.cur.execute('''INSERT INTO coursesdb4 VALUES (NULL, ?, ?, ?)''', (firstName, lastName, age))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


db = Database('courses.db')
# db.insert("jour", "nal", 20)
# db.insert("de", "main", 30)
# db.insert("se", "maine", 40)
