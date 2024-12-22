def back(dir):
    with open(dir + 'user1.dat', 'rb') as f:
        data = f.read()
        with open(dir + 'user1.dat.bak', 'wb') as bf:
            bf.write(data)


def crack_other_games(dir):
    back(dir)
    with open(dir + 'user1.dat', 'r+b') as f:
        f.seek(12)
        after_data = f.read()
        f.seek(12)
        f.write(b'\x01')
        f.write(after_data[1:])


def crack_survival_game(dir):
    back(dir)
    with open(dir + 'user1.dat', 'r+b') as f:
        index = 16
        f.seek(64)
        after_data = f.read()
        while index <= 52:
            f.seek(index)
            if index >= 36:
                f.write(b'\x0a')
                index += 4
                continue
            f.write(b'\x05')
            index += 4
        f.write(after_data[1:])


def crack_zombie_doctorate(dir):
    back(dir)
    with open(dir + 'user1.dat', 'r+b') as f:
        f.seek(4)
        after_data = f.read()
        f.seek(4)
        f.write(b'\x32')
        f.write(after_data[1:])


def crack_coins(dir):
    back(dir)
    with open(dir + 'user1.dat', 'r+b') as f:
        f.seek(10)
        after_data = f.read()
        f.seek(8)
        f.write(b'\xff')
        f.seek(9)
        f.write(b'\xff')
        f.seek(10)
        f.write(b'\xff')
        f.write(after_data[1:])


def crack_mini_game(dir):
    back(dir)
    with open(dir + 'user1.dat', 'r+b') as f:
        index = 76
        f.seek(148)
        after_data = f.read()
        while index <= 148:
            f.seek(index)
            f.write(b'\x01')
            index += 4
        f.write(after_data[1:])


def crack_puzzle_game(dir):
    back(dir)
    with open(dir + 'user1.dat', 'r+b') as f:
        index = 216
        f.seek(248)
        after_data = f.read()
        while index <= 248:
            f.seek(index)
            f.write(b'\x01')
            index += 4
        f.write(after_data[1:])

        next_index = 256
        f.seek(288)
        after_data = f.read()
        while next_index <= 288:
            f.seek(next_index)
            f.write(b'\x01')
            next_index += 4
        f.write(after_data[1:])
