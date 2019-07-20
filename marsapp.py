from Flask import flask, render_template, redirect 
from flask_pymongo import PyMongo
import pymongo
import scrape_mars

#Create an instance of Flask
app = Flask(__name__)

#Use PyMongo to establish Mongo connection 
conn ='mongodb://localhost:27017'
client = pymongo.MongoClient(conn, ConnectTimeoutMS=30000)

db = client.mars_data_db
collection = mars_data_coll


#Route to render template using the data from Mongo
@app.route("/")
def home():

    mars_scraping = collection.find_one()

    return render_template('mars.html', mars_scraping=mars_scraping)
from scrape_mars import mars_scrape

@app.route("/scrape")
def scrape():

    #Run the scrape function 
    mars_data = scrape_mars.scrape_info()

    #Update the mongo database using and upsert = True
    collection.update({"id":1}, {"$set": mars_data}, upsert = True)

    return redirect("http://localhost:5000/", code=302)





if __name__ == "__main__":
    app.run(debug=True)
