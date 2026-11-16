def find_best_advantage(Advs):
    buy = 0
    sell = 0
    advantages = []
    for i in range(len(Advs)):
        buy = Advs[i]
        for j in range(len(Advs)):
            sell = Advs[j]
            advantages.append( sell - buy)
    bestAdv = max(advantages)
    return bestAdv     

listOfAdv = list(map(int,input().split()))
theBestAdv = find_best_advantage(listOfAdv)
print(theBestAdv)