
countries = ['Ghana', 'USA', 'China']

cities = [['Accra', '-245.202E', '-83.67464W'], ['Newyork', '-37.690N', '83.232N'], 
          ['Beijing', '69.0532S', '-133.5336N']]

tour_maps = dict(zip(countries, cities))
for country, position in tour_maps.items():
    globals()['{}_list'.format(country)] = position
    
print(USA_list)
print(Ghana_list)
print(China_list)