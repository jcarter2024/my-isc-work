with open('weather.csv', 'r') as weather:
    rain = []
    for line in weather.readlines():
        print(line)
