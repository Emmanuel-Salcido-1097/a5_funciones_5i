print("funciones creadas por el usuario")
# Las funciones

# Lista
def Mi_lista():
    print("---Lista---")
    amigos=["Homero","Paty","Lety"]
    for nava in amigos:
        print(nava)

# Tupla
def Mi_tupla():
    print("---Tupla---")
    amigos=("Angel","David Munoz Salazar","Kevin")
    for ele in amigos:
        print(ele)

# Conjunto
def Mi_conjunto():
    print("---Conjunto---")
    amigos={"David Martinez","Roberto Perez","Montelongo"}
    for ele in amigos:
        print(ele)

# Diccionario
def Mi_diccionario():
    print("---Diccionario---")
    estedicc={
        "Amigo 1" : "Jhoana",
        "Amigo 2" : "Ale",
        "Amigo 3" : "Sky"
    }
    for key, value in estedicc.items():
        print(f"{key} = {value}")
        
# Llamadas a funciones
Mi_lista()
Mi_tupla()
Mi_conjunto()
Mi_diccionario()