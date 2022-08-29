print("The Test Score Program")
print("Enter 'x' to Exit\n")
total = 0
num_scores=0
score_list = []
# score_tuple = ()
while True:
    score = input("Enter Test Score: ")
    if score == 'x':
        break
    score = int(score)
    score_list.append(score)


score_tuple = tuple(score_list)

print(f"\nTotal:\t\t\t\t{sum(score_tuple)}")
print(f"Number of Score:\t{len(score_tuple)}")
print(f"Average Scores:\t\t{sum(score_tuple)//len(score_tuple)}")
print(f"Low Score:\t\t\t{min(score_tuple)}")
print(f"High Score:\t\t\t{max(score_tuple)}")

tuple_len = len(score_tuple)
if tuple_len%2==0:
    median_cal = (tuple_len)//2
else:
    median_cal = (tuple_len+1)//2
print(f"Median Score: {score_list[median_cal-1]}")
