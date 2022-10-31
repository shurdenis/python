
def cacluate(*num):
    y = []
    x = sum(num) / len(num)
    for i in num:
        if i > x:
            list.append(i)
    return x, y
        
