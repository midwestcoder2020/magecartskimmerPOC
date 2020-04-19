from flask import Flask, jsonify,json,redirect,request
app = Flask(__name__)
@app.route('/cc/<data>')
def key(data):
    if data:
        print(str(data))
    return(jsonify({"thanks":"bye"}))
if __name__ == '__main__':
    app.run(debug=True)