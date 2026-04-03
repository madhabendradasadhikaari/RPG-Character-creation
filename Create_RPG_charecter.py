full_dot = '●'
empty_dot = '○'

def create_character(character_name, STR, INT, CHA):
    if not character_name:
        return "The character should have a name"
    elif len(character_name) > 10:
        return "The character name is too long"
    elif " " in character_name:
        return "The character name should not contain spaces"
    if not isinstance(STR, int) or not isinstance(INT, int) or not isinstance(CHA, int):
        return "All stats should be integers"
    elif INT < 1 or STR < 1 or CHA < 1:
        return "All stats should be no less than 1"
    elif INT > 4 or STR > 4 or CHA > 4:
        return "All stats should be no more than 4"
    elif INT + STR + CHA != 7:
        return "The character should start with 7 points"
    return character_name + "\nSTR " +  full_dot * STR + empty_dot * (10 - STR) + "\nINT " + full_dot * INT + empty_dot * (10 - INT) + "\nCHA " + full_dot * CHA + empty_dot * (10 - CHA)

#character creation
while True:
  character_name = input("Enter the character name:").strip()

  if not character_name:
    print("Name can not be empty.")
    continue

  if len(character_name) > 10:
    print("The character name is too long (max 10 chars).")
    continue
  
  break

print(f"Success! The character name set to {character_name}")

#stats
print("Each stats should be from 1 to 4.")

total_point = 7
print(f"You have total {total_point} points.")

#STR
try:
    STR = int(input("Enter your character strength:"))
except:
    print("You should only write number")
  
print(f"You have {total_point - STR} left!")

#INT
try:
    INT = int(input("Enter your character intelligence:"))
except:
  print("You should only write number")

print(f"You have {total_point - INT} left!")

#CHA
try:
    CHA = int(input("Enter your character charisma:"))
except:
  print("You should only write number")

print(f"You have {total_point - CHA} left!")

#printing
print(create_character(character_name, STR, INT, CHA))
