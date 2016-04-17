guess_me=7
start=1

while start<guess_me:
    print('too low')
    start+=1
    if start==guess_me:
        print('found it')
        start+=1
    if start>guess_me:
        print('oops')
    
    
