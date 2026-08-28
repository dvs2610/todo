from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
tasks = []
display_finished_tasks = True

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		task = request.form.get('task', '').strip()
		if task:
			tasks.append({'description': task, 'finished': False})
		return redirect(url_for('index'))

	return render_template('index.html', tasks=tasks, display_finished_tasks=display_finished_tasks)

@app.route('/task', methods=['POST'])
def manage_task():
	task_index = request.form.get('task_index', type=int)
	action = request.form.get('action')

	if task_index is not None and 0 <= task_index < len(tasks):
		if action == 'done':
			tasks[task_index]['finished'] = True
		elif action == 'undone':
			tasks[task_index]['finished'] = False
		elif action == 'delete':
			tasks.pop(task_index)

	return redirect(url_for('index'))

@app.route('/toggle-finished')
def toggle_finished():
	global display_finished_tasks
	display_finished_tasks = not display_finished_tasks
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(debug=True)