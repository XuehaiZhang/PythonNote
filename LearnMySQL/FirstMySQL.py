#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'bpmacmini01'

import mysql.connector

conn = mysql.connector.connect(user='root', password='', database='test')
cursor = conn.cursor()

cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ['2', 'Jobs'])
print(cursor.rowcount)

conn.commit()
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from user where id = %s or %s', ['1', '2'])
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()