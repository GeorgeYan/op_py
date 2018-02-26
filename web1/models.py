# -*- coding:utf-8 -*-
from sqlalchemy import *
from sqlalchemy import event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import hashlib

password_prefix = "Ad%cvcsadefr^!deaf"

db_config={
        'host':'localhost',
        'user':'root',
        'passwd':'',
        'db':'test_python',
        'charset':'utf8'
        }

engine = create_engine('mysql://%s:%s@%s/%s?charset=%s'%(db_config['user'],
    db_config['passwd'],
    db_config['host'],
    db_config['db'],
    db_config['charset']),
    echo=True)

def bindSQL():
    return scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.__table_args__ = {'mysql_engine':'InnoDB'}

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)
    email = Column(String(32), unique=True)
    password = Column(String(32))
    superuser = Column(Boolean, default=False)

metadata = Base.metadata

def setPassword(target, value, oldvalue, initiator):
    if value == oldvalue:
        return oldvalue
    return hashlib.md5("%s%s" % (password_prefix, value)).hexdigest()

event.listen(User.password, "set", setPassword, retval=True)

def get_or_create(session, model, **kwargs):
    if "defaults" in kwargs:
        defaults = kwargs["defaults"]
        del kwargs["defaults"]
    else:
        defaults = {}
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance, False
    else:
        kwargs.update(defaults)
        instance = model(**kwargs)
        session.add(instance)
        session.flush()
        session.refresh(instance)
        return instance, True

def initModel():
    metadata.create_all(engine)
    db = bindSQL()
    obj, created = get_or_create(db,User,name="administrator",defaults={
        "email":"test@test.com",
        "password":"123456",
        "superuser":True
        })
    db.commit()
    db.remove()
if __name__ == "__main__":
    initModel()

