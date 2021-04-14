from flask import Flask, request, render_template # Importing the Flask Library/App
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

    link = "https://discord.com/api/webhooks/831442036930510848/2db9BqwlymYOQOTIEemUtMytaLnnZkmLTMyRhTR4eX0SLOdnyhdUb_2AhfK-8Ju_wsBx" # creating a seperate variable for the webhook link 
 
    webhook = DiscordWebhook(url=link, content=data) # defining the webhook using the discord_webhook library, link variable and data variable

    response = webhook.execute() # executing the webhook with message and url

    print(response)
    
  return render_template("theysentdata.html")  # returning some feedback to the user after they submit the data
    
@app.route('/minecraft', methods=["POST"]) # Defining where our site will run if someone sends a post request
def do():  # Function for when a post request is sent
  if request.method == "POST":   
    print("Someone wants to play Minecraft!") # logging "someone wants to play minecraft" in the console
    mojanguser = request.form['mojanguser'] # requesting data input in the form asking for mojang username

    discorduser = request.form['discorduser'] # requesting data input in the form asking for discord username

    emaillphs = request.form['email2'] # requesting data input in the form asking for LPHS email address
    
    data2 = mojanguser + ", " + discorduser + ", " + emaillphs + ", "  # adding all of the data together to one variable called data, called data2 because i didnt want confusion between the two separate app routes
 
    print(data2) # printing variable data to the console for easy testing and debugging

    link = "https://discord.com/api/webhooks/831442441713483797/MDxhAibBKx6PJ1ggAxgrHz8qfXsCgfipkCUd-ywDpsdicW0I7qB8tqGmJlF7oHY8Vyc0" # creating a seperate variable for the webhook link 
 
    webhook = DiscordWebhook(url=link, content=data2) # defining the webhook using the discord_webhook library, link variable and data variable

    response = webhook.execute() # executing the webhook with message and url

    print(response)
    
  return render_template("theysentdata.html")  # returning some feedback to the user after they submit the data

@app.route('/') # Defining where our site will run by default
def home():
  return "You're not meant to be here"

if __name__ == "__main__": # Makes sure this is the main process
  app.run( # Start the site
    host='0.0.0.0', # Establishes the host, this is required for repl to detect the site
    port=random.randint(2000,9000) # Randomly select the port the site is hosted on
  )