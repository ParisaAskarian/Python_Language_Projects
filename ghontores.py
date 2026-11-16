def ghontores(num, mab):
    number = ''
    if num != 0:
        alph = { 10: 'A', 11: 'B', 12:'C', 13:'D', 14:'E', 15: 'F'}

        res = []
        final = ''
        
        while num >= mab:
            if num % mab < 10:
                final += str(num%mab)
            else:
                res.append(num % mab)    
            num = num // mab
    
        if num < 10:
            final += str(num)
        else:
            res.append(num) 

        j = len(final) - 1
        while j >= 0 :
            number += final[j]
            j -= 1

        for item in res:
            for key, val in alph.items():
                if key == item:
                    number += val                       
    else:
        number = '0'
    print(number)

number , mabna = map(int,input().split())
ghontores(number, mabna)