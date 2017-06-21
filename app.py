# -*- coding: utf-8 -*-
import web
from urls import urls
import cgi
import urllib
import urllib2
import json
import subprocess
import smtplib
import email.utils
from email.mime.text import MIMEText

# Maximum input we will accept when REQUEST_METHOD is POST
# 0 ==> unlimited input
#cgi.maxlen = 1 * 1024 * 1024 #10MB

#web.config.debug = False
render = web.template.render('templates/', base='layout')


class home:
    def GET(self):
        return render.home()

class Contact:
    def GET(self):
        return render.contact()

    def POST(self):
        input_data = web.input()
        print "DATA:", input_data

        server = smtplib.SMTP('localhost')
        #server.set_debuglevel('True') #debugging

        msg = MIMEText(input_data.message)
        msg['To'] = email.utils.formataddr(('Recipient', 'soportemorant@gmail.com'))
        #msg['Cc'] = email.utils.formataddr(('Recipient', input_data.email)) 
        msg['From'] = email.utils.formataddr(('Author', 'morant@localhost'))
        msg['Subject'] = "Contacto - Sitio Web Morant"
        try:
            server.sendmail('morant@localhost', 'soportemorant@gmail.com',
                    msg.as_string())
        finally:
            server.quit()
        return "El mensaje se ha enviado con éxito"

class Help:
    def GET(self):
        return render.help()

class Upload:
    upload_id = 0

    def GET(self):
        web.header("Content-Type", "text/html; charset=utf-8")
        return render.upload()

    def POST(self):
        Upload.upload_id += 1
        images = web.input()
        filedir = '/tmp'
        data_string = {"Id": str(Upload.upload_id)}

        for counter, value in enumerate(images, 1):
            filename = "tallo" + str(counter) + "-" + str(Upload.upload_id)
            filepath = filedir + "/" + filename
            with open(filepath, r'w') as f:
                f.write(images[value])
            data_string.update({"Tallo" + str(counter): filepath})
        encoded_args = urllib.urlencode(data_string)
        raise web.seeother('/severity?' + encoded_args)

class Severity:
    def GET(self):
        json_data = json.dumps(web.input())
        url = 'http://127.0.0.1:3030/sever/'
        output = subprocess.check_output(['curl', '-XPOST', url, '-d', str(json_data)])
        #output = '{ "id": "1",\
        #        "porcentaje": "nulo",\
        #        "mensaje":[{\
        #        "medidas": "preventivas",\
        #        "tratamiento": "utilice fungicidas protectantes y practicas\
        #        culturales."\
        #        }]}'
        json_data = json.loads(output)
        #print(json.dumps(json_data, indent=4))
        return render.severity(json_data)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
else:
    app = web.application(urls, globals())
    application = app.wsgifunc()
