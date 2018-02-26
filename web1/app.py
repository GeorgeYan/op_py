#-*-coding:utf-8-*-
import string
import random
import web
from sqlalchemy.orm import scoped_session, sessionmaker
from models import *
import json

urls = (
        "/", "add",
        "/view", "view"
        )

def load_sqla(handler):
    web.ctx.orm = scoped_session(sessionmaker(bind=engine))
    try:
        return handler()
    except web.HTTPError:
        web.ctx.orm.commit()
        raise
    except:
        web.ctx.orm.rollback()
        raise
    finally:
        web.ctx.orm.commit()

app = web.application(urls, globals())
app.add_processor(load_sqla)

class add:
    def GET(self):
        web.header('Content-type', 'text/html')
        name = "".join(random.choice(string.letters) for i in range(6))
        u = User(name=name, email="test@test1.com", password="123456")
        web.ctx.orm.add(u)
        return "added:" + web.websafe(str(u)) \
                + "<br/>" \
                + '<a href="/view">view all</a>'

class view:
    def GET(self):
        web.header('Content-type', 'text/plain')
        user = web.ctx.orm.query(User).first()
        print user.name
        return "\n".join(map(str, web.ctx.orm.query(User).all()))

if __name__ == "__main__":
    app.run()
