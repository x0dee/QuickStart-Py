from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample in-memory database
todos = [
    {"id": 1, "text": "Sample Task", "complete": False}
]

@app.route('/')
def index():
    incomplete = [todo for todo in todos if not todo["complete"]]
    complete = [todo for todo in todos if todo["complete"]]
    return render_template("index.html", incomplete=incomplete, complete=complete)

@app.route('/add', methods=['POST'])
def add():
    text = request.form.get('todoitem')
    if text:
        todos.append({"id": len(todos) + 1, "text": text, "complete": False})
    return redirect(url_for('index'))

@app.route('/complete/<int:id>')
def complete(id):
    for todo in todos:
        if todo["id"] == id:
            todo["complete"] = True
    return redirect(url_for('index'))
