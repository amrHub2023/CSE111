>>> d = {'uno': 1, 'dos': 2, 'tres': 3}
>>> for e in d:
...     print(e)
... 
uno
dos
tres

# Recorrer las claves del diccionario
>>> for k in d.keys():
...     print(k)
...     
uno
dos
tres

# Recorrer los valores del diccionario
>>> for v in d.values():
...     print(v)
...     
1
2
3

# Recorrer los pares clave valor
>>> for i in d.items():
...     print(i)
...     
('uno', 1)
('dos', 2)
('tres', 3)