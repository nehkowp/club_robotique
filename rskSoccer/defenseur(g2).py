import rsk
from math import sqrt, pi
from time import sleep

with rsk.Client(host='127.0.0.1', key='') as client:
    green1_x, green1_y, ang_g1 = client.robots['green'][1].pose
    green2_x, green2_y, ang_g2 = client.robots['green'][2].pose
    blue1_x, blue1_y, ang_b1 = client.robots['blue'][1].pose
    blue2_x, blue2_y, ang_b2 = client.robots['blue'][2].pose
    ball_x, ball_y = client.ball

    def positions(client, dt):
        client.ball
        client.robots['green'][1].pose
        client.robots['green'][2].pose
        client.robots['blue'][1].pose
        client.robots['blue'][2].pose    

    distance_green1_ball = sqrt(((ball_x-green1_x)**2) + ((ball_y-green1_y)**2))
    distance_green2_ball = sqrt(((ball_x-green2_x)**2) + ((ball_y-green2_y)**2))
    distance_blue1_ball = sqrt(((ball_x-blue1_x)**2) + ((ball_y-blue1_y)**2))
    distance_blue2_ball = sqrt(((ball_x-blue2_x)**2) + ((ball_y-blue2_y)**2))
    distance_green1_green2 = sqrt(((green2_x-green1_x)**2) + ((green2_y-green1_y)**2))
    distance_blue1_blue2 = sqrt(((blue2_x-blue1_x)**2) + ((blue2_y-blue1_y)**2))
    distance_green1_blue1 = sqrt(((blue1_x-green1_x)**2) + ((blue1_y-green1_y)**2))
    distance_green1_blue2 = sqrt(((blue2_x-green1_x)**2) + ((blue2_y-green1_y)**2))
    distance_green2_blue1 = sqrt(((blue1_x-green2_x)**2) + ((blue1_y-green2_y)**2))
    distance_green2_blue2 = sqrt(((blue2_x-green2_x)**2) + ((blue2_y-green2_y)**2))

    #angle_g2_ball = (green2_x*(ball_x-green2_x) + ang_g2*(ball_y-green2_y))/distance_green2_ball


    while True:
        client.on_update = positions

        green1_x, green1_y, ang_g1 = client.robots['green'][1].pose
        green2_x, green2_y, ang_g2 = client.robots['green'][2].pose
        blue1_x, blue1_y, ang_b1 = client.robots['blue'][1].pose
        blue2_x, blue2_y, ang_b2 = client.robots['blue'][2].pose
        ball_x, ball_y = client.ball

        xvb0, yvb0 = client.ball

        distance_green1_ball = sqrt(((ball_x-green1_x)**2) + ((ball_y-green1_y)**2))
        #print(distance_green1_ball)

        distance_green2_ball = sqrt(((ball_x-green2_x)**2) + ((ball_y-green2_y)**2))
        #print(distance_green2_ball)

        distance_blue1_ball = sqrt(((ball_x-blue1_x)**2) + ((ball_y-blue1_y)**2))
        #print(distance_blue1_ball)

        distance_blue2_ball = sqrt(((ball_x-blue2_x)**2) + ((ball_y-blue2_y)**2))
        #print(distance_blue2_ball)   

        distance_green1_green2 = sqrt(((green2_x-green1_x)**2) + ((green2_y-green1_y)**2))
        #print(distance_green1_green2) 

        distance_blue1_blue2 = sqrt(((blue2_x-blue1_x)**2) + ((blue2_y-blue1_y)**2))     
        #print(distance_blue1_blue2)   

        distance_green1_blue1 = sqrt(((blue1_x-green1_x)**2) + ((blue1_y-green1_y)**2))
        #print(distance_green1_blue1)   

        distance_green1_blue2 = sqrt(((blue2_x-green1_x)**2) + ((blue2_y-green1_y)**2))
        #print(distance_green1_blue2)   

        distance_green2_blue1 = sqrt(((blue1_x-green2_x)**2) + ((blue1_y-green2_y)**2))
        #print(distance_green2_blue1)    

        distance_green2_blue2 = sqrt(((blue2_x-green2_x)**2) + ((blue2_y-green2_y)**2))
        #print(distance_green2_blue2)

        #angle_g2_ball = ((green2_x)*(ball_x-green2_x) + ang_g2*(ball_y-green2_y))/(distance_green2_ball)
        # angle_to_ball = math.atan2(ball_y - green2_y, ball_x - green2_x)

        # angle_difference = angle_to_ball - client.robots['green'][2].orientation

        # angle_difference = (angle_difference + pi) % (2*pi) - pi
        # if abs(angle_difference) > 0.1 and distance_green2_ball < 0.45:
        #     rotation_speed = 2 if angle_difference > 0 else -2
        #     client.robots['green'][2].control(ball_x, ball_y, rotation_speed)
        #     client.green2.kick()
        # elif abs(angle_difference) < 0.1 and distance_green2_ball < 0.45:
        #     client.robots['green'][2].goto((ball_x, ball_y, 0))
        #     client.green2.kick()

        #xvb0, yvb0 = client.ball # xvb0 -> position x de la balle après 0.1s, yvb0 -> position y de la balle après 0.1s 
        #sleep(0.1)
        #xvb1, yvb1 = client.ball # xvb1 -> position x de la balle après 0.1s, yvb1 -> position y de la balle après 0.1s 
        #if xvb0 == xvb1 and  yvb0 == yvb1:
           # breakpoint
            #print("La balle est au repos")
        #else:
            #xvb = (xvb1 - xvb0)/0.1 # xvb -> vitesse x de la balle entre les 0.1s
           # yvb = (yvb1 - yvb0)/0.1 # yvb -> vitesse y de la balle entre les 0.1s
           # vb = math.sqrt(xvb**2 + yvb**2) # vb -> vecteur vitesse de la balle entre les 0.1s
           # print("La balle se déplace à la vitesse de : ", vb, "m.s-1")

        if distance_blue1_ball <= 0.3 or distance_blue2_ball <= 0.3:
            if ball_x < 0.46 and ball_y >= -0.3 and ball_y <= 0.3: #balle en dehors de la défense
                client.robots['green'][2].goto((0.7, ball_y, pi))
            elif ball_x < 0.46 and ball_y < -0.3:
                client.robots['green'][2].goto((0.7, -0.27, pi))
            elif ball_x < 0.46 and ball_y > 0.3:
                client.robots['green'][2].goto((0.7, 0.27, pi)) #fin

            elif ball_x >= 0.73 and ball_y > 0.45: #zone 1
                client.robots['green'][2].goto((0.9, 0.25, pi))
            elif ball_x >= 0.62 and ball_x < 0.73 and ball_y > 0.45:
                client.robots['green'][2].goto((0.77, 0.3, pi))
            elif ball_x >= 0.46 and ball_x < 0.62 and ball_y >= 0.52:
                client.robots['green'][2].goto((0.68, 0.37, pi))
            elif ball_x >= 0.46 and ball_x < 0.62 and ball_y >= 0.45 and ball_y < 0.52:
                client.robots['green'][2].goto((0.65, 0.4, pi))# fin

            elif ball_x >= 0.73 and ball_y  < -0.45: #zone 2 (inverse de 1)
                client.robots['green'][2].goto((0.9, -0.25, pi))
            elif ball_x >= 0.62 and ball_x < 0.73 and ball_y < -0.45:
                client.robots['green'][2].goto((0.77, -0.3, pi))
            elif ball_x >= 0.46 and ball_x < 0.62 and ball_y <= -0.52:
                client.robots['green'][2].goto((0.68, -0.37, pi))
            elif ball_x >= 0.46 and ball_x < 0.62 and ball_y <= -0.45 and ball_y > -0.52:
                client.robots['green'][2].goto((0.65, -0.4, pi))# fin





        #bien
        # if ball_y >= -0.3 and ball_y <= 0.3 and ball_x < 0.46:
        #     if distance_blue1_ball < 0.3 or distance_blue2_ball < 0.3:
        #         client.green2.goto((0.7, ball_y, math.pi))
        #     else:
        #         client.green2.goto((0.9, ball_y, math.pi))
        # elif ball_y < -0.3 and ball_x < 0.46:
        #     client.green2.goto((0.9, -0.25, math.pi))
        # elif ball_y > 0.3 and ball_x < 0.46:
        #     client.green2.goto((0.9, 0.25, math.pi))
        # elif ball_x >= 0.46 and ball_x <= 0.62 and ball_y >= -0.3 and ball_y <= 0.3 and distance_blue1_ball < 0.3 or distance_blue2_ball < 0.3:
        #     client.green2.goto((0.70, ball_y, math.pi))
        # elif ball_y > -0.7 and ball_x > 0.46:
        #     client.green2.goto((0.9, ball_y, math.pi))
        #     client.green2.goto((ball_x+0.05, ball_y, math.pi))
        #     client.green2.kick()
        # client.blue1.kick()




        # if distance_green2_ball < 0.45:
        #     client.green2.goto((0.9, ball_y, math.pi))
        #     client.green2.goto((ball_x, ball_y, math.pi))
        #     client.green2.kick()


    
   

        


       # angle_to_ball = math.atan2(ball_y - green1_y, ball_x - green1_x)

        #angle_difference = angle_to_ball - client.robots['green'][1].orientation

      #  angle_difference = (angle_difference + math.pi) % (2*math.pi) - math.pi

       # if abs(angle_difference) > 0.1:
          #  rotation_speed = 2 if angle_difference > 0 else -2
          #  client.robots['green'][1].control(0, 0, rotation_speed)
        #else:
          #  client.robots['green'][1].control(0.5, 0, 0)

        #time.sleep(0.1)