# AOC Summer 25 - Branch Merging Guide

Use this to find the Questions :

https://adventofcode.com/2021/day/1

follow instructions and sign up

## Add your Code

# add commit and push your code
git add .         
git commit -m "read"    
git push origin your-branch-name



## How to Merge Your Branch with Main

### Method 1: Local Merge (Quick)

# Switch to main branch
git checkout main

# Pull latest changes from remote main
git pull origin main

# Merge your branch into main (replace 'your-branch-name' with actual branch name)
git merge your-branch-name

# Push the merged changes
git push origin main


