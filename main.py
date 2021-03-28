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
    print("Someone wants to join your club!") # logging "someone sent a post request" in the console
    name = request.form['name'] # requesting data input in the form asking for name

    year = request.form['year'] # requesting data input in the form asking for year level

    discordTag = request.form['discordtag'] # requesting data input in the form asking for Discord Tag

    email = request.form['email'] # requesting data input in the form asking for LPHS email address
    
    data = name + ", " + year + ", " + discordTag + ", " + email # adding all of the data together to one variable called data
 
    print(data) # printing variable data to the console for easy testing and debugging

    link = "https://discord.com/api/webhooks/824475546662600725/O7Ojqokl196NnnR6Hjs_---PEBAH_eEG4621WE6ieGKIpWND9PgW2xFFlEGRtVLx2gJC" # creating a seperate variable for the webhook link 
 
    webhook = DiscordWebhook(url=link, content=data) # defining the webhook using the discord_webhook library, link variable and data variable

    response = webhook.execute() # executing the webhook with message and url

    print(response)
    
  return "Thank You For Entering Data"  # returning some feedback to the user after they submit the data
    

@app.route('/') # Defining where our site will run by default
def home():
  return "Hello World"

if __name__ == "__main__": # Makes sure this is the main process
  app.run( # Start the site
    host='0.0.0.0', # Establishes the host, this is required for repl to detect the site
    port=random.randint(2000,9000) # Randomly select the port the site is hosted on
  )