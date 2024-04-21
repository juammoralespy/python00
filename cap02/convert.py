# convert.py
# un programa para convertir celsius a farenthei
# por juan morales

def main():
    celsius = eval(input("Cual es la temperatura en celsius?: "))
    farenheit = 9/5 * celsius + 32
    print("La temperatura en farenthei es de: ", farenheit)

main()
