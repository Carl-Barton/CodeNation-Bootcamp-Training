from flask import Flask, Blueprint, render_template, request, redirect, url_for   #Importing every module needed for this part of the app to work
from .models import Todo
from . import db

my_view = Blueprint("my_view",__name__)

@my_view.route("/")
def home():
    todo_list = Todo.query.all()
    message = request.args.get('message', None)
    return render_template("index.html" , todo_list = todo_list, message = message)

@my_view.route("/add", methods = ["POST"])
def add():
    try:
        task = request.form.get("task")
        new_todo = Todo(task=task)
        db.session.add(new_todo)
        db.session.commit()
        message = "Task Successfully Added."
        return redirect(url_for("my_view.home", message = message))
    except:
        message = "There was an error adding your task. Please try again."
        return redirect(url_for("my_view.home", message = message))

@my_view.route("/update/<todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("my_view.home"))

@my_view.route("/delete/<todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("my_view.home"))

@my_view.route("/edit/<int:todo_id>",methods=["GET","POST"])    #ChatGPT helped with the "message2" variable and the duplicate task section of this code, the rest is from the presentation guide of creating an "edit" route
def edit(todo_id):
    todo = Todo.query.get(todo_id)
    message2 = None #Message variable                                                  
    if request.method == "POST":
        new_task = request.form.get("task")
        if new_task:
            duplicate_task = Todo.query.filter(Todo.task == new_task, Todo.id != todo_id).first()
          
            if duplicate_task:
                message2 = "This task already exists. Please enter a different task."
            else:    
                todo.task = new_task
                db.session.commit()
                return redirect(url_for("my_view.home"))
            
    return render_template("edit.html", todo = todo, message2 = message2)   