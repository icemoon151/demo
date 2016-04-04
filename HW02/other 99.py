for i in range(9, 0,-1):
        for k in range(i-9,1):
                print(end='        ') 
        for j in range(i,0,-1):
                print('{0:1}x{1:1}={2:2}\t'.format(i, j, i*j), end='')
        print()

