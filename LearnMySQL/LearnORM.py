#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'bpmacmini01'

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

# 创建对象的基类
Base = declarative_base()


# 定义User对象:
class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))


# 初始化数据库连接:
# create_engine()用来初始化数据库连接。SQLAlchemy用一个字符串表示连接信息：
# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:@localhost:3306/test')
# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

session = DBSession()
new_user = User(id='7', name='Bob')
new_user1 = User(id='8', name='Max')
print(new_user.id)

session.add(new_user)
session.commit()
session.close()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
session = DBSession()
user = session.query(User).filter(User.id == '5').one()
print('type:', type(user))
print('name:', user.name)
session.close()


# 外键一对多，多对多的关联的表现方式
class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多
    books = relationship('Book')


class Book(Base):
    __tablename__ = 'book'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey('user.id'))
# 当我们查询一个User对象时，该对象的books属性将返回一个包含若干个Book对象的list。
# ORM框架的作用就是把数据库表的一行记录与一个对象互相做自动转换。
# 正确使用ORM的前提是了解关系数据库的原理。
