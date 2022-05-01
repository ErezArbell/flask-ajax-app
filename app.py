from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/add_numbers', methods=['POST'])
def add_numbers():
    try:
        firstnumber = int(request.form['firstnumber'])
        secondnumber = int(request.form['secondnumber'])
    except:
        return jsonify({'error' : 'Bad data!'}), 400
    sum = firstnumber + secondnumber
    return jsonify({'output':'The sum is %d' % sum})

@app.route("/ping", methods=["GET"])
def ping():
    return "pong", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)