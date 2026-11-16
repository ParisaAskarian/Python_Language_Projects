num = input()

def num_things(number):

    lengh = len(number)
    print(len(number))

    count = 0
    s_m = 0
    for i in range(lengh):
        count += int(number[i])
        if i%2 == 0:
            s_m += int(number[i])
        else:
            s_m -= int(number[i])      
         
    print(count)
    print(s_m)

num_things(num)
