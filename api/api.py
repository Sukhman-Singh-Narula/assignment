import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the student data from the JSON file
with open('students.json') as f:
    student_data = json.load(f)

@app.route('/api', methods=['GET'])
def get_marks():
    # Retrieve the names from the query parameters
    names = request.args.getlist('name')

    # Retrieve the marks for the requested students
    marks = [next((student['marks'] for student in student_data if student['name'] == name), "Student not found") for name in names]

    # Return the marks in JSON format
    return jsonify({"marks": marks})

if __name__ == "__main__":
    app.run(debug=True)
