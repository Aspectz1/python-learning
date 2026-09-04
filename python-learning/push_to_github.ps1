# Run this from the repository root after installing Git and authenticating with GitHub CLI.

git init
git add .
git commit -m "Add Python learning projects"

# Create the GitHub repository and push it.
gh repo create python-learning --public --source=. --push
