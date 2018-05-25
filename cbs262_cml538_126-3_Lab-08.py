# Lab 08 - Grade Calculator II
# Colton Spector and Courtney Richmond
# cbs262 and cml538
# 10-26-2017
# Lab Section - 03


# FROM LAB 04 - Grade Calculator
# Function finds the average between the two parameters
# score_list is expected to be the list that has the scores the user
# received. max_list is expected to be the list that contains
# the total possible points that the user could have earned
def average(score_list, max_list):
    # finds the sum of the score_list
    sum_points_earned = sum(score_list)
    # finds the sum of the max_list
    sum_max_points = sum(max_list)

    # calculates the average of the score_list by taking the total
    # of the list and dividing by the length of score_list
    average_points_earned = sum_points_earned / (len(score_list))
    # works the same as average_points_earned
    average_max_points = sum_max_points / (len(max_list))

    # returns the average between the amount of points earned
    # and the max possible points that could have been earned
    return (average_points_earned) / (average_max_points)


# this function will print out a letter grade
# based upon what percent is passed into the parameter
def letter_grade(percent):
    # returns A if percent is greater than 90
    if percent >= 0.9:
        return "A"
    # returns B if percent is greater than 80 but less than 89
    elif percent >= 0.80 and percent <= 0.89:
        return "B"
    # returns C if percent is greater than 70 but less than 79
    elif percent >= 0.70 and percent <= 0.79:
        return "C"
    # returns D if percent is greater than 60 but less than 69
    elif percent >= 0.60 and percent <= 0.69:
        return "D"
    # returns F if percent is lower than 59
    elif percent <= 0.59:
        return "F"
    # this branch is meant to catch anything that the program cannot
    # utilze and automatically will print out a C
    else:
        print("Not a valid input")
        return "C"


# function uses the average() function already defined
# parameters are similar to the average() function but also includes
# the weight parameters
def average_weighted(score_list, max_list, weight):
    # uses the average() function to find the average between score_list
    # and max_list
    average_score = average(score_list, max_list)
    # uses what is returned from average_score and multiplies it
    # by the weight
    average_weight = average_score * weight
    return average_weight


grade_dict = {}

fh = open("Grades.txt", "r")


def read_grade_data(filehandle):
    for line in filehandle:
        strippedline = line.strip()
        splitline = strippedline.split(" ", 2)
        grade_dict[splitline[0]] = [splitline[1], splitline[2].split(",")]
    return grade_dict


def write_grade_report(filehandle, data)
    fh = open(filehandle, "w")

    for category in data:
        data_name = data[category]
        data_weight = float(data[category][0][0:2]) / 100
        data_scores = data[category][1]
        points_earned = []
        points_possible = []

        for i in range(len(data_scores)):
            data_scores[i] = data_scores[i].strip().split("/")
            points_earned.append(int(data_scores[i][0]))
            points_possible.append(int(data_scores[i][1]))
        averages = average(points_earned, points_possible)
        letters = letter_grade(averages)
        weighted_averages = average_weighted(points_earned, points_possible, data_weight)

        fh.write("<h1>" + category + " Statistics (" + str(data_weight*100) + ")</h1>\n")
        fh.write("<ul>\n")
        fh.write(" <li><b>Average: </b> %.03f" %(averages) + "</li>\n")
        fh.write(" <li><b>Letter Grade: </b>" + letters + "</li>\n")
        fh.write(" <li><b>Overall Grade Contribution: </b>%.03f" %(weighted_averages) + "</li>\n")
        fh.write("</ul>\n")


# this function allows for implementation of every other function defined
def main():
    grades_data = read_grade_data(fh)
    print(write_grade_report("Scores.txt", grade_dict))


main()
