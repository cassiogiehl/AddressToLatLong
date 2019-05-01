import pandas as pd
from geopy.geocoders import Nominatim

df = pd.read_excel(r'~/code/AddressToLatLong/data/Enderecos.xlsx')
print(df.head())

geolocator = Nominatim(user_agent="Geolocation")

for i in range(0, len(df)):
    
    local = "{}".format(df['Logradouro'][i])

    if pd.isnull(df['Numero'][i]) > 0:
        local = "{}, {}".format(df['Logradouro'][i], df['Numero'][i])

        if pd.isnull(df['Bairro']) > 0:
            local = "{}, {}, {}".format(df['Logradouro'][i], df['Numero'][i], df['Bairro'][i])

            if pd.isnull(df['Cidade']) > 0:
                local = "{}, {}, {}, {}".format(df['Logradouro'][i], df['Numero'][i], df['Bairro'][i], df['Cidade'][i])
                    
                if pd.isnull(df['Cidade']) > 0:
                    local = "{}, {}, {}, {}, {}".format(df['Logradouro'][i], df['Numero'][i], df['Bairro'][i], df['Cidade'][i], df['Estado'][i])
    
    location = geolocator.geocode(local)
    print('\n')
    print(local)
    print("Latitude: {}".format(location.latitude))
    print("Longitude: {}".format(location.longitude))
    df['Latitude'] = location.latitude
    df['Longitude'] = location.longitude