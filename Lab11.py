import matplotlib.pyplot as plt
import os

def main():
    print("""1. Student grade
2. Assignment statistics
3. Assignment graph 
""")
    menu_choice = input("Enter your selection: ")

    content = file_handling()
    student_id, grade_point, assignment_details = get_details()

    if menu_choice == "1":
        student_name = input("What is the student's name: ")
        calculate_student_grade(content, student_name, student_id, grade_point)
    elif menu_choice == "2":
        assignment_name = input("What is the assignment name: ")
        if assignment_name in assignment_details:
            scores = get_assignment_scores(content, assignment_name, assignment_details)
            maximum = max(scores)
            minimum = min(scores)
            average = round(sum(scores) / len(scores))
            print(f"Min: {minimum}%\nMax: {maximum}%\nAverage: {average}%")
        else:
            print("Assignment not found.")
    elif menu_choice == "3":
        assignment_name = input("What is the assignment name: ")
        if assignment_name in assignment_details:
            scores = get_assignment_scores(content, assignment_name, assignment_details)
            plt.hist(scores, bins=10)
            plt.xlabel('Scores')
            plt.ylabel('Number of Students')
            plt.title(f"{assignment_name} Scores")
            plt.show()
        else:
            print("Assignment not found.")
    else:
        exit()

def get_assignment_scores(content, assignment_name, assignment_details):
    scores = []
    for line in content:
        id_num, assignment_code, score = line.strip().split("|")
        if assignment_details[assignment_name] == assignment_code:
            scores.append(int(score))
    return scores

def file_handling():
    # print(os.listdir("data/submissions"))  # returns a list will all the file names under submissions.
    content = []
    for file in os.listdir("data/submissions"):
        my_file = open(f"data/submissions/{file}", "r")
        content.append(my_file.read())
        my_file.close()

    return content

def get_details():
    student_id = {}   # holds name with id
    grade_point = {}   # holds the assignment code with grade_point
    assignment_details = {}   # holds assignment name with code

    # Assigns an ID to each name
    file = open("data/students.txt", "r")
    c = file.read().splitlines()
    for line in c:
        student_id[line[3:]] = line[:3]

    # Assigns point score to each assignment code
    other_file = open("data/assignments.txt")
    cont = other_file.read().splitlines()

    count_for_name = 0
    count_for_code = 1
    while count_for_code <= len(cont):
        assignment_details[cont[count_for_name]] = cont[count_for_name + 1]
        grade_point[cont[count_for_code]] = cont[count_for_code + 1]
        count_for_code += 3
        count_for_name += 2

    return student_id, grade_point, assignment_details

def calculate_student_grade(content, student_name, student_id, grade_point):
    # calculates the students grade
    total = 0
    if student_name in student_id:
        for assignment in content:
            id_num, assignment_code, score = assignment.strip().split("|")
            if id_num == student_id[student_name]:
                total += (int(score) * int(grade_point[assignment_code])) / 100
        grade_average = (total / 1000) * 100
        print(f"{round(grade_average)}%")
    else:
        print("Student not found.")



if __name__ == "__main__":
    main()

