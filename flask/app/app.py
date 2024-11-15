from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def calculate_sum():
    try:
        # Get JSON data from the request
        data = request.get_json()
        
        # Extract the integers from the JSON data
        num1 = data.get('num1')
        num2 = data.get('num2')
        
        # Validate input
        if not isinstance(num1, int) or not isinstance(num2, int):
            return jsonify({'error': 'Both num1 and num2 must be integers'}), 400
        
        # Calculate the sum
        result = num1 + num2
        
        # Return the result as JSON
        return jsonify({'sum': result}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

