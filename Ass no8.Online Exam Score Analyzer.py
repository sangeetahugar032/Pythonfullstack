scores=[78,85,92,66,88]
total_score=sum(scores)
average_score=total_score/len(scores)
above_average_count=0
for score in scores:
    if score>average_score:
        above_average_count+=1
print("Total Score:",total_score)
print("Average Score:",average_score)
print("Scores Above Average:",above_average_count)
