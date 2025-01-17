import math

def main():
    name="#1 picnic"
    radius = 6.83
    heigth = 10.16   
    can_eff(name,radius,heigth)
    
def can_eff(name, radius, height):
    volumen=can_vol(radius,height)
    area=can_area(radius,height)
    eff_storage = volumen/area
    print(f"{name} the volume is = {volumen:.2f} and the area is={area:.2f} and the efficiency storage is= {eff_storage:.2f}")
    
def can_vol(radius,height):
    vol= math.pi * radius ** 2 * height  
    return vol  
def can_area(radius,heigth):
    area= 2 * math.pi * radius *(radius + heigth)    
    return area





main()    
