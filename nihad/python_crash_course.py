s = 'Hi there Sam!'
print(s.split())

planet = "Earth"
diameter = 12742
print("The diameter of {} is {} kilometers.".format(planet,diameter))

lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2][0])

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][3])

def domainGet(email):
    return email.split('@')[-1]
print(domainGet('user@domain.com'))

def findDog(st):
    return 'dog' in st.lower().split()
print(findDog('Is there a dog here?'))

def countDog(st):
    count = 0
    for word in st.lower().split():
        if word == 'dog':
            count += 1
    return count
print(countDog('This dog runs faster than the other dog dude!'))

seq = ['soup','dog','salad','cat','great']
print(list(filter(lambda word: word[0]=='s',seq)))

def caught_speeding(speed, is_birthday):
    
    if is_birthday:
        speeding = speed - 5
    else:
        speeding = speed
    
    if speeding > 80:
        return 'Big Ticket'
    elif speeding > 60:
        return 'Small Ticket'
    else:
        return 'No Ticket'
print(caught_speeding(81,True))
print(caught_speeding(81,False))
