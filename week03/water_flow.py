# def main():
    # print("program")


def water_column_height(tower_heights, tank_height):
    print("tower_heights:", tower_heights)
    # h=height_of_waters
    t=tower_heights
    w=tank_height
    h = t + ((3*w)/4)
    print("height_of_water:", h)
    return h
def pressure_gain_from_water_height(height):
    # P is the pressure in kilopascals
    p=998.2   #density of water
    g=9.80665 #acceleration from Earths gravity
    #height of the water column in meters
    P=(p*g*height)/1000
    return P

def pressure_loss_from_pipe(pipe_diameter,pipe_length, friction_factor, fluid_velocity):    
    #P is the lost pressure in kilopascals
    f=friction_factor #is the pipe’s friction factor
    L= pipe_length #is the length of the pipe in meters
    p = 998.2 #is the density of water 998.2 (kilogram / meter3)
    v = fluid_velocity #is the velocity of the water flowing through the pipe in meters / second
    d = pipe_diameter #is the diameter of the pipe in meters
    P = (-f*L*p*v ** 2  ) / 2000*d
    return P

# main()

#ALEJANDRO MORENO