colors = ['red','orange','yellow','green','blue','navy','purple']

for idx, color in enumerate(colors):
    print(f'무지개의 {idx+1}번째 색은 {color}입니다.')

# zip 이용하는 방법
a = [1,2,3,4,5,6,7]
b = ['red','orange','yellow','green','blue','navy','pruple']

for a, b in zip(a, b):
    print(f'무지개의 {a}번째 색은 {b}입니다.')

print()
print("점수를 입력하세요.\n더이상 점수가 없으면 음수를 아무거나 입력하세요.")
nums = []
sum = 0
temp = True

while temp:
    num = int(input("점수를 입력하세요 >>"))
    if num < 0:
        temp = False
        break
    else:
        nums.append(num)
        sum += num

max = nums[0]
for i in range(len(nums)):
    if nums[i] > max:
        max = nums[i]

min = nums[0]
for i in range(len(nums)):
    if nums[i] < max:
        min = nums[i]

print(f'평균 = {sum/len(nums)}, 최대 = {max}, 최소 = {min}')


