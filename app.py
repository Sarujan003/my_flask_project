from flask import Flask, render_template

# Create the Flask app instance
app = Flask(__name__)

# Sample data (in a real app, this would come from a database)
tasks = [
    {"id": 1, "description": "Learn Flask deployment", "done": True},
    {"id": 2, "description": "Set up PythonAnywhere", "done": True},
    {"id": 3, "description": "Celebrate!", "done": False},
]

@app.route('/')
def home():
    """Renders the main page with the to-do list."""
    return render_template('index.html', tasks=tasks)

# This is only for running on your local computer
if __name__ == '__main__':
    app.run(debug=True)