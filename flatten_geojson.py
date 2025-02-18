import pandas as pd
def flatten_geojson(parent,id='OBJECTID'):
    '''
    Returns a DataFrame containing the properties from the supplied geojson dictionary structure.
    The hierarchy of object properties in the input is converted to a flattened representation comprising one row per item.
    '''

    #
    # convenience for Plotly Express chloropleth_mapbox:
    #
    for child in parent['features']:
        child['id'] = child['properties'][id]

    #
    # flatten properties to a data frame:
    #
    child_properties = [child['properties'] for child in parent['features']]
    df_child_properties = pd.DataFrame.from_dict(child_properties) 
    return df_child_properties