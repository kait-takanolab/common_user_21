from random import sample, shuffle
from time import time

numQuiz = 5
height = 4
width = 5
numSample = height * width

print('同じ数字を見つけて入力してください。')
start = time()
for q in range(numQuiz):
    print('{}/{}問目'.format(q + 1, numQuiz))
    print('-' * 16)

    data = sample(range(1, 100), numSample - 1)
    ans = data[0]
    data.append(ans)
    shuffle(data)
    i = 0
    for y in range(height):
        for x in range(width):
            print('{:4}'.format(data[i]), end='')
            i += 1
        print()
    while True:
        a = int(input('ans: '))
        if a == ans:
            print('Yes!')
            break
        else:
            print('No.')
    print()
end = time()
print('All cleared.')
print('Time: {}[s]'.format(end - start))
print('Bye')
