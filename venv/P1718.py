#니꺼아님
sen = list(input())
key = list(input())
cipher = ""
while len(key) < len(sen):
    key += key
alp = "a b c d e f g j i j k l m n o p q r s t u v w x y z".split()
print(len(alp))
print(len(sen))
for i in range(len(key)):
    for j in range(26):
        print(i,j)
        if key[i] == alp[j]:
            key[i] = j + 1
        if sen[i] == alp[j]:
            sen[i] = j + 1
for m in range(len(key)):
    if sen[m] != " ":
        sen[m] -= key[m]
        if sen[m] <= 0:
            sen[m] += 26
for n in range(len(sen)):
    if sen[n] != " ":
        sen[n] = alp[sen[n]-1]
    cipher += sen[n]
print(cipher)

# key 문자열을 늘렸는데 그 크기만큼 돌리는 반복문에서 key만큼의 인덱스로
# sen 문자열을 접근하면 당연 에러