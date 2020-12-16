from visual import *

cross_road1 = curve(pos=[(5,0,40),(5,0,-40)], color=color.white)
cross_road2 = curve(pos=[(-5,0,40),(-5,0,-40)], color=color.white)
cross_road3 = curve(pos=[(0,0,40),(0,0,40)], color=color.white)

cross_road3 = box(pos=(2.5,0,36), size = (5,0,4), color=color.white)
cross_road3 = box(pos=(2.5,0,28), size = (5,0,4), color=color.white)
cross_road3 = box(pos=(2.5,0,20), size = (5,0,4), color=color.white)
cross_road3 = box(pos=(2.5,0,12), size = (5,0,4), color=color.white)
cross_road3 = box(pos=(2.5,0,4), size = (5,0,4), color=color.white)
cross_road3 = box(pos=(2.5,0,-4), size = (5,0,4), color=color.white)
cross_road3 = box(pos=(2.5,0,-12), size = (5,0,4), color=color.white)
cross_road3 = box(pos=(2.5,0,-20), size = (5,0,4), color=color.white)
cross_road3 = box(pos=(2.5,0,-28), size = (5,0,4), color=color.white)
cross_road3 = box(pos=(2.5,0,-36), size = (5,0,4), color=color.white)

cross_road3 = box(pos=(-2.5,0,32), size = (5,0,4), color=color.white)
cross_road3 = box(pos=(-2.5,0,24), size = (5,0,4), color=color.white)
cross_road3 = box(pos=(-2.5,0,16), size = (5,0,4), color=color.white)
cross_road3 = box(pos=(-2.5,0,8), size = (5,0,4), color=color.white)
cross_road3 = box(pos=(-2.5,0,0), size = (5,0,4), color=color.white)
cross_road3 = box(pos=(-2.5,0,0), size = (5,0,4), color=color.white)
cross_road3 = box(pos=(-2.5,0,-8), size = (5,0,4), color=color.white)
cross_road3 = box(pos=(-2.5,0,-16), size = (5,0,4), color=color.white)
cross_road3 = box(pos=(-2.5,0,-24), size = (5,0,4), color=color.white)
cross_road3 = box(pos=(-2.5,0,-32), size = (5,0,4), color=color.white)


road = curve(pos=[(-40,0,-40),(20,0,-40)], color=color.white)
road = curve(pos=[(-40,0,40),(20,0,40)], color=color.white)
road = curve(pos=[(20,0,-40),(20,0,-100)], color=color.white)
road = curve(pos=[(20,0,40),(20,0,80)], color=color.white)
road = curve(pos=[(-40,0,-40),(-60,-5,-40)], color=color.white)
road = curve(pos=[(-40,0,40),(-60,-5,40)], color=color.white)

building1 = box(pos=(5,5,55), size = (15,10,5), color=color.white)
building1 = box(pos=(5,1,51), size = (15,2,3), color=color.gray(0.7))

building1 = box(pos=(-18,5,55), size = (15,10,5), color=color.white)
building1 = box(pos=(-18,1,51), size = (15,2,3), color=color.gray(0.7))

building1 = box(pos=(-30,5,55), size = (15,10,5), color=color.white)
building1 = box(pos=(-30,1,51), size = (15,2,3), color=color.gray(0.7))

building2 = box(pos=(-20,14,-60), size = (15,28,15), color=color.white)
building2 = box(pos=(-20,30,-65), size = (15,5,5), color=color.white)
building2 = box(pos=(-25,30,-58), size = (5,5,5), color=color.white)
building1 = box(pos=(-20,1,-60), size = (17,2,17), color=color.gray(0.7))
building1 = box(pos=(-20,14,-60), size = (17,2,17), color=color.gray(0.7))
building1 = box(pos=(-20,28,-60), size = (17,2,17), color=color.gray(0.7))

building3 = box(pos=(-50,22,-60), size = (25,42,15), color=color.white)
building3 = box(pos=(-50,45,-65), size = (25,5,5), color=color.white)
building3 = box(pos=(-45,45,-58), size = (5,5,5), color=color.white)
building2 = box(pos=(-50,1,-60), size = (27,2,17), color=color.gray(0.7))
building2 = box(pos=(-50,14,-60), size = (27,2,17), color=color.gray(0.7))
building2 = box(pos=(-50,28,-60), size = (27,2,17), color=color.gray(0.7))
building2 = box(pos=(-50,42,-60), size = (27,2,17), color=color.gray(0.7))

door = box(pos = (30,21,-85), size = (25,5,5), axis = (0,100,0))
door.rotate(angle=50, axis=(0,0,15), origin = (0,0,0))

door2 = box(pos = (38,20,-85), size = (5,40,5))
door3 = box(pos = (38,45,-85), size = (5,10,5), color=(0,0.3,0.9))


traffic = cylinder(pos = (-10,0,-42), axis = (0,7,0), radius = 0.5, color=color.white)
traffic = cylinder(pos = (10,0,42), axis = (0,7,0), radius = 0.5, color=color.white)
trafficbox = box(pos = (-10,8,-42), size = (3,5,3))
trafficbox = box(pos = (10,8,42), size = (3,5,3))

