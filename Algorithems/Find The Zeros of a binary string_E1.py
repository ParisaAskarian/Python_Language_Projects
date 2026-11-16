def find_the_number_of_zeros(w):
    k = len(w)
    if k  == 1:
        if w[0] == '1':
            return 0
        else:
            return 1    
    mid = int(k/2)    
    rightZeros = find_the_number_of_zeros(w[mid:k])
    if '0' in w[0:mid]:
        leftZeros = find_the_number_of_zeros(w[0:mid])
        return leftZeros + rightZeros
    return rightZeros    

S = input()
numberOfZeros = find_the_number_of_zeros(S)
print(numberOfZeros)