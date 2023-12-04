from flask import request, Blueprint


#使用蓝图
user = Blueprint('user',__name__,url_prefix="/user")
@user.route("/user",methods=["post","get"])
def creat_fetch_user():
    if request.method=="GET":
        print(request.args.get("id"))
        return "<p>Hello,get</p>"
    elif request.method=="POST":
    #print(request.args)
    #print(request.args.get("id"))
        print(request.form)
        return "<p>Hello,post</p>"