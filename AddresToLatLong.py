import pandas as pd
from geopy.geocoders import Nominatim

df = pd.read_excel(r'data\Enderecos.xlsx')
print(df.head())

geolocator = Nominatim(user_agent="Geolocation")

for i in range(0, len(df)):
    
    local = "{}, {}, {}, {}, {}".format(df['Logradouro'][i], df['Numero'][i], df['Bairro'][i], df['Cidade'][i], df['Estado'][i])
    
    location = geolocator.geocode(local)
    print(local)
    print("Latitude: {}".format(location.latitude))
    print("Longitude: {}".format(location.longitude))
    df['Latitude'] = location.latitude
    df['Longitude'] = location.longitude
    print('==============================================================')