from website import create_app # Importing the create_app function from the website module created

app = create_app() # Calling the create_app function to the app

if __name__ == "__main__": # Checking if the script is run directly
    app.run(debug=True, port=8000) 
    