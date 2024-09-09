print("--Manejo de funciones V1--")
def hola_mundo():
    print("Hola aqui estoy dentro de la funcion")

def Mensa(msg):
    print(msg)
def EscribeNC(Nombre,Apellido):
    print(Nombre,Apellido)
    print(f"Tu nombre completo es {Nombre} {Apellido}")
def suma2numeros(n1,n2):
    s=n1+n2 
    return f"La suma de {n1} + {n2} es de:",s
# Llamando a la funcion
hola_mundo()
Mensa("hola WhatsAPP") # Llama a la funcion Mensa con 1 parametro
print("El profe me sorprendio enviando mensajes") # Llama a mensa con 1 parametro
EscribeNC("Emmanuel","Salcido")
print("Funciones que regresan valores")
print(suma2numeros(7,3))
print(suma2numeros(15,45))