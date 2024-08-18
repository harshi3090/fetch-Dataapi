import requests
import os
from dotenv import load_dotenv
import dataConversion

# Load environment variables from .env file
load_dotenv()

# Base URL
rdfox_server = "http://localhost:12110"

# Creating data store
try:
    dataStoreName = os.getenv("DATASTORE_NAME")  # Fixed typo in the environment variable name
    response = requests.post(rdfox_server + "/datastores/" + dataStoreName)
except Exception as e:
    print(e)

# Assigning converted data
turtle_data = dataConversion.ttl_data  # Corrected variable name

try:
    payload = {
        'operation': 'add-content-update-prefixes'  # Fixed dictionary syntax and quotes
    }
    response = requests.patch(rdfox_server + "/datastores/" + dataStoreName + "/content", params=payload, data=turtle_data)
except Exception as e:
    print(response.status_code, response.text)
