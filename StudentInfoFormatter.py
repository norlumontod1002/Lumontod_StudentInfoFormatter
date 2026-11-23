# Version 1

print("\nSTUDENT INFORMATION FORMATTER")

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
favorite_subject = input("Enter favorite subject: ")

full_name = first_name + " " + last_name

print("\nStudent Information")
print("Name:", full_name)
print("Section:", section)
print("Favorite Subject:", favorite_subject)

# Version 2

first_name = input("\nEnter first name: ").strip()
last_name = input("Enter last name: ").strip()
section = input("Enter section: ").strip()
favorite_subject = input("Enter favorite subject: ").strip()

full_name = first_name + " " + last_name

proper_name = full_name.title()
uppercase_name = full_name.upper()
formatted_section = section.upper()
proper_subject = favorite_subject.title()

print("\nFormatted Output")
print("Name:", proper_name)
print("Name Code:", uppercase_name)
print("Section:", formatted_section)
print("Favorite Subject:", proper_subject)
print("Character Count:", len(full_name))
