#-*-coding:utf-8-*-
import web
web.config.debug = True
urls = (
    "/","index"
)
app = web.application(urls, locals())
#render = web.template.render('templates', globals)
render = web.template.render('templates/')
class index:
    def GET(self):
        return render.index('lalala')
if __name__ == "__main__":
    app.run()
