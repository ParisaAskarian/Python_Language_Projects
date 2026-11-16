def can_rabit_finish_the_line(line):
    sucessfuly = True
    currentPosition = 0
    finish = len(line) - 1
    jumpRange = 0
    while currentPosition != finish:
        i = currentPosition
        jumpRange = line[i]
        if jumpRange >= (finish - currentPosition) or jumpRange == 0:
            break
        currentPosition += jumpRange
    if currentPosition < finish and jumpRange < ( finish - currentPosition ):
        sucessfuly = False
    return sucessfuly        

line =list(map(int, input().split()))
rabitSucessfuly = can_rabit_finish_the_line(line)
print(rabitSucessfuly)