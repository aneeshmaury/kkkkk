import os
import subprocess

# Step 1: Create a folder named 'test'
folder_name = 'test'
os.makedirs(folder_name, exist_ok=True)
print(f"Folder '{folder_name}' created or already exists.")

# Step 2: Initialize git (if not already a git repo) and add the folder to the git index
subprocess.run(['git', 'init'], check=True)
subprocess.run(['git', 'add', folder_name], check=True)
print(f"Folder '{folder_name}' added to git index.")

# Step 3: Commit the changes
commit_message = 'Add test folder'
subprocess.run(['git', 'commit', '-m', commit_message], check=True)
print("Changes committed.")

# Step 4: Push the changes to GitHub
# You may need to replace 'origin' and 'main' with your remote name and branch name
remote_name = 'origin'
branch_name = 'main'
subprocess.run(['git', 'push', remote_name, branch_name], check=True)
print("Changes pushed to GitHub.")
