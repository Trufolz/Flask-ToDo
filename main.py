from flask import Flask, render_template, request, redirect, url_for
from models.todo import Todo
from models.data_manager import create_table_query, delete_query


create_table_query()

app = Flask(__name__)


@app.route("/")
def list():
    """
    Shows list of todo items stored in the database.
    """
    all_todos = Todo.get_all()

    return render_template("index.html", all_todos=all_todos)


@app.route("/add", methods=['GET', 'POST'])
def add():
    """ Creates new todo item
    If the method was GET it should show new item form.
    If the method was POST it should create and save new todo item.
    """
    if request.method == "GET":

        return render_template("add.html")

    if request.method == "POST":
        id = ''
        name = request.form["name"]
        status = request.form.get("status")
        if status == None:
            new_todo = Todo(id, name, 0)
            Todo.add(new_todo)
        elif status == "on":
            new_todo = Todo(id, name, 1)
            Todo.add(new_todo)

        return redirect(url_for('list'))


@app.route("/remove/<todo_id>")
def remove(todo_id):
    """
    Removes todo item with selected id from the database
    """
    delete_query(todo_id)

    return redirect(url_for('list'))


@app.route("/edit/<todo_id>", methods=['GET', 'POST'])
def edit(todo_id):
    """
    Edits todo item with selected id in the database
    If the method was GET it should show todo item form.
    If the method was POST it should update todo item in database.
    """
    if request.method == "GET":
        todo_to_edit = Todo.get_by_id(todo_id)
        return render_template("edit.html", todo_to_edit=todo_to_edit)

    elif request.method == "POST":
        edited_name = request.form["name"]
        edited_status = request.form.get("status")

        if edited_status == None:
            edited_todo = Todo(todo_id, edited_name, 0)
            Todo.edit(edited_todo)
        elif edited_status == "on":
            edited_todo = Todo(todo_id, edited_name, 1)
            Todo.edit(edited_todo)

        return redirect(url_for("list"))


@app.route("/toggle/<todo_id>")
def toggle(todo_id):
    """ Toggles the state of todo item """
    toggled_todo = Todo.get_by_id(todo_id)
    Todo.toggle(toggled_todo)
    return redirect(url_for("list"))


if __name__ == "__main__":
    app.run(debug=True)
