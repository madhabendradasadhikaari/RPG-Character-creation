# RPG-Character-creation
A simple Python program to create and validate a game character with stat constraints.
## Rules of the Programme
- Each stat must be between 1 and 4
- Total stat points must equal 7
- Character name must not contain spaces
- Maximum name length is 10 characters
## How to run
1. **Install Python**: Ensure you must have [python3.x](https://www.python.org/downloads/) installed.
2. **Download the file**: Save the code as `character_creator.py`
3. Run the program:
```python
python character_creator.py
```
## Example Output
```Enter the character name: Hero
Enter your character strength: 3
Enter your character intelligence: 2
Enter your character charisma: 2

Hero
STR ●●●○○○○○○○
INT ●●○○○○○○○○
CHA ●●○○○○○○○○`
```
## Future Improvements
1. Add input error handling
2. Allow multiple character creation
3. Add more attributes (HP, Level)
4. Create a GUI version
