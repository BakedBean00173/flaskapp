from flask import Flask, request # Importing the Flask Library/App
import random  # Importing the random Library
from discord_webhook import DiscordWebhook

app = Flask( # Creating the flask app
  __name__,
  template_folder='templates', # Naming the html file folder 
  static_folder='static' # Naming the directory for static files
)

@app.route('/webhook', methods=["POST"]) # Defining where our site will run if someone sends a post request
def say():  # Function for when a post request is sent
  if request.method == "POST":   
    print("someone sent a post request") # logging "someone sent a post request" in the console
    name = request.form['stuff'] # requesting the data input in the html form and storing it in data variable
    info = request.form['morestuff']
    
    data = name + ", " + info

    print(data)

    link = "https://discord.com/api/webhooks/824475546662600725/O7Ojqokl196NnnR6Hjs_---PEBAH_eEG4621WE6ieGKIpWND9PgW2xFFlEGRtVLx2gJC"

    webhook = DiscordWebhook(url=link, content=data)
    response = webhook.execute()

    # Notifier = dn.notifier(url)
    # Notifier.send(data, print_message=true)
    
  return "Thank You For Entering Data"  # returning some feedback to the user after they submit the data
    

@app.route('/') # Defining where our site will run by default
def home():
  return "Hello World"

if __name__ == "__main__": # Makes sure this is the main process
  app.run( # Start the site
    host='0.0.0.0', # Establishes the host, this is required for repl to detect the site
    port=random.randint(2000,9000) # Randomly select the port the site is hosted on
  )