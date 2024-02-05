from flask import Flask, request, jsonify

app = Flask(__name__)

# Allow both GET and POST requests for the /run_script endpoint
@app.route('/run_script', methods=['GET', 'POST'])
def run_script():
    if request.method == 'GET':
        # Path to your Python script
        script_path = './ai2.py'

        try:
            # Run the Python script
            import subprocess
            result = subprocess.run(['python', script_path], capture_output=True, text=True)

            # Check if the script executed successfully
            if result.returncode == 0:
                response_data = {'success': True, 'output': result.stdout}
            else:
                response_data = {'success': False, 'error': result.stderr}

        except Exception as e:
            response_data = {'success': False, 'error': str(e)}

        return jsonify(response_data)

    return jsonify({'error': 'Method Not Allowed'}), 405

if __name__ == '__main__':
    app.run(debug=True)
