from flask import Flask

from homework_backend.flask.flask_request_demo import json2
from homework_backend.flask.testcase import user

app=Flask(__name__)
#注册blueprint
app.register_blueprint(json2)
app.register_blueprint(user)

if __name__=='__main__':
    app.run(host="0.0.0.0",port=5002,debug=True)