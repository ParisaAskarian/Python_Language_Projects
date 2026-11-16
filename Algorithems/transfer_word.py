def transfer(w1 = str(),w2 = str()):
    numberOfOperat = 0
    lenghWord1 = len(w1)
    lenghWord2 = len(w2)
    if lenghWord1 > lenghWord2:
        while (lenghWord1 != lenghWord2):
            w1 = w1[:-1]
            numberOfOperat += 1

word1 = input()
word2 = input()