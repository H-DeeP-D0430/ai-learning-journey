name=['Einstein','Newton','Tesla']
print(name[0])
print(name[1])
print(name[2])

print(f'hello,{name[0]}')
print(f'hello,{name[1]}')
print(f'hello,{name[2]}')

print(f'尊敬的 {name[0]},邀请您共进晚餐。')
print(f'尊敬的 {name[1]},邀请您共进晚餐。')
print(f'尊敬的 {name[2]},邀请您共进晚餐。')

out_name=name.pop(1)
print(f'由于{out_name}有事不能来，名单更改。')
name.append('Hawking')
print(name)

name.insert(0,'Curie')
name.insert(2,'DaVinci')
name.append('Turing')
print(name)

del name[2]
del name[2]
del name[2]
del name[2]
print(name)