def mozisuu(t):
    mozi = tuple(t)
    box = [[chr(i) for i in range(97, 97+26)]]
    n_box = [ 0 for i in range(26)]

    for i in mozi:
        t = box[0].index(i)
        n_box[t] = n_box[t] + 1

    for i in range(26):
        print(box[0][i], 'is' , n_box[i])
            
            
    
    
