def read(filename):
    file = open(filename, 'r')
    data = file.read()
    file.close()
    return data


def write(filename, data):
    file = open(filename, 'w')
    file.write(data)
    file.close()
