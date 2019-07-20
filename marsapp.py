from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import pymongo
import scrape_mars

#Create an instance of Flask
app = Flask(__name__)

#Use PyMongo to establish Mongo connection 
conn ='mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.mars_data_db
collection = db.mars_coll

db.mars_data_db.drop()




#Route to render template using the data from Mongo
@app.route("/")
def home():

    mars_scraping = mongo.db.collection.find_one()

    return render_template('mars.html', mars=mars)

# from scrape_mars import mars_scrape

@app.route("/scrape")
def scrape():

    #Run the scrape function 
    mars_data = scrape_mars.scrape_info()

    #Update the mongo database using and upsert = True
    collection.update({"id":1}, {"$set": mars_data}, upsert = True)

    return redirect("/")





if __name__ == "__main__":
    app.run(debug=True)
