with open("initial.txt", "r") as input:
    with open("copy.txt", "w") as output:
        for line in input:
            output.write(line)