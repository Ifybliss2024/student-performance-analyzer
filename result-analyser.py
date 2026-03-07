# A script to analyse ENG 401 (COMPUTATIONAL METHODS) RESULTS

# 1. The data scores for Eng 401
Scores = [81, 27, 50, 66, 40, 38, 40, 29, 40, 45, 71, 47, 61, 62, 77, 54, 38,
46, 48, 48, 62, 40, 42, 33, 36, 62, 40, 58, 42, 80, 43, 59, 70, 0, 60, 41, 48,
46, 40, 32, 37, 68, 44, 61, 51, 37, 74, 34, 40, 60, 40, 46, 33, 40, 49, 43, 55, 
44, 48, 46, 55, 50, 58, 42, 65, 43, 78, 66, 40, 57, 42, 45, 56, 43, 46, 83, 76, 
40, 55, 55, 79, 88, 73, 71, 50, 55, 55, 41, 42, 80, 72, 70, 40, 44, 46, 68, 55,
61, 38, 57, 60]

 # 2. General Calculations
total_score = sum(Scores)
number_of_scores = len(Scores)
average_value = total_score / number_of_scores
highest_value = max(Scores)
lowest_value = min(Scores)

# 3. Counting how many students who passed
passing_count = 0
for c in Scores:
  if c>= 40:
    passing_count += 1

# 4. Set counters for each grade
Grade_count = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}
for g in Scores:
  if g >= 70:
    Grade_count["A"] += 1
  elif g>= 60:
    Grade_count["B"] +=1
  elif g>= 50:
    Grade_count["c"] +=1
  elif g>= 45:
    Grade_count["D"] +=1
  elif g>= 40:
    Grade_count["E"] +=1
  else:
    Grade_count["F"] +=1

# 5. Display the results
print("2024/2025 ENG 401 FIRST SEMESTER RESULTS PERFORMANCE ANALYSIS")
print("-" * 35)
print(f"Number of Students: {number_of_scores}")
print(f"Average Score: {average_value:.2f}")
print(f"Highest Score: {highest_value}")
print(f"Lowest Score: {lowest_value}")
print(f"Number of students who passed: {passing_count}")
print("-" * 35)
print("Grade distribution:")
for grade, count in Grade_count.items():
  print(f"Grade {grade}: {count} students")
print("-" * 35)
    
    
