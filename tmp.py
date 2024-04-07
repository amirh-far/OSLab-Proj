import subprocess

command = "cd ~/Desktop/Dev ; ls"
result = subprocess.run(
    command,
    shell=True,
    text=True, 
    check=True,
    capture_output=True
)

print(result.stdout)

# command = "pwd"
# result = subprocess.run(
#     command,
#     shell=True,
#     text=True, 
#     check=True,
#     capture_output=True
# )

# print(result.stdout)