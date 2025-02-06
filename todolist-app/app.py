from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# List to store tasks (in-memory)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    if task:  # Ensure task is not empty
        tasks.append(task)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if task_id < len(tasks):  # Ensure task_id is valid
        tasks.pop(task_id)  # Remove task from the list
        print(f'Task list after deletion: {tasks}')  # Debugging line
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
