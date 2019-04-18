import time
import random
import operator
count = 48000
print ('There is allways more than one way to solve a problem. Some are a little bit faster than others and some will slow down your program. Here are a few examples.\n')
print ('Time in milliseconds')
print('==================\n')
print ('Add {} random numbers\n'.format(count))

starttime = (time.time())
sum = 0
for i in range (count):
    sum = sum + random.randint(0, 100)
time1 = round(1000 * (time.time() - starttime))

starttime = (time.time())
sum = 0
for i in range (count):
    sum += random.randint(0, 100)
time2 = round(1000 * (time.time() - starttime))

starttime = (time.time())
sum = 0
for i in range (count):
    operator.add(sum, random.randint(0, 100))
time3 = round(1000 * (time.time() - starttime))

print('{:<12}|{:<12}|{}'.format('b = b + x', 'b += x', 'operator.add()'))
print('{:<12}|{:<12}|{}\n\n'.format(time1, time2, time3))

print ('Create a 2D array of size {} x {}\n'.format(int(count/100), int(count/100))
)

starttime = (time.time())
lst1 = []
lst2 = []
for i in range (int(count/100)):
    for j in range(int(count/100)):
        lst2.append(random.randint(1, 100))
    lst1.append(lst2)
    lst2 = []
time1 = round(1000 * (time.time() - starttime))

starttime = (time.time())
lst3 = [[random.randint(1,100) for i in range (int(count/100))] for j in range (int(count/100))]
time2 = round(1000 * (time.time() - starttime))

print('{:<12}|{}'.format('for-loop', 'list comp.'))
print('{:<12}|{}\n\n'.format(time1, time2))

print('Fill a list with {} random numbers\n'.format(count))

starttime = (time.time())
lst4 = []
for i in range (count):
    lst4.append(random.randint(0,100))
time1 = round(1000 * (time.time() - starttime))

starttime = (time.time())
lst5 = [random.randint(0, 100) for i in range (count)]
time2 = round(1000 * (time.time() - starttime))

print('{:<12}|{}'.format('for-loop', 'list comp.'))
print('{:<12}|{}\n\n'.format(time1, time2))

print ('Filter odd numbers from a list of {} random numbers\n'.format(count))

starttime = (time.time())
filterlist = []
for i in lst4:
    if i % 2 != 0:
        filterlist.append(i)
time1 = round(1000 * (time.time() - starttime))

starttime = (time.time())
filterlist = list(filter(lambda x: x % 2 != 0, lst4))
time2 = round(1000 * (time.time() - starttime))

print('{:<12}|{}'.format('for-loop', 'filter(lambda)'))
print('{:<12}|{}\n\n'.format(time1, time2))

print ('Double all elements in a list of {} random numbers\n'.format(count))

starttime = (time.time())
doublelist = []
for i in lst4:
    doublelist.append (i *2)
time1 = round(1000 * (time.time() - starttime))

starttime = (time.time())
doublelist = list(map(lambda x: x * 2, lst4))
time2 = round(1000 * (time.time() - starttime))

print('{:<12}|{}'.format('for-loop', 'map(lambda)'))
print('{:<12}|{}\n\n'.format(time1, time2))

print ('Find all combinations of 6 letters\n'.format(count))
abc = ('a','b','c','d','e', 'f')

starttime = (time.time())
perms = []
for a in abc:
    for b in abc:
        for c in abc:
            for d in abc:
                for e in abc:
                    for f in abc:
                        perms.append('{}{}{}{}{}{}'.format(a, b, c, d, e, f))
time1 = round(1000 * (time.time() - starttime))

starttime = (time.time())
perms = ['{}{}{}{}{}{}'.format(a, b, c, d, e, f) for a in abc for b in abc for c in abc for d in abc for e in abc for f in abc]
time2 = round(1000 * (time.time() - starttime))

print('{:<12}|{}'.format('for-loop', 'list comp.'))
print('{:<12}|{}'.format(time1, time2))