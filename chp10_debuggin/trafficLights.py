market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
switchLights(market_2nd)
assert 'red' in market_2nd.values(), 'Neighter light is red! ' + str(market_2nd)
#switchLights(mission_16th)
#assert 'red' in mission_16th.values(), 'Neighter light is red! ' + str(mission_16th)