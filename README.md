﻿# Mission to Mars

I completed this project during my time at the [Columbia Engineering Data Analytics Bootcamp](https://bootcamp.cvn.columbia.edu/data/nyc/landing/?s=Google-Brand&pkw=%2Bdata%20%2Banalytics%20%2Bcolumbia&pcrid=392444639754&pmt=b&utm_source=google&utm_medium=cpc&utm_campaign=%5BS%5D_GRD_Data_Brand_ALL_NYC_BMM_New&utm_term=%2Bdata%20%2Banalytics%20%2Bcolumbia&utm_content=392444639754&s=google&k=%2Bdata%20%2Banalytics%20%2Bcolumbia&gclid=Cj0KCQiA2b7uBRDsARIsAEE9XpFH-2wU0-_7jtxCV_PCkGBR0prlyKtvpF2-nAWU1tO4oYci5h1QStsaAsg5EALw_wcB&gclsrc=aw.ds) located in New York, NY.

#### -- Project Status: [Completed]

![mission_to_mars](Instructions/Images/mission_to_mars.png)

The purpose of this project is to build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 

The final project includes the following:

### * A Jupyter Notebook file called `mission_to_mars.ipynb` that scrapes the following:

#### NASA Mars News

* [NASA Mars News Site](https://mars.nasa.gov/news/) for the latest News Title and Paragraph Text. 

```python
# Example:
news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"

news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."
```

#### JPL Mars Space Images - Featured Image

* [JPL Featured Space Image](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars) by navigating the site, finding the image url for the current Featured Mars Image and assigning the url string to a variable called `featured_image_url`.



```python
# Example:
featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'
```

#### Mars Weather

* The latest Mars weather tweet on the [Mars Weather twitter account](https://twitter.com/marswxreport?lang=en) and saved as a variable called `mars_weather`.

```python
# Example:
mars_weather = 'Sol 1801 (Aug 30, 2017), Sunny, high -21C/-5F, low -80C/-112F, pressure at 8.82 hPa, daylight 06:09-17:55'
```

#### Mars Facts

* The table containing facts about the planet including Diameter, Mass, etc. from the [Mars Facts webpage](https://space-facts.com/mars/) using Pandas. 


#### Mars Hemispheres

* High resolution images for each of Mar's hemispheres from the [USGS Astrogeology site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars).

```python
# Example:
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]
```

- - -

### * MongoDB and Flask Application

* A new HTML page that displays all of the information that was scraped from the URLs above.

* A Python script called `scrape_mars.py` with a function called `scrape` that executes all of the scraping code from above and returns one Python dictionary containing all of the scraped data.

* A route called `/scrape` that imports the `scrape_mars.py` script and calls the `scrape` function.

* The return value stored in Mongo as a Python dictionary.

* A root route `/` that queries the Mongo database and passes the mars data into an HTML template to display the data.

* A template HTML file called `index.html` that takes the mars data dictionary and displays all of the data in the appropriate HTML elements. 


## Methods Used
* Data visualization
* Data exploration
* Web Scraping 



## Technologies
* Python (Jupyter Notebook, BeautifulSoup, Pandas, Requests/Splinter).
* HTML
* MongoDB (pymongo)



## Output 
![final_app_part1.png](Instructions/Images/final_app_part1.png)
![final_app_part2.png](Instructions/Images/final_app_part2.png)



## Contact
* [Visit my LinkedIn](https://www.linkedin.com/in/caroline-delva-5184a172/) 
* [Visit my portfolio](https://carolinedelva.github.io/CarolineDelvaPortfolio/) 
