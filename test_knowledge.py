countries = ['Ghana', 'USA', 'China']

cities = [['Accra', '-245.202E', '-83.67464W'], ['Newyork', '-37.690N', '83.232N'], 
          ['Beijing', '69.0532S', '-133.5336N']]


tour_maps = dict(zip(countries, cities))


while True:
    askme = input('Where do you want to Go?: ')
    if askme in tour_maps.keys():
        diff = round(abs((abs(float(tour_maps[askme][2][:-2]))- abs(float(tour_maps[askme][2][:-1])))), 4)
        print('Print the most popular city in ' + askme +  ' is ' 
             + tour_maps[askme][0],  'and it can be located in Longitude: ' + tour_maps[askme][1] +
             ' and Latitude ' + tour_maps[askme][2] + ' . The total distance between the two points is: ' + str(diff))
        break





