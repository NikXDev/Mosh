from pathlib import Path

path = Path('emails')   # it forms a directory named emails
path.mkdir()    # it forms a directory
path.rmdir()    # it deletes the directory

print("...................")
print(path.glob("*.py"))    # using this statement pops generator object, we need for loop to iterates over the objects

print("...................")    # remove emails from path class to make this code work
for i in path.glob("*.py"):     # * represents all types of files
    print(i)
