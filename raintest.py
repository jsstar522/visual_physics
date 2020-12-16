from visual import *
from random import *
from Tkinter import *

# structures module of University of Seoul (author = Park Jong Seok)
from uos import *



####### author ########
# Park Jong Seok      #
# University of Seoul #
# Dept. Physics       #
# jsstar522@gmail.com #
#######################





def main(n,Z,k):
    i = 0
    N = k
    rain_list = []
    # y is height because of figure showed first scene.
    # make Z number rain_drop
    while N>0:
        x = uniform(-1,1)
        z = uniform(-40,40)
        y = uniform(20,50)
        rain = curve(pos=[(x,y,z), (x, y-1, z)])
        rain_list.append(rain)
        N = N-1


    person = box(pos = (0,2,-65), size = (2,4,2), color = color.yellow)

    #initialization again because N is 0 due to upper while loop
    N = k

    dt = 0.1
    t = 0
    v_rain = vector(0,-10,0)
    v_per = vector(0,0,Z)
    count = 0

    # rain drop function
    def fall(n):
        rain_list[n].pos = rain_list[n].pos + v_rain*dt
    # person move function
    def move():
        person.pos = person.pos + v_per*dt


    traffic_light = sphere(pos = (-10,8,-41), radius = 1.5, color = (1,0,0))
    traffic_light = sphere(pos = (10,8,41), radius = 1.5, color = (1,0,0))

    while person.pos.z < 45 :
        while N > 0:
            rate(100000)
            if rain_list[N-1].pos[1][1] > 0: # rain-drop is falling while z>0(in the air)
                fall(N-1)
                #rain_list[N-1].pos.x -> rain_list[N-1].pos[1][0](down-edge of rain drop)
                #rain_list[N-1].pos.y -> rain_list[N-1].pos[1][1]
                #rain_list[N-1].pos.z -> rain_list[N-1].pos[1][2]
                if (rain_list[N-1].pos[1][0] > person.pos.x - 1) and (rain_list[N-1].pos[1][0] < person.pos.x + 1) and (rain_list[N-1].pos[1][1] > person.pos.y - 2) and (rain_list[N-1].pos[1][1] < person.pos.y +2) and (rain_list[N-1].pos[1][2] > person.pos.z + v_per.z*dt -1) and (rain_list[N-1].pos[1][2] < person.pos.z + v_per.z*dt +1):
                    count = count + 1 # if rain position in 'area of persin', count + 1
                    x = uniform(-1,1) # And then the rain-drop is maked again at random upper-position
                    z = uniform(-40,40)
                    y = uniform(50,80) 
                    rain_list[N-1].pos[0] = vector(x,y,z)
                    rain_list[N-1].pos[1] = vector(x, y-1, z)

            else: #if a rain-drop is located z=0, maked again at random upper-position
                x = uniform(-1,1)
                z = uniform(-40,40)
                y = uniform(50,80)
     
                rain_list[N-1].pos[0] = vector(x,y,z)
                rain_list[N-1].pos[1] = vector(x, y-1, z)

            N = N-1


        if t > 4: # After 4 seconds, 'person move' and 'traffic light' changed(we have to do this because of equally drop after few seconds)
            move()
            traffic_light = sphere(pos = (-10,8,-41), radius = 1.5, color = (0,1,0))
            traffic_light = sphere(pos = (10,8,41), radius = 1.5, color = (0,1,0))
            if person.pos.z > 44:  #If person reach target, go back starting point
                person.pos.z = -65
                print count
                count = 0
                i = i + 1

        t = t + dt

        # initialization again because N is 0 due to upper while loop
        N = k

        # Operate same loop while i = n
        if i == n:
            break     


####################################################################################
def var():
    E1 = int(e1.get())
    E2 = int(e2.get())
    E3 = int(e3.get())
    print "(loop : %d, person velocity : %d, rain number : %d)" % (E1, E2, E3)
    main(E1,E2,E3) 
    # E1 = n(how many times is it to operate) , E2 = Z(velocity of person) , E3 = k(rain drop number)



master = Tk()
Label(master, text = "\tLoop").grid(row=0)
Label(master, text = "\tVelocity of Person").grid(row=1)
Label(master, text = "\tRain Number").grid(row=2)
Label(master, text = "ex ) Rain number : 200 -> 0.2mm/h(light rain)").grid(row=3, column = 1)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)

e1.grid(row = 0, column = 1)
e2.grid(row = 1, column = 1)
e3.grid(row = 2, column = 1)

Button(master, text = 'Start', command = var).grid(row = 4, column = 1, sticky = W, pady = 4)

mainloop()








