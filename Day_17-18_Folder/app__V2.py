from flask import Flask, render_template # Import the Flask class from the flask module

app = Flask(__name__) # Create a Flask Object - Initialise a new flask application

@app.route("/") # When a user visits my app through the route “/”, run the index() function..
def index():
   #return "<h1>Hello, World!</h1>" ### Which returns a h1 HTML element. Why return?
    return render_template("index_V2.html")

@app.route("/page2") ### What is a decorator?
def page2():
   #return "<h1>Hello World From My Second Page</h1>"
    return render_template("page2_V2.html")

@app.route("/page3")
def page3():
    my_name = "Carl"
    return render_template("page3_V2.html", my_name = my_name) ### What is the point of the variable? How would you use this how would you ask the user their name?


if __name__ == "__main__": ### Don't get this logic behind this, where is "__main__"? Or is it because there's no alternative?
    app.run(debug=True, port = 8000)

# Your browser will respond to the Flask app and display the message.
# 127.0.0.1 is localhost - it’s using your computer as a web server for this app.

