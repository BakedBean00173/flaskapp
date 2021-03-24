from flask import Flask, request # Importing the Flask Library/App
import requests
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

    data = request.form['stuff'] # requesting the data input in the html form and storing it in data variable
    print(data)

    url = "https://discord.com/api/webhooks/823821827285057576/oS3Y48XrLhjFOQ4H9ZWv4TLtlZoH2V-Lc1hb7clXwOZcPURc_30NHJVJcHDnhMc2dSPG"
    # requests.post(url, data)
    webhook = DiscordWebhook(url, data)
    response = webhook.execute()
    
    return "Thank You For Entering Data"  # returning some feedback to the user after they submit the data
    

@app.route('/') # Defining where our site will run by default
def home():
  return "Hello World"

if __name__ == "__main__": # Makes sure this is the main process
  app.run( # Start the site
    host='0.0.0.0', # Establishes the host, this is required for repl to detect the site
    port=random.randint(2000,9000) # Randomly select the port the site is hosted on
  )