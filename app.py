from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    
    
    reply = 'reply-placeholder'
    
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)