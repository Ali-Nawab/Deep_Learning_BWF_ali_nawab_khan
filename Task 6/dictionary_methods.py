n1 = {"ali": 10, "nawab": 20, "khan": 30}
n2 = {"bangash": 40, "pathan": 50}

n1.update(n2)
print(n1)
del n1["ali"]
print(n1)
n2.clear()
print(n2)
del n2
# print(n2) it will give error because n2 is deleted.

n1.popitem()
print(n1)

n1.pop("nawab")
print(n1)

playlist = {
    'india': 'bollywood',
    'english': 'very hot',
    'pakistan': 'lollywood',
    'urdu': [{1: 'a', 2: 'b', 3: 'c'}, {4: 'd', 5: 'e', 6: 'f'}, {7: 'g', 8: 'h', 9: 'i'}]
}

print(playlist['urdu'][2])
print(playlist['urdu'][2][8])



values = dict(a=1, b=2, c=3, d=4)
num = {keys: val * 2 for keys, val in values.items()}
print(num)

answer = dict.fromkeys("aeiou", 0)
print(answer)

answer = {count: chr(count) for count in range(65, 91)}
print(answer)


values = dict(a=7, b=8, c=10)
values1 = values.copy()
print(values1)

# from keyloggers.
values = {}.fromkeys([1, 2, 3, 4], 'unknown')
print(values)

instructor = dict(a=5, b=8, c=10)
print(instructor)
person = dict([])
print(person)
person.update(a=5)
print(person)

person.update(instructor)
print(person)