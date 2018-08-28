disciplines = ['maths', 'physics', 'chemistry']
msg = "Please enter scores for " + str(disciplines) + " respectively (0..100): "

scores = []
while len(scores) < len(disciplines):
    scores = list(map(
        lambda x: 0 if int(x) < 0 else 100 if int(x) > 100 else int(x),
        [x for x in input(msg).split()]
    ))

all_passed = True

for i in range(len(disciplines)):
    score = scores[i]
    if score < 35:
        print("You've failed %s" % (disciplines[i],))
        all_passed = False
        break

if all_passed:
    average = int(sum(scores) / len(scores))
    grade = 'C' if average <= 59 else 'B' if average <= 69 else 'A'

    print("Your final grade is %s (your average is %s)" % (grade, average))

else:
    print("Re-take the failed exam.")
