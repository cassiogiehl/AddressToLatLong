import pandas as pd
from geopy.geocoders import Nominatim
import xlsxwriter

# df = pd.read_excel(r'~/code/AddressToLatLong/data/Enderecos.xlsx')
df = pd.read_excel(r'C:\Users\Cássio Giehl\Documents\Enderecos.xlsx')


print(df.head())

geolocator = Nominatim(user_agent="Geolocation")

for i in range(0, len(df)):
    
    local = "{}".format(df['Logradouro'][i])

    if not pd.isnull(df['Numero'][i]):
        local = "{}, {}".format(df['Logradouro'][i], df['Numero'][i])

    location = geolocator.geocode(local)
    print('\n')
    print(local)
    print("lat. long: {}, {}".format(location.latitude, location.longitude))
    df['Lat Long'][i] = str(location.latitude) +', '+ str(location.longitude)
    # df['Latitude'][i] = location.latitude
    # df['Longitude'][i] = location.longitude

print('\n\n')
print('Script Finalizado!')

workbook = xlsxwriter.Workbook(r'C:\Users\Cássio Giehl\Documents\AddressWithLatLong.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True})

for j in range(0, len(df)):
    worksheet.write('A1', 'Logradouro', bold)
    worksheet.write('B1', 'Numero', bold)
    worksheet.write('C1', 'Bairro', bold)
    worksheet.write('D1', 'Cidade', bold)
    worksheet.write('E1', 'Estado', bold)
    worksheet.write('F1', 'Lat Long', bold)
    
    cell_a = 'A' + str(j+1)
    cell_b = 'B' + str(j+1)
    cell_c = 'C' + str(j+1)
    cell_d = 'D' + str(j+1)
    cell_e = 'E' + str(j+1)
    cell_f = 'F' + str(j+1)
    worksheet.write(cell_a, df['Logradouro'][j])
    worksheet.write(cell_b, df['Numero'][j])
    worksheet.write(cell_c, df['Bairro'][j])
    worksheet.write(cell_d, df['Cidade'][j])
    worksheet.write(cell_e, df['Estado'][j])
    worksheet.write(cell_f, df['Lat Long'][j])

workbook.close()
    