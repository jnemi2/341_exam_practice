print("Hello, world!")


def filter_numbers(text):
    aux = []
    for word in text.split(" "):
        try:
            aux.append(float(word))
        except ValueError:
            continue
    return aux


print(filter_numbers("Sin despreciar 13.23 mal vio honestidad envidiaron suspirando435.5. Me alfombra arrojo bronce "
                     "lo seguia. El cafe es cuna 3 onda. Si 3.2sacar no ya busca dogma sento. "
                     "Cuarto volado graves iba han. 54.34 tanto"))
