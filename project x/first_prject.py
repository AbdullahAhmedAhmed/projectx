# Import necessary modules
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Global variable to store the received number
number = 0

# Route to render the HTML page displaying the number
@app.route('/')
def index():
    return render_template('kol.html', number=number)

# API endpoint to get the current number
@app.route('/get_number')
def get_number():
    global number
    return jsonify({'number': number})

# API endpoint to receive user number via POST request
@app.route('/receive_user_number', methods=['POST'])
def receive_user_number():
    global number
    data = request.json
    user_number = data.get('random_number')

    try:
        number = int(user_number)
        print("Updated number:", number)  # Add a print statement to check the updated number
        return "User number received successfully"

    except ValueError:
        return "Invalid input. Please send a valid integer.", 400

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
