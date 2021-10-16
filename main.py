import datetime


def load_products():
    products = []
    file = open("productos.txt", "rt")
    line = file.readline().strip().split(", ")
    while len(line) > 0:
        new_dict = {}
        new_dict.setdefault('id', int(line[0]))
        new_dict.setdefault('descripcion', line[1][1:-1])
        new_dict.setdefault('precio', float(line[2]))
        products.append(new_dict)
        line = file.readline().strip().split(", ")
    file.close()
    return products


def get_price(product_id):
    products = load_products()
    price = None
    for p in products:
        if p['id'] == product_id:
            price = p['precio']
            break
    return price, datetime.datetime.now()

