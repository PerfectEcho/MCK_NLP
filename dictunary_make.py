import string
with open("MGKmodlyrics.txt", "r") as MGKreader:
    with open ("MGKdicLyrics.txt", "w") as MGKwriter:
        text = set(MGKreader.read().split(" "))
        for word in text:
            if word == "" or word =="\n":
                continue
            for punc in string.punctuation:
                word = word.replace(punc,"")
            MGKwriter.write(word+"\n")