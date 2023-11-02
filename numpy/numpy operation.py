import numpy as np

# 40 到 100 的数据 10行5列
score = np.random.randint(40, 120, (10, 5))

print(f'score:{score}\n')

test_score = score[6:, 0:5]

test_k = test_score > 60

test_score[test_score > 60] = 1

print(f'test_core:{test_score}\n')

temp = score[:4, :4]
temp = np.where(temp > 60, 1, 0)

print(f'temp:{temp}\n')

temp = score[:4, :4]
temp = np.where(np.logical_and(temp > 60, temp < 100), 1, 0)

print(f'temp:{temp}\n')
