

# Existe alguns poucos pacotes R para trabalhar com arquivos hdf5

# h5
# hdf5r
# ncdf4
# rgdal
# rhdf5 - Da biocontuctor

setwd("C:/Users/Usuário/Desktop")
# Para usar o pacote h5, o primeiro passo é carregar o pacote
library(hdf5r)

# Para abrir um arquivo NASA HDF, 
# use h5file() com o caminho para o nome do arquivo
file <- h5file ('SMAP_L3_SM_P_20151012_R11920_001.h5', 'r')
typeof(file)

new.file <- as.data.frame(as.list(file))

# Para listar os conjuntos de dados disponíveis no arquivo HDF5, 
# digite o nome da variável atribuído

h5attr(file[["Soil_Moisture_Retrieval_Data"]])



list.datasets (file, 
               recursive = TRUE)

# Para recuperar dados do conjunto de dados em um grupo, 
# use readDataSet ().
dataset <- file["/Soil_Moisture_Retrieval_Data/latitude"]

dset <- file['/Soil_Moisture_Retrieval_Data/latitude']

vals <- readDataSet(dset)

# Para recuperar o valor do atributo de um conjunto de dados, 
# use h5attr ().

fv <- h5attr(dset, "_FillValue")






