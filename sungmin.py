def num_vowel(f):
    a=0
    for i in f:
        if i in 'aeiou':
            a+=1
    return a
b = input()
k=num_vowel(b)
print(k)