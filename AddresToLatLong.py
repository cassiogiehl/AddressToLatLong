import pandas as pd
from geopy.geocoders import Nominatim

# df = pd.read_excel(r'~/code/AddressToLatLong/data/Enderecos.xlsx')
df = pd.read_excel(r'C:\Users\Cássio Giehl\Documents/Enderecos.xlsx')


print(df.head())

geolocator = Nominatim(user_agent="Geolocation")

for i in range(0, len(df)):
    
    local = "{}".format(df['Logradouro'][i])

    if not pd.isnull(df['Numero'][i]):
        local = "{}, {}".format(df['Logradouro'][i], df['Numero'][i])

    location = geolocator.geocode(local)
    print('\n')
    print(local)
    print("Latitude: {}".format(location.latitude))
    print("Longitude: {}".format(location.longitude))
    df['Latitude'] = location.latitude
    df['Longitude'] = location.longitude