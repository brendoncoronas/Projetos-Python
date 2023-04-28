# faça um projeto que mostre a usabilidade de

from datetime import datetime

# hora brasileira
data_str_data = '20/04/2023  07:49:23'
data_str_fmt = '%d/%m/%Y %H:%M:%S'
#
data_str_data = '2023-04-20  07:49:23'
data_str_fmt = '%Y-%m-%d %H:%M:%S'


# no strptime recebemos a data e o formato
data = datetime.strptime(data_str_data, data_str_fmt)
