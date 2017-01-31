import turtle
import math
bob = turtle.Turtle()
# print(bob)


def calculations(r, theta):
    '''
    takes in (r), the desired radius of the flower
    takes in (theta), half the desired angle of the petal
    returns calc_values in list [line_len, line_angle]
    line_len is the length of the individual little lines, line_angle is their angle
    '''
    theta_radians = theta * math.pi / 180
    r_gauge = r/(2*math.cos(theta_radians))
    arc_len = (2*r_gauge*math.pi)*((180-2*theta)/360)
    line_len = arc_len / 90
    line_angle = 2*theta / 90
    calc_values = [line_len, line_angle]
    return calc_values


def half_petal(r, theta, bob):
    '''    takes in radius (r), angle (theta) and bob(the turtle sim)
    moves the turtle through the path of half the petal    '''
    calc_values = calculations(r, theta)
    line_len = calc_values[0]
    line_angle = calc_values[1]
    for i in range(90):
        bob.fd(line_len)
        bob.lt(line_angle)


def petal_turn_outside(theta):
    '''    takes in theta
    rotates the turtle for the tip of the petal back towards the center    '''
    bob.lt(180-2*theta)


def petal_turn_inside(theta, num_petals):
    '''    takes in angle (theta) and desired number of petals (num_petals)
    rotates the turtle on the inside of the petal for the next petal    '''
    bob.rt(180-((360-2*num_petals*theta)/num_petals))


def draw_petal(r, theta, num_petals, bob):
    '''    takes in radius, theta, num_petals, and bob
    draws a complete petal    '''
    half_petal(r, theta, bob)
    petal_turn_outside(theta)
    half_petal(r, theta, bob)
    petal_turn_inside(theta, num_petals)


def draw_flower(r, theta, num_petals, bob):
    '''takes in radius, theta, num_petals, and bob
    draws a complete flower'''
    for i in range(num_petals):
        draw_petal(r, theta, num_petals, bob)


draw_flower(300, 40, 6, bob)
bob.rt(30)
draw_flower(200, 40, 6, bob)
bob.rt(30)
draw_flower(100, 40, 6, bob)
turtle.mainloop()
