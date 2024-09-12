print("Ejemplos de funciones")
# declarando funciones
def hola():
    print("Alguien uso la funcion hola")

def chat(mensa):
    print(f"Chat {mensa}")

def ellacontesta(mensa):
    print(f"chat ella: {mensa}")
    
def escribetunombre(ap,n):
    print(f"Tu nombre completo es: {n} {ap}")

def suma(a,b):
    s=a+b
    return s

def resta(a,b):
    r=a-b
    return r

def multiplicacion(a,b):
    m=a*b
    return m

def division(a,b):
    d=a/b
    return d

# llamada funciones
hola()
chat("que bonita estas")
ellacontesta("gracias")
escribetunombre("rivera","andres")
print("operacion suma")
c1=int(input("Ingresa un numero"))
c2=int(input("Ingresa un numero"))
damesuma=suma(c1,c2)
print(f"La suma de {c1} + {c2} = {damesuma}")
print("operacion resta")
c1=int(input("Ingresa un numero"))
c2=int(input("Ingresa un numero"))
dameresta=resta(c1,c2)
print(f"La resta de {c1} - {c2} = {dameresta}")
print("operacion multiplicacion")
c1=int(input("Ingresa un numero"))
c2=int(input("Ingresa un numero"))
damemultiplicacion=multiplicacion(c1,c2)
print(f"La multiplicacion de {c1} * {c2} = {damemultiplicacion}")
print("operacion division")
c1=int(input("Ingresa un numero"))
c2=int(input("Ingresa un numero"))
damedivision=division(c1,c2)
print(f"La division de {c1} / {c2} = {damedivision}")

