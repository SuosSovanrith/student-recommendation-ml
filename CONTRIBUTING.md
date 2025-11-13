# For collaborator:

## 1. Clone the Repository in VS Code
```bash
git clone https://github.com/SuosSovanrith/student-recommendation-ml.git
cd student-recommendation-ml
```

## 2. Set Up Your Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate         
pip install -r requirements.txt
```
## 3. Create your feature branch (always branch from latest main)
```bash
# Switch to main branch
git checkout main

# Pull to update code to latest to match the main branch
git pull origin main

# Create a new branch to code your feature
git checkout -b <branch-name>
```

Example: git checkout -b feature/add-model-a-dev

## 4. Commit frequently with clear messages:
```bash
git add path/to/changed_file.py
git commit -m "feature: add stuff in model-a-developement notebook."
```
or use VS Code UI

## 5. Sync Branch Before Pushing
Before pushing or opening a pull request, make sure branch is up to date.

```bash
git fetch origin
git checkout main
git pull origin main
git checkout feature/add-model-a-dev
git merge main
# resolve conflicts if there are any, then:
git add <resolved files>
git commit    # finish merge commit if necessary
```

## 6. Push your branch to GitHub
```bash
git push -u origin feature/add-model-a-dev
```
or use VS Code UI

## 7. Open a Pull Request on GitHub
Go to the GitHub repo page.
Click “Compare & pull request” — GitHub often shows this automatically after pushing.
Fill out the PR title and description clearly.
Done.

