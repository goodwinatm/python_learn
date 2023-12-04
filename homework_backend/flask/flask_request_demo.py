from flask import Flask, request, jsonify, Blueprint


#使用blueprint
json2 = Blueprint('json2',__name__)

# @app.route("/user",methods=["post"])
# def creat_user():
#     print(request.args)
#     print(request.args.get("id"))
#     print(request.json)
#     return f"Hello, World!"



@json2.route("/json2",methods=["post","get"])
def creat_fetch_json():
    if request.method=="GET":
        # print(request.args.get("id"))
        return {"name":"ad","age":"18"}
    elif request.method=="POST":
    #print(request.args)
    #print(request.args.get("id"))
        print(request.form)
        return "<p>Hello,post</p>"
# @app.route("/json2",methods=["get"])
# def creat_fetch_json2():
#     if request.method=="GET":
#         # print(request.args.get("id"))
#         return jsonify(name="yan",age="18")
#
