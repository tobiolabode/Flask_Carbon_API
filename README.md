# Flask_Carbon_API
An API developed to work out the about of emmissions produced when a shipment is fulliled.


The API  will calculate emissions produced when shipping products around the world. I got this idea from a website called [patch](https://www.usepatch.com/). 
The company offsets carbon by working out the emissions generated when shipping a product.

Please read the [blog post of this project on my website for more info](https://www.tobiolabode.com/blog/2020/6/25/python-api-for-carbon-emmissions).

## Usage
You can test the API by using a local host. To do this clone the Project
```
clone...
```
Then run flask_restful_ex.py
```
python flask_restful_ex.py
```
This will run the server

You can then use the request.py file to send info at the API

To caluate road freight using add '/road_freight' and the end of your local host address

To caluate boat freight using add '/boat_freight' and the end of your local host address

The road_freight only allows for miles and tonnes
The boat_freight  allows for kilometere and tonnes
