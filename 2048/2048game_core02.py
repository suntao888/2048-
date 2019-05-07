def zero_to_end(list_target):
    new_list = [item for item in list_target if item != 0]
    new_list += [0] * list_target.count(0)
    # return new_list
    # list_target = new_list  #此时修改的是变量，不是传入的对象
    list_target[:] = new_list[:]  # 此时修改的是对象


# def zero_to_end(list_target):
#     for item in list_target:
#         if item == 0:
#             list_target.remove(0)
#             list_target.append(item)
def print_atlas(list_atlas):
    # 00   01   02   03
    for r in range(len(list_atlas)):
        for c in range(len(list_atlas[r])):
            print(list_atlas[r][c], end=" ")
        print()


atlas01 = [
    [2, 0, 0, 2],
    [8, 0, 4, 4],
    [2, 2, 0, 4],
    [0, 2, 4, 0],
]
print_atlas(atlas01)


def merge(list_target):
    zero_to_end(list_target)
    for i in range(len(list_target) - 1):
        if list_target[i] != 0 and list_target[i] == list_target[i + 1]:
            list_target[i] += list_target[i + 1]
            list_target[i + 1] = 0
    zero_to_end(list_target)


def print_atlas(list_atlas):
    for r in range(len(list_atlas)):
        for c in range(len(list_atlas[r])):
            print(list_atlas[r][c], end=" ")
        print()


def move_up(atlas):
    for c in range(4):
        list_merge = []
        for r in range(4):
            list_merge.append(atlas[r][c])

        merge(list_merge)

        for r in range(4):
            atlas[r][c] = list_merge[r]


def move_left(atlas):
    for r in range(4):
        list_merge = []
        for c in range(4):
            list_merge.append(atlas[r][c])

        merge(list_merge)

        for c in range(4):
            atlas[r][c] = list_merge[c]


def move_down(atlas):
    for c in range(4):
        list_merge = []
        for r in range(3, -1, -1):
            list_merge.append(atlas[r][c])

        merge(list_merge)

        for r in range(3, -1, -1):
            atlas[r][c] = list_merge[3 - r]


def move_right(atlas):
    for r in range(4):
        list_merge = []
        for c in range(3, -1, -1):
            list_merge.append(atlas[r][c])

        merge(list_merge)

        for c in range(3, -1, -1):
            atlas[r][c] = list_merge[3 - c]



while True:
    shell = input("请输入玩家指令wsad:")
    if shell=="w":
        move_up(atlas01)
        print_atlas(atlas01)
    elif shell=="s":
        move_down(atlas01)
        print_atlas(atlas01)
    elif shell=="a":
        move_left(atlas01)
        print_atlas(atlas01)
    elif shell=="d":
        move_right(atlas01)
        print_atlas(atlas01)
    else:
        print("输入错误")