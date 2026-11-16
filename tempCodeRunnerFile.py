
            final += str(num%mab)
        else:
            res.append(num % mab)    
        num = num / mab
    print(num)
    if num < 10: