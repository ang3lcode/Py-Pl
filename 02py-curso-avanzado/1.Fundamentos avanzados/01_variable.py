x = 100

def local_funcion( ):
   x = 10 #variable local
   print(f'El calor de la variable es {x}')

def show_global( ):
   print(f'el calor de la cariable es {x}')


# local_funcion()
show_global()
# print(x) #genera error

# ejemplo inner_ourter
x = 'global' #variable global

# funcion externa
def outer_funcion( ):
    x = 'enclosing'
    #funcion interna
    def inner_funcion( ):
        x = 'local'
        print( x )
    
    inner_funcion()
    print( x )

outer_funcion( )
print(x)


#ejemplo global
x = 5 #variable global

def modify_global( ):
    global x 
    x += 3
    print( f'valor modificado: { x }')

modify_global()
print( x )

#nonlocal
def outer_funcion():
    x = 'enclosing'
    def inner_funcion( ):
        nonlocal x 
        x = 'modified'
        print (f'El valor en inner es: { x }')
    inner_funcion()
    print( f'el valor outer: { x } ')
outer_funcion()