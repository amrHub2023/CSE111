def main():
#  b=test_min()   
#  if test_min() is True:
    #  print(f"se encontro el  menor",b)
#  else:     
    #  print(f"error",b)
    
   fahr=int(input("enter a fahr number: "))
   res=cels_from_fahr(fahr)
   print(res)

def test_min():
  a=min(7, -3, 0, 2)  
  assert min(7, -3, 0, 2) == -3       
  return a
# weather.py
def cels_from_fahr(fahr):
  """Convert a temperature in Fahrenheit to
  Celsius and return the Celsius temperature.
  """
  cels = (fahr - 32) * 5 / 9
  return cels
main()            