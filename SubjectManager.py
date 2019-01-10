#Add Student and write them to a file

# Check if there are any subjects in the file
# Ask the user if would like to add new subjects
# Yes >> Prompt for adding a new subject
# No >> Print the list of subjects that are saved so far.

# List of available subjects
subjects = []

# This function will get the list of the subjects saved to file.
def get_subjects():
    try:
        f = open('subject.txt', 'r')
        for subject in f.readlines():
            row = subject.split(" ")
            add_subject(row[0], row[1])
        f.close()
    except Exception:
        print('No contents available')

        
# This function will update the global variable
def add_subject(subject_id, subject_name):
    subject = {"name": subject_name, "id": subject_id}
    subjects.append(subject)

# Get the input from the user and the subject to the list of subjects
def new_subject():
    subject_name = input("Enter subject name: ")
    subject_id = input("Enter subject id: ")
    add_subject(subject_id, subject_name)

# Print all the subjects added so far
def print_all_subjects():
    print('\n')
    print('********************')
    print('The list of available subjects are \n')
    for subject in subjects:
        print(f"subject Id is {subject['id']} subject name is {subject['name']}  ")

#save the contents of subjects to file
def save_subjects():
    try:
        f = open('subject.txt', 'w')
        for subject in subjects:
            f.write(subject['id'] + " " + subject['name'] + "\n")
        f.close()
    except Exception:
        print('Error occured in saving the new list to disk')


print(" Program execution started")
get_subjects()

while True:
    # Prompt the user if he would like to add new subjects
    if input("Would you like to add a new subject? please answer yes or no - ") == "yes":
        new_subject()
    else:
        print_all_subjects()
        save_subjects()
        break

print("\n")
print(" Program execution completed ")

    
