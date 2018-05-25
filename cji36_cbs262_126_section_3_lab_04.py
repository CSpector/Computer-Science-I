# Lab  04 Grade calculator
# Corey Imperatrice, Colton Spector
# cji36, cbs262
# 9/28/2017
# Section 3

def main():
    # Lists for score and Max score
    hwScore = [39,40,29,40,0,5]
    hwMax = [40,40,40,40,40,5]
    quizScore = [10,10,9,2,10,10,10]
    quizMax = [10,10,10,10,10,10,10]
    testScore = [293,284,300]
    testMax = [300,300,300]
    # Average score and max
    score_list = hwScore + quizScore + testScore
    max_list = hwMax + quizMax + testMax
    # Weighted for each category
    hwWeight = .2
    quizWeight = .2
    testWeight = .6
    # Average for HW
    homework_avg = average(hwScore, hwMax)
    homework_percent = letter_grade(homework_avg)
    homework_weight = average_weighted(hwScore, hwMax, hwWeight)
    # Average for quizzes
    quiz_avg = average(quizScore, quizMax)
    quiz_percent = letter_grade(quiz_avg)
    quiz_weight = average_weighted(quizScore, quizMax, quizWeight)
    # Average for tests
    test_avg = average(testScore, testMax)
    test_percent = letter_grade(test_avg)
    test_weight = average_weighted(testScore, testMax, testWeight)
    # Total grade
    total_grade = homework_weight + quiz_weight + test_weight
    total_percent = letter_grade(total_grade)
    # Print statements
    print("Homework Grade: " + str(homework_avg) + " (" + homework_percent + ")")
    print("Quiz Grade: " + str(quiz_avg) + " (" + quiz_percent + ")")
    print("Test Grade: " + str(test_avg) + " (" + test_percent + ")")
    print("Final Grade: " + str(total_grade) + " (" + total_percent + ")")
# Define average function
def average(score_list, max_list):
    total_score = sum(score_list)
    max_score = sum(max_list)
    score_average = round(100 * (total_score / max_score))
    return score_average
# Define letter grade
def letter_grade(percent):
    if percent >= 90:
        grade = "A"
    elif percent >= 80:
        grade = "B"
    elif percent >= 70:
        grade = "C"
    elif percent >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade
# Define average weighted
def average_weighted(score_list, max_list, weight):
    score_average = average(score_list, max_list)
    weighted_total = score_average * weight
    return round(weighted_total)
# Call the main function
main()
