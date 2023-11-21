chaine = "abcdefghijklmnopqrstuvwxyz" * 10

for i in range(1, len(chaine) + 1, 2):
    segment = chaine[:i]
    print(segment.ljust(50))

