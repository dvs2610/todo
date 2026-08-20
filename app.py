from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		task = request.form.get('task', '').strip()
		if task:
			tasks.append({'text': task, 'finished': False})
		return redirect(url_for('index'))

	return render_template('index.html', tasks=tasks)

@app.post('/task/<int:task_index>/handle')
def handle_task(task_index):
	if 0 <= task_index < len(tasks):
		action = request.form.get('action')
		if action == 'delete':
			tasks.pop(task_index)
		elif action == 'toggle':
			tasks[task_index]['finished'] = not tasks[task_index]['finished']
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(debug=True)