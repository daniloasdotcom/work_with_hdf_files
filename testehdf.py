import h5py
import os
from pandas import DataFrame

# Stores the working directory in the path variable
path = "C:\\Users\\Usuário\\Desktop"

# Indicating the working directory
os.chdir(path)

# Open the .hdf5 file in read mode
# And store it in the file variable
file = h5py.File('GLAH10_633_2131_001_1317_0_01_0001.h5', 'r')

# List of folders within the .hdf5 file
print('Lista de grupos no arquivo hdf5')
print(file.keys())
print('')

# Let's store the interest group between [] in data01
data01 = file['Data_1HZ']

# List of folders within the data01 group
print('Lista de chaves no arquivo datas')
print(data01.keys())
print('')

# Let's store the interest group between [] in data02
data02 = file['Data_1HZ/Geolocation']

# List of folders within the data02 group
print('Lista de chaves no arquivo datas02')
print(data02.keys())
print('')


data03 = file['Data_1HZ/Geolocation/d_lat']

print('Lista de chaves no arquivo datas03')
print(data03)
print('')

# Now that we have found our data of interest we will store it in a list type variable
latitude = list(file['Data_1HZ/Geolocation/d_lat'])
longitude = list(file['Data_1HZ/Geolocation/d_lon'])

# Let's create a data frame with the data lists above
# First a data frame with latitude data
df = DataFrame(latitude,  columns=['Latitude'])

print(df)

# And now appending the longitude data in the second column with loc = 1
df.insert(loc=1, column='Longitude', value=longitude)

# We will convert it to excel so we can use the data in other programs
df.to_excel("danilo.xlsx", index=False)

# Finally we will print on the console the value of the first 5 lines of our data frame
print(df.head())


"""
# Imprimimos uma lista das informações do arquivo de umidade do solo
# e imprimimos uma lista dos tipo de atributos presentes nesse arquivo
print("Resumo dos dados de umidade do solo: {}".format(datas['soil_moisture']))
print("Atributos presentes no arquivo de umidade do solo: {}".format(list(datas['soil_moisture'].attrs)))

print('')

print("Descrição: {}".format(datas['soil_moisture'].attrs['long_name'].decode()))
print("Unidade: {}".format(datas['soil_moisture'].attrs['units'].decode()))
print("Coodenadas: {}".format(datas['soil_moisture'].attrs['coordinates'].decode()))

umidade_solo = list(datas['soil_moisture'])

arquivocsv = pd.DataFrame({"Umidade do Solo": umidade_solo})
print('')
print('Arquivos:')
print(arquivocsv.head())

arquivocsv.columns = [datas['soil_moisture'].attrs['long_name'].decode() +
                      " (" + datas['soil_moisture'].attrs['units'].decode() + ")"]

arquivocsv.to_csv("danilo.csv", index = False)
"""
