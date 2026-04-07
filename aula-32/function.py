fahren = float(input("Digite a temperatura em Fahrenheit: "))

def conversor(fahren):
    celcius = ((fahren-32*(5/9)))
    kelvin = (5/9*(fahren-32))+273.15
    print(f"A conversão da temperatura {fahren}")
    print(f"Temos as temperaturas {celcius:.2f} e {kelvin:.2f}")

conversor(fahren)