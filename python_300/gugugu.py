for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}", end="\t")
        if j % 3 == 0:
            print()