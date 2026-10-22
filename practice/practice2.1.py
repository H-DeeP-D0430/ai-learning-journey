pizzas = ['pepperoni', 'margherita', 'hawaiian']
for pizza in pizzas:
    print(f'I like {pizza} pizza')

print('I really love pizza!')

animals = ['dog', 'cat', 'rabbit']
for animal in animals:
    print(f'A {animal} would make a great pet')

print('Any of these animals would makeagreat pet!')

nums=list(range(1,21))
for num in nums:
    print(num)

numbs=list(range(1,1000_001))
print(sum(numbs))
print(max(numbs))
print(min(numbs))

cubes=list(range(1,20,2))
for cube in cubes:
    print(cube)

thres=list(range(3,31,3))
for thre in thres:
    print(thre)

ns=[n**3 for n in range(1,11)]
for n in ns:
    print(n)

sss=[]
for s in range(1,11):
    ss=s**3
    sss.append(ss)

print(sss)