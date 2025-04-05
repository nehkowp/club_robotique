import rsk
import time
import math


def distance(c1,c2):
    x1 = c1[0] 
    y1 = c1[1]
    x2 = c2[0] 
    y2 = c2[1]
    return math.sqrt((x1-x2)**2+(y1-y2)**2)


def angle_ball(cR,cB):
    xb = cB[0] 
    x = cR[0]
    cosa = (abs(xb-x)/distance(cR,cB))-math.pi
    print(cosa)
    return math.acos(cosa)


def point_on_line(xb, yb, xg, yg, distance):
    # Vecteur directeur
    vx = xg + xb
    vy = yg + yb
    
    # Normalisation
    longueur = math.sqrt(vx**2 + vy**2)
    vx_unitaire = vx / longueur
    vy_unitaire = vy / longueur
    
    # Nouveau point
    x = xb + distance * vx_unitaire
    y = yb + distance * vy_unitaire
    
    return [float(x), float(y)]
 
with rsk.Client(host='192.168.100.1', key='') as client:
        print("Connexion établie avec les robots")
        #client.green1.kick()
        # def print_the_ball(client, dt):
            # print(client.ball)

        # This will print the ball everytime a new information is obtained from the client
        # client.on_update = print_the_ball
        while True:

            # Ball's position (x [m], y [m])
            # client.ball
            try:
            
                # print("Position robot actuel", client.green1.position)
                # print("Position Robot prévue : ", point_on_line(client.ball[0], client.ball[1], -0.9, 0, -0.20))
                coords_prevus = point_on_line(client.ball[0], client.ball[1], -0.9, 0, -0.08)
                target1 = [coords_prevus[0], coords_prevus[1],0]
                client.green1.goto(target1)
                target2 = [coords_prevus[0], coords_prevus[1],angle_ball(client.green1.position,client.ball)]
                client.green1.goto(target2)
                client.green1.kick()                
            except Exception as e:
                # Capturer toutes les autres exceptions
                print(f"Une erreur s'est produite: {e}")
                
            # Pause avant la prochaine itération, quoi qu'il arrive

           


            # #time.sleep(1)
            # client.green1.goto((0.55, 0.55, 0))
            # client.green1.goto((-0.55, 0.55, 0))
            # client.green1.goto((-0.55, -0.55, 0))
            # client.green1.goto((0.55, -0.55, 0))
            ##print(client.ball[1])
            ##print(client.ball[0])
            ##client.green1.goto((client.ball[0], client.ball[1], 0))
            ##client.green1.kick()

            