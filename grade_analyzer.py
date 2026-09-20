
# Test scores in list[]
scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]

# Calculate class statistics variables
total_scores = len(scores)
average = sum(scores) / total_scores
highest = max(scores)
lowest = min(scores)

# tally counters for grades and pass/fail
passing = 0
failing = 0

grade_a = 0
grade_b = 0
grade_c = 0
grade_d = 0
grade_f = 0


# Loop through each score type in list
for score in scores: # Check passing vs failing
    if score >= 60:
        passing = passing + 1
    else: failing = failing + 1

    # Categorize grades by letter
    if score >= 90:
        grade_a = grade_a + 1
    elif score >= 80:
        grade_b = grade_b + 1
    elif score >= 70:
        grade_c = grade_c + 1
    elif score >= 60:
        grade_d = grade_d + 1
    else:
        grade_f = grade_f + 1


# Calculate percentages for amt of grades passing/failing
passing_pct = (passing / total_scores) * 100
failing_pct = (failing / total_scores) * 100

# Header
print("=== Grade Analyzer ===")
print(f"Total scores: {total_scores}")
print(f"Average: {average:.1f}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"Passing: {passing} ({passing_pct:.1f}%)")
print(f"Failing: {failing} ({failing_pct:.1f}%)")

print("\nGrade Distrubution:")
print(f"A: {grade_a} students")
print(f"B: {grade_b} students")
print(f"C: {grade_c} students")
print(f"D: {grade_d} students")
print(f"F: {grade_f} students")

# Add More Scores to gradebook
print("\n--- Add More Scores---")

while True:
    user_input = input("Enter a score (or type 'done' to finish): ")
    if user_input.lower() == "done":
        break

     # Convert input string to an integer and update list
    try:
        new_score = int(user_input)
    except ValueError:
        print("Please enter valid entry")
        continue

     # Add score to list
    scores.append(new_score)

    # Recalculate and display the updated average
    new_average = sum(scores) / len(scores)
    print(f"Updated average: {new_average:.1f}")

# Final print statement after loop exists
final_average = sum(scores) / len(scores)
print(f"\nFinal Average: {final_average:.1f}")
