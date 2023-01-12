import os

# if(not os.path.exists("data")):
#     os.mkdir("data")

# for i in range(0, 6):
#     os.mkdir(f"data/Day{i+1}")

# Folder rename
# for i in range(0, 6):
#     os.rename(f"data/Tutorial{i+1}", f"data/Tutorial {i+1}")

folders = os.listdir("data")
print(folders)

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folders}"))