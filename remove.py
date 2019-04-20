with open("MGKlyrics.txt", "r") as MGKreader:
    with open ("MGKmodLyrics.txt", "w") as MGKwriter:
        for line in MGKreader:
            if line and line[0] != "[" and line[0] != "\n":
                MGKwriter.write(line)

