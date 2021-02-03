def reversal(w):

    reverse = w[0]
    for i in range(1,len(w)):
        reverse = w[i] + reverse
        
    return reverse

print(reversal("Mississippi"))

