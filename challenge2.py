student_id = input("Enter student id: ")
email = input("Enter email: ")
password = input("Enter password: ")
referral = input("Enter referral: ")
valid = True
if not ( len(student_id) == 7 and
    student_id[0:4] == "CSE-" and
    student_id[4:7].isdigit()):
    valid = False
elif not ("@" in email and "." in email and not email.startswith("@") and not email.endswith("@") and
    email.endswith(".edu")):
    valid = False
elif not ( len(password) >= 8 and
    password[0].isupper() and
    not password.isalpha()):
    valid = False
elif not ( len(referral) ==6 and
    referral[0:3] == "REF" and
    referral[3:5].isdigit() and
    referral[5] == "@"):
    valid = False
if valid:
    print("Approved")
else:
    print("Rejected")