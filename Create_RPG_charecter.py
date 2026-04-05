GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BLUE = '\033[94m'
CYAN = '\033[96m'
BOLD = '\033[1m'
RESET = '\033[0m'
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
    return  BOLD + YELLOW + character_name + RESET + "\nSTR " +  full_dot * STR + empty_dot * (10 - STR) + "\nINT " + full_dot * INT + empty_dot * (10 - INT) + "\nCHA " + full_dot * CHA + empty_dot * (10 - CHA)

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

print(f"---{GREEN}{BOLD}Success!{RESET} The character name set to {YELLOW}{BOLD}{character_name}{RESET}---")

#stats
print(f"{RED}*Each stats should be from 1 to 4.{RESET}")

total_point = 7
print(f"{CYAN}*You have total {total_point} points.{RESET}")
STR = INT = CHA = 0

#STR
while True:
  try:
    STR = int(input(f"{BLUE}Enter Strength (1-4):{RESET}"))
    if (1 <= STR) and (STR>= 4):
      print(f"{BOLD}Strength must be between 1 and 4!{RESET}")
      continue
    else:
      total_point -= STR
      print(f"{CYAN}You have total {total_point} points left.{RESET}")
      break
  except ValueError:
    print(f"{RED}It must be an number!{RESET}")
    continue
  
#INT
while True:
  try:
    INT = int(input(f"{BLUE}Enter Intelligent (1-4):{RESET}"))
    if 1 <= INT >= 4:
      print(f"{BOLD}Intelligence must be between 1 and 4!{RESET}")
      continue
    else:
      total_point -= INT
      print(f"{CYAN}You have total {total_point} points left{RESET}")
      break
  except ValueError:
    print(f"{RED}It must be an number!{RESET}")
    continue

#CHA
CHA = total_point
print(f"{BLUE}Charisma is automatically set to {total_point} according to your remaing points.{RESET}")
#printing
print(create_character(character_name, STR, INT, CHA))
