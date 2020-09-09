# GNU General Public License Version 3

def multiplicativeinverse(number):
    # "number" needs to be prime, or the array will contains zeros
    mi = bytearray(number)
    mi[0] = 0
    for a in range(1, number):
        for b in range(a, number):
            if (a * b) % number == 1:
                mi[a] = b
                mi[b] = a
    return bytes(mi)

def euclideanrec(a, b):
    if b == 0:
        return a
    else:
        return euclideanrec(b, a % b)

def euclideanloop(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a
