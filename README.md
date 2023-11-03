# DoWell Message Analysis Project From DoWell UX Living Lab

Welcome to the DoWell DoWell Message Analysis Project! The Message Analysis Project is a tool that allows users to extract text from images and analyze it to identify nouns, verbs, and adjectives. It also provides an API for text analysis, making it easy to integrate into other applications.

## Features

- Extract text from images using Optical Character Recognition (OCR).
- Analyze extracted text to identify nouns, verbs, and adjectives.
- User-friendly web interface for image uploads and analysis.
- API endpoint for text analysis.

## Getting Started

To get started with this project, you have two options:

1. **Web Interface:**

   - Visit our web application [here](https://example.com) to upload an image and analyze the text.
   
2. **API Usage:**

   - To use the API, you need an API key. Please contact us at [api@example.com](mailto:api@example.com) to obtain your API key.
   - Make a POST request to `https://api.example.com/analyze` with your API key and the text you want to analyze.
   - You will receive a JSON response with information about the nouns, verbs, and adjectives in the text.


# Steps to use DoWell Message Analysis and APIs
There are two main steps to use DoWell DataCube


## Step 1: Add request for database
To submit a request for the database, please begin by logging into DataCube. You can access the login page by clicking on the following link: [DataCube Login](https://datacube.uxlivinglab.online/). <br>
Once you have successfully logged in, you will be redirected to the dashboard. From there, you can enter your request for the database.

![Dashboard](screenshots/dashboard.jpg)
<br>
<br>
After submitting your request for the database, you'll have the ability to view the created database and its associated collections. <br>
By clicking on "View Collection," you can access and inspect all the collections within the relevant database. <br>
Moreover, you also have the option to add additional collections to the database if needed
![Metadata Records](screenshots/metadata_record.jpg)
![Add Collections](screenshots/add_collections_to_database.jpg)
<br>
<br>
You also have the option to import JSON or CSV files to add documents to a collection.
![Import File](screenshots/import_file.jpg)
<br>
<br>

You can also view the data in a data view by selecting the database and collection from the dropdown menu.
![Data View](screenshots/data_view.jpg)
<br>
<br>
After adding the database and collection, you can now utilize APIs to add, retrieve, and update data within the database.

## Step 2: Use Database using APIs
Click here to read the documentation in postman [Documentation](https://documenter.getpostman.com/view/29895764/2s9YRB1WyN)

# API Detailed Documentation
=============================================================================
## Fetch Data Using the API

### URL: https://livinglab100114.pythonanywhere.com/API/noun_&_verb/v1/API
### Method: POST

This API enables you to retrieve data.

#### Request Data / API Payload

```json
{
    "api-key": "your-dowell-api-key",
    "data_sentence": "your-data"
}
```

#### Parameters

- `api-key` (required): Your Dowell API key.
- `data_sentence`: Your given text or sentences.

#### Example of Fetching Data in Python

```python
import requests
import json

url = "https://datacube.uxlivinglab.online/db_api/get_data/"
query = {"_id": "101001010101"}

data = {
    "api-key": "your-dowell-api-key",
    "db_name": "dowell",
    "coll_name": "test",
    "operation": "fetch",
    "filters": json.dumps(query),
    "limit": 1,
    "offset": 0
}

response = requests.post(url, json=data)
print(response.text)
```

#### Response:

- For success: `{"data": "[]"}` (an empty array in this example)
- For error: `{"message": "Database not found"}`
- 

### Response Codes

- For success: HTTP 200 OK with a JSON response containing a success message.
- For errors: HTTP status codes such as 404 Not Found or 400 Bad Request with an error message.

**Note:** Ensure you replace placeholders such as `"your-dowell-api-key"` and other specific details with actual values in your requests.

```
Thank you for choosing Dowell API. We look forward to helping you with your data operations.Please ensure you have the necessary API key and valid data to perform these operations successfully.
