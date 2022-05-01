from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/printname', methods=['POST'])
def printname():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    output = firstname + lastname
    if firstname and lastname:
        return jsonify({'output':'Your Name is ' + output + ', right?'})
    return jsonify({'error' : 'Missing data!'}), 400

@app.route("/ping", methods=["GET"])
def ping():
    return "pong", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)