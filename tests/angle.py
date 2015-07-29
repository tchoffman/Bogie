import math
rotation = -45
for angle in range(0,360,15):
    x = math.cos(math.radians(angle))
    y = math.sin(math.radians(angle))
    x_prime = (x * math.cos(math.radians(rotation))) - (y * math.sin(math.radians(rotation)))
    y_prime = (x * math.sin(math.radians(rotation))) + (y * math.cos(math.radians(rotation)))
    print "Angle: ", angle, " X: ", x, " Y: ", y
    print "Bogie: ", angle + rotation, " Xp: ", x_prime, " Yp: ", y_prime 
