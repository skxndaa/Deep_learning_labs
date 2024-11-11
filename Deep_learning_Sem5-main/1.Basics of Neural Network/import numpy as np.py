# Step 1: Ask for student number
student_number = input("Enter student number: ")

# Step 2: Ask for tutorial mark
tutorial_mark = float(input("Enter tutorial mark: "))

# Step 3: Ask for test mark
test_mark = float(input("Enter test mark: "))

# Step 4: Calculate whether the student can write the examination
average_mark = (tutorial_mark + test_mark) / 2
if average_mark < 40:
    print("Average is below 40%. Student gets an F grade.")
else:
    # Step 5: Ask for end term examination mark
    exam_mark = float(input("Enter end term examination mark: "))

    # Step 6: Calculate final mark
    final_mark = 0.25 * tutorial_mark + 0.25 * test_mark + 0.5 * exam_mark

    # Step 7: Determine and print the final grade
    if 80 <= final_mark <= 100:
        print(f"Final Grade for student {student_number}: A")
    elif 70 <= final_mark < 80:
        print(f"Final Grade for student {student_number}: B")
    elif 60 <= final_mark < 70:
        print(f"Final Grade for student {student_number}: C")
    elif 50 <= final_mark < 60:
        print(f"Final Grade for student {student_number}: D")
    else:
        print(f"Final Grade for student {student_number}: E")
