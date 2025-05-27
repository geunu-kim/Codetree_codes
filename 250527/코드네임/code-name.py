MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.

lowest_score = min(scores)
lowest_score_index = scores.index(lowest_score)

print(codenames[lowest_score_index],lowest_score)