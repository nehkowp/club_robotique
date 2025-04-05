import rsk

with rsk.Client(host='127.0.0.1', key='') as client:
    print(client.robots['green'][1].position())