from flask import Flask
app = Flask(__name__)
@app.route("/demo/<int:user_id>")
def hello_world(user_id):
    return f"Hello, World? user: {user_id}"

if __name__=='__main__':
    app.run()