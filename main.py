from flask import Flask, request # Importing the Flask Library/App
import random  # Importing the random Library

app = Flask( # Creating the flask app
  __name__,
  template_folder='templates', # Naming the html file folder 
  static_folder='static' # Naming the directory for static files
)

@app.route('/webhook', methods=["POST"]) # Defining where our site will run if someone sends a post request
def say():  # Function for when a post request is sent
  if request.method == "POST":   
    print("someone sent a post request") # logging "someone sent a post request" in the console
    print(request.form['stuff']) # !
    return "aaaaaaa" 

@app.route('/') # Defining where our site will run by default
def home():
  return "Hello World"

if __name__ == "__main__": # Makes sure this is the main process
  app.run( # Start the site
    host='0.0.0.0', # Establishes the host, this is required for repl to detect the site
    port=random.randint(2000,9000) # Randomly select the port the site is hosted on
  )