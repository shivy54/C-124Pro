from flask import Flask,jsonify,request

app = Flask(__name__)
tasks = [{
    'Contact':9943366877,
    'Name':'Raju',
    'done':'False',
    'id':1
},
{
    'Contact':9877346547',
    'Name':'Kaju',
    'done':'False',
    'id':2
}]

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please give data"
        },400)
    task = {
        'Contact':tasks[-1]['id']+1,
        'Name':request.json['title'],
        'done':request.json.get('description',""),
        'id':False
    }
    tasks.append(task)
    return jsonify({
        "success":"success",
        "message":"Done"
    })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })
if (__name__=="__main__"):
    app.run(debug=True)
