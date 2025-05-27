"""
This script will implement our knowledge on conditions and different datatypes.
"""

print("This IT Organization has various skill sets.")
print("Find out your match.")

print("Enter Capitalised Values: ")

DevOps = ["Jenkins", "Ansible", "Bash", "Python", "Puppet", "Dockers", "Kubernetes", "Terraform"]
Development = ("Nodejs", "Angularjs", "Java", ".net", "Python")
cntr_emp1 = {"Name":"Salander", "Skill":"Blockchain", "Code":1824}
cntr_emp2 = {"Name":"Blomkvist", "Skill":"IA", "Code":1218}

usr_skill = input("Enter your desired skill: ")
#print(usr_skill)

#Check in the database if we have this skill
if usr_skill in DevOps:
    print(f"We Have {usr_skill} in DevOps Team.")
elif (usr_skill in Development):
    print(f"We Have {usr_skill} in Development Team.")
elif (usr_skill in cntr_emp1.values()) or (usr_skill in cntr_emp2.values()):
    print(f"We Have contract employees with {usr_skill} skill.")
else:
    print("Skill not found")
    print("Please check if you have a value in capitalize or check the spelling.")