import json
import requests

def create_layer(name, description, api_key):
    # Define the API endpoint URL
    url = 'https://geodata.ameno.de/api/v0.1/Layers'

    # Define the request headers
    headers = {
        'x-api-key': api_key,
        'Content-Type': 'application/json; x-api-version=0.1',
        'accept': '*/*',
    }

    # Define the request body as a dictionary
    data = {
        'name': name,
        'description': description,
    }

    # Convert the request body to JSON format
    json_data = json.dumps(data)

    # Send the POST request
    response = requests.post(url, headers=headers, data=json_data)

    # Check the status code
    if response.status_code == 201:
        # Parse the response JSON
        response_data = json.loads(response.text)
        
        # Check if the response contains the 'id' field
        if 'id' in response_data:
            layer_id = response_data['id']
            print(f'Layer created successfully with ID: {layer_id}')
            return layer_id
        else:
            print('Error: Response does not contain the "id" field.')
            return None
    else:
        print('Error: POST request failed with status code', response.status_code)
        return None


def delete_layer(layer_id, api_key):
    # Define the API endpoint URL with the layer ID
    url = f'https://geodata.ameno.de/api/v0.1/Layers/{layer_id}'

    # Define the request headers
    headers = {
        'x-api-key': api_key,
        'accept': '*/*',
    }

    # Send the DELETE request
    response = requests.delete(url, headers=headers)

    # Check the status code
    if response.status_code == 204:
        print(f'Layer with ID {layer_id} deleted successfully.')
    else:
        print(f'Error: DELETE request failed with status code {response.status_code}')

def get_all_layer_information(api_key, print_layers=True):
    # Define the API endpoint URL for getting all layers
    url = 'https://geodata.ameno.de/api/v0.1/Layers/AllLayers'

    # Define the request headers
    headers = {
        'x-api-key': api_key,
        'accept': '*/*',
    }

    # Send the GET request
    response = requests.get(url, headers=headers)

    # Check the status code
    if response.status_code == 200:
        # Parse the response as JSON
        layers = response.json()
        if print_layers:
            formatted_layers = json.dumps(layers, indent=4)
            print('All Layers:')
            print(formatted_layers)
        return layers
    else:
        print('Error: GET request failed with status code', response.status_code)
        return None

def get_layer_information(layer_id, api_key):
    # Define the API endpoint URL with the layer ID
    url = f'https://geodata.ameno.de/api/v0.1/Layers/{layer_id}'

    # Define the request headers
    headers = {
        'x-api-key': api_key,
        'accept': '*/*',
    }

    # Send the GET request
    response = requests.get(url, headers=headers)

    # Check the status code
    if response.status_code == 200:
        layer_info = response.json()
        layer_id = layer_info['id']
        layer_name = layer_info['name']
        layer_description = layer_info['description']
        return layer_id, layer_name, layer_description
    
    else:
        print(f'Error: GET request failed with status code {response.status_code}')
        return None
    

def change_layer_name_and_description(layer_id, new_name, new_description, api_key):
    # Define the API endpoint URL with the layer ID
    url = f'https://geodata.ameno.de/api/v0.1/Layers/{layer_id}'

    # Define the request headers
    headers = {
        'x-api-key': api_key,
        'Content-Type': 'application/json; x-api-version=0.1',
        'accept': '*/*',
    }

    # Define the request body as a dictionary
    data = {
        'name': new_name,
        'description': new_description,
    }

    # Send the PUT request
    response = requests.put(url, headers=headers, json=data)

    # Check the status code
    if response.status_code == 204:
        print(f'Layer {layer_id} name and description changed successfully.')
    else:
        print(f'Error: PUT request failed with status code {response.status_code}')




