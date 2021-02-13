# Importing Packages
import pandas as pd
from bs4 import BeautifulSoup
import requests
import json

# Function to convert JSON file to .CSV file


def json_to_csv():
    # Reading the JSON file using pandas library
    asd = pd.read_json("technologies.json")
    # Converting the JSON file to .CSV file
    asd.to_csv("technologies.csv", index=None)
    # Printing a message to notify that the process has been completed
    print("Successfully created the csv")

# Function to read the .CSV file


def reading_csv():
    # Setting the variable "dataset" as global inorder to use it in another function
    global dataset
    # Reading the .CSV file using pandas library
    dataset = pd.read_csv("technologies.csv")
    # Printing a message to notify that the process has been completed
    print("Successfully read the csv")

# Web Scraping and Checking technologies


def techno(r):
    # If the link doesn't throws any exceptions then proceed with this code
    try:
        # Calling the reading_csv() funtion
        reading_csv()
        # Creating a response object "resp" to store the request-response
        resp = requests.get(r)
        # Storing the content with the read mentod
        soup = BeautifulSoup(resp.content, 'html.parser')
        # Performing the typecasting and storing the result
        a = str(soup)
        # Checking whether the following technologies are found in the provided URL, if yes -> return
        return str([i for (i, j) in zip(dataset.columns, dataset.iloc[7]) if ((i or j) in a)])

    # If the link throws any exceptions then proceed with this code
    except requests.exceptions.HTTPError as errh:
        return "Sorry, the link is seem to be broken. Kindly provide a valid link"
    except requests.exceptions.ConnectionError as errc:
        return "Sorry, the link is seem to be broken. Kindly provide a valid link"
    except requests.exceptions.Timeout as errt:
        return "Sorry, the link is seem to be broken. Kindly provide a valid link"
    except requests.exceptions.RequestException as err:
        return "Sorry, the link is seem to be broken. Kindly provide a valid link"
