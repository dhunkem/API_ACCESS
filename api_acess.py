from geometry import *
from layers import *
import json

api_key = 'CS-SVwklkAHrP7k6A6Kf6vRbPQwlvJww'
geojson_file_path = '/home/install/Downloads/2023_mini_cliped.geojson'

with open(geojson_file_path, 'r') as geojson_file:
    geojson_data = json.load(geojson_file)


layer_id = create_layer('2023_mini_area', 'Class in column DN-> 1: Deciduous Tree, 2:Conifer Tree, 3: Dead Tree, 4: Grasland, 5:Cropland, 6:Built Up, 7: Water, 255: No Label', api_key)
if layer_id is not None:
    print(f'Returned layer ID: {layer_id}')

upload_geometry(layer_id, geojson_data, api_key)


#layer_id, layer_name, layer_description = get_layer_information(layer_id, api_key)
#all_layers = get_all_layer_information(api_key)
#delete_layer(layer_id_to_delete, api_key)
#change_layer_name_and_description(layer_id, new_name, new_description, api_key)

