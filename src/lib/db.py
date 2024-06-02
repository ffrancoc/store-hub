# db.py
#
# Copyright 2024 Francisco Curin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from rethinkdb import r


class Database(object):

    def init_db(self):
        r.connect(self.host, self.port).repl()
        databases = r.db_list().run()
        if self.db not in databases:
            r.db_create(self.db).run()

        self.conn = r.connect(host=self.host, port=self.port, db=self.db)

    def init_tables(self):
        system_tables = ['users']
        tables = r.table_list().run(self.conn)

        for table in system_tables:
            if table not in tables:
                r.table_create(table).run(self.conn)

    def save_data(self, table_name: str, document: dict):
        log = r.table(table_name).insert(document).run(self.conn)
        print(f'db_log [save_data]: {log}')


    def retrieve_data(self, table_name: str):
        documents= r.table(table_name).run(self.conn)
        return documents


    def remove_data(self, table_name: str, document_id: int):
        log = r.table(table_name).get(document_id).delete().run(self.conn)
        print(f'db_log [remove_data]: {log}')


    def __init__(self, host: str, port: int, db: str):
        self.conn = None
        self.host = host
        self.port = port
        self.db = db

        self.init_db()
        self.init_tables()        
