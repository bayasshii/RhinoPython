        
def check_fermat(f):

    abcn_group = []

    f = f+1
    
    for i in range(1, f):
        for j in range(1, f):
                for k in range(1, f):
                    
                    if (i <= j) and (i < k) and (j < k):
                        for l in range(3, f):
                            abcn = [i, j, k, l]
                            abcn_group.append(abcn)     
                    else:
                        pass

    kazu = len(abcn_group)

    for m in range(kazu):
        
        a = abcn_group[m][0]
        b = abcn_group[m][1]
        c = abcn_group[m][2]
        n = abcn_group[m][3]
        
        if ( a**n + b**n == c**n):
            print ('Fermat isnot great.')
        else:
            print ('Fermat is great.')
            print (abcn_group[m])

check_fermat(5)

