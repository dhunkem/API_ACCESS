import requests
import json
import pygeoj

def upload_geometry(layer_id, geojson, api_key):
    # Define the API endpoint URL with the layer ID
    url = f'https://geodata.ameno.de/api/v0.1/Geometry/UpsertFeaturesOfLayer/{layer_id}'

    # Define the request headers
    headers = {
        'x-api-key': api_key,
        'Content-Type': 'application/json; x-api-version=0.1',
        'accept': '*/*',
    }

    # Define the request body as a dictionary
    # Wrap the GeoJSON data in the 'geoJson' field
    data = {
        'geoJson': geojson
    }

    # Convert the request body to JSON format
    json_data = json.dumps(data)

    # Send the PUT request
    response = requests.put(url, headers=headers, data=json_data)
    print(response.text)
    # Check the status code
    if response.status_code == 204:
        print('Geometry uploaded successfully.')
    else:
        print('Error: PUT request failed with status code', response.status_code)


def get_geometry(layer_id, api_key):
    # Define the API endpoint URL with the layer ID
    url = f'https://geodata.ameno.de/api/v0.1/Geometry/FeatureCollectionOfLayer/{layer_id}/GeoJson'

    # Define the request headers
    headers = {
        'x-api-key': api_key,
        'accept': 'text/plain; x-api-version=0.1',
    }

    # Send the GET request
    response = requests.get(url, headers=headers)

    # Check the status code
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error: GET request failed with status code {response.status_code}')
        return None

