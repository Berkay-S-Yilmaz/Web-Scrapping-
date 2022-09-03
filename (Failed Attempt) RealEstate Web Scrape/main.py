#Modules
from bs4 import BeautifulSoup
import requests
from csv import writer


#Object to get URL
req = requests.get("https://www.century21.com/real-estate/austin-tx/LCTXAUSTIN/")
#Processing url contents with html.parser
cont = req.content
soup = BeautifulSoup(cont, "html.parser")

with open('RealEstate.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Location', 'Price', 'Area']
    thewriter.writerow(header)

#Finding all property listings on url through the class
all = soup.find_all("div", {"class", "property-card-primary-info"})
#Creating For Loop to iterate through each listing 
for list in all:
        #picking out specific details of houses for sales
        listing_type = list.find("div", {"class", "pdp-listing-type sale"}).text.replace("\n", "")
        price = list.find("a", {"href", "listing-price"}).text.replace("\n", "")
        bedrooms = list.find("div", {"class", "property-beds"}).text.replace("\n", "")
        bathrooms = list.find("div", {"class", "property-baths"}).text.replace("\n", "")
        half_baths = list.find("div", {"class", "property-half-baths"}).text.replace("\n", "")
        property_sqft = list.find("div", {"class", "property-sqft"}).text.replace("\n", "")
        address = list.find("div", {"class", "property-address"}).text.replace("\n", "")

 #Variable that contains all the details of housing
        info = [listing_type, price, bedrooms, bathrooms, half_baths, property_sqft, address]
        thewriter.writerow(info)