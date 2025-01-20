import os

path = input()

all_of = {}


def get_dir_size(ph):
    total_size = 0
    k = ''
    for currentdir, dirs, files in os.walk(ph):
        for y in files:
            print(ph, y, k)
            total_size += os.path.getsize(ph + '/' + y)
        for k in dirs:
            total_size += get_dir_size(ph + '/' + k)

    return total_size

def human_read_format(size):
    kb = size // 1024
    if kb == 0:
        return f"{size}Б"
    else:
        mb = kb // 1024
        if mb == 0:
            return f"{kb + round((size - kb * 1024) / 1024)}КБ"
        else:
            gb = mb // 1024
            if gb == 0:
                return f"{mb + round((kb - mb * 1024) / 1024)}МБ"
            else:
                return f"{gb + round((mb - gb * 1024) / 1024)}ГБ"


for currentdir, dirs, files in os.walk(path):
    for i in files:
        all_of[i] = os.path.getsize(path + '/' + i)
    for j in dirs:
        all_of[j] = get_dir_size(path + '/' + j)
    break

sorty = sorted(all_of.items(), key=lambda x: -x[1])

for b in sorty[:10]:
    print(f'{b[0]}\t{human_read_format(b[1])}')
