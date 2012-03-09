# -*- coding: utf-8 -*-

from repository.db import DB

class ModifyTable(DB):

    def add_field(self):
        self.cursor.execute('delete from js where id>=2849')
        self.cursor.connection.commit()


if __name__=='__main__':
    modify_table = ModifyTable()
    modify_table.add_field()