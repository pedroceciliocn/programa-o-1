n = int(input("De o número de linhas com #: "))


for i in range(1, n + 1):
    for j in range(0, i):
        print("#", end='')

    print()


# n = int(input("Dê o número de linhas com #: "))
# hashtag = ""
# for i in range(1, n + 1):
#     hashtag += "#"
#     print(hashtag)
