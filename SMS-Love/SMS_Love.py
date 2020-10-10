arr = list(input().rstrip())
word = list(input().rstrip())

n = len(arr)
m = len(word)
count = [0 for i in range(128)]
for i in range(n - m):
    if ord(arr[i]) != 91:
        count[ord(arr[i])] += 1
ans = 0
for j in range(m):
    if ord(arr[n-m+j]) != 91:
        count[ord(arr[n-m+j])] += 1
    if ord(word[j]) != 91:
        ans += count[ord(word[j])]
    if ord(arr[j]) != 91:
        count[ord(arr[j])] -= 1
print(ans)
    
