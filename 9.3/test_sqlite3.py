#-*-coding:utf-8-*-

import sqlite3


try:
    c = sqlite3.connect('test.db')
    cur = c.cursor()
    # cur.execute('create table user (id varchar(20) primary key ,name varchar(20))')
    # cur.execute('insert into user (id,name) values (\'3\',\'mark\')')
    cur.execute('select * from user where id=?',('1'))
    val = cur.fetchall()
    print(val)
    print(cur.rowcount)
except MemoryError :
    print('hh')
finally:
    cur.close()
    c.commit()
    c.close()


