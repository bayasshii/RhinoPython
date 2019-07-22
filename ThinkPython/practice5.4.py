def tri(a, b, c):
    box = [a, b, c]
    box.sort()
    if box[2] < box[0] + box[1] :
        print ('Yes, you can make tri.')
    else:
        print ('No, you cannot make tri.')
    
