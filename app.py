from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

feedbacks = []

@app.route('/postfeedback', methods = ['POST'])
def rcvfeedback():
    global feedbacks
    if request.is_json:
        data = request.get_json()
        print(f'Recieved Data: {data}')

        data['s.no.'] = len(feedbacks) + 1

        feedbacks.append(data)
        return jsonify({'success': True})
    else:
        print('Request must be JSON.')
        return jsonify({'success': False})

@app.route('/getfeedbacks')
def sendfeed():
    global feedbacks
    return jsonify(feedbacks)

@app.route('/clearfeedbacks')
def clearfeed():
    global feedbacks
    feedbacks = []
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)