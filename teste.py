import pandas as pd
from geopy.geocoders import Nominatim
import xlsxwriter

df = pd.read_excel(r'C:\Users\Cássio Giehl\Documents\EnderecosMKT.xls')

geolocator = Nominatim(user_agent="Geolocation")

workbook = xlsxwriter.Workbook(r'C:\Users\Cássio Giehl\Documents\AddressWithLatLong.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True})

worksheet.write('A1', 'Logradouro', bold)
worksheet.write('B1', 'Numero', bold)
worksheet.write('C1', 'Bairro', bold)
worksheet.write('D1', 'Cidade', bold)
worksheet.write('E1', 'Estado', bold)
worksheet.write('F1', 'Lat Long', bold)
worksheet.write('G1', 'Detalhamento', bold)

for i in range(0, len(df)):
    
    local = "{}".format(df['Nome Logradouro'][i])

    if not pd.isnull(df['Número Logradouro'][i]):
        local = "{}, {}, Rio Grande do Sul".format(df['Nome Logradouro'][i], df['Número Logradouro'][i])

    location = geolocator.geocode(local, timeout=100)
    print('\n')
    print(i)
    print(" - ")        
    print(local)
    
    if location is not None:
        print("lat. long: {}, {}".format(location.latitude, location.longitude))
        df['Lat Long'][i] = str(location.latitude) +', '+ str(location.longitude)
        df['Detalhamento'][i] = str(location)
    else:
        df['Lat Long'][i] = 'Não encontrado'
        print('Não encontrado')
    
    try:
        cell_a = 'A' + str(i+1)
        worksheet.write(cell_a, df['Nome Logradouro'][i])
        cell_b = 'B' + str(i+1)
        worksheet.write(cell_b, df['Número Logradouro'][i])
        cell_c = 'C' + str(i+1)
        worksheet.write(cell_c, df['Nome Bairro'][i])
        cell_d = 'D' + str(i+1)
        worksheet.write(cell_d, df['Município'][i])
        cell_e = 'E' + str(i+1)
        worksheet.write(cell_e, df['UF'][i])
        cell_f = 'F' + str(i+1)
        worksheet.write(cell_f, df['Lat Long'][i])
        cell_g = 'G' + str(i+1)
        worksheet.write(cell_g, df['Detalhamento'][i])
    except:
        print("Sem sucesso na inserção no X")

workbook.close()
print('\n\n')
print('Script Finalizado!')
print("XLSX Criado com sucesso!")