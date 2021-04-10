
from flask import Flask, jsonify, request
  
app = Flask(__name__)
  
# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
#GET http://127.0.0.1:5000/users?country=india
@app.route('/users', methods = ['GET'])
def home():
    coutry= request.args.get('country')

    data = "hello " ""+coutry
    return jsonify({'message': data})
  
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)