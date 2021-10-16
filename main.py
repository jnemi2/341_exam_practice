

def filter_odds(number_list):
    aux = []
    for n in number_list:
        if n%2 == 1 and n not in aux:
            aux.append(n)
    aux.sort()
    return aux


print(filter_odds([1,7,7,75,2,8,10,4,3,7,77]))
