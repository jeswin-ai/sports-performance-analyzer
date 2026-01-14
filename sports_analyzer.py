# Sports Performance Analyzer

player_name = input("Enter player name: ")

scores = []
matches = int(input("Enter number of matches: "))

for i in range(matches):
    score = int(input(f"Enter score for match {i+1}: "))
    scores.append(score)

total_score = sum(scores)
average_score = total_score / matches

print("\n--- Performance Report ---")
print("Player:", player_name)
print("Total Score:", total_score)
print("Average Score:", average_score)

if average_score >= 80:
    print("Performance: Excellent")
elif average_score >= 50:
    print("Performance: Good")
else:
    print("Performance: Needs Improvement")
