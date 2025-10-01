# Assignment 1 - Python Desktop Applications

This project contains 3 desktop applications built with Python and tkinter for CPSC 8740 class assignment:
1. Basic Calculator
2. To-Do List Application
3. Simple Tic-Tac-Toe Game

## Setup

### Environment Setup
```bash
# Create conda environment
conda create -n cpsc8740 python=3.11 -y

# Activate environment
conda activate cpsc8740

# Install dependencies (if any additional packages are needed)
# pip install -r requirements.txt
```

### Project Structure
```
assignment-1/
├── calculator/
│   └── calculator.py
├── todo/
│   └── todo_app.py
├── tic_tac_toe/
│   └── tic_tac_toe.py
└── CLAUDE.md
```

## Running the Applications

Make sure the conda environment is activated first:
```bash
conda activate cpsc8740
```

### Calculator
```bash
cd assignment-1/calculator
python calculator.py
```

### To-Do List
```bash
cd assignment-1/todo
python todo_app.py
```

### Tic-Tac-Toe
```bash
cd assignment-1/tic_tac_toe
python tic_tac_toe.py
```

## Development Workflow

### Code Quality (Optional)
```bash
# Format code
python -m black .

# Lint code
python -m flake8 .
```

### Git Workflow for Code Reviews
1. Create feature branches for each app or feature
2. Make commits with clear messages
3. Push to GitHub and create pull requests
4. Use coderabbit.ai for automated code reviews

### Creating Pull Requests
When ready to submit work:
```bash
# Add and commit changes
git add .
git commit -m "Add [feature/app name]"

# Push to remote branch
git push origin [branch-name]

# Create PR (Claude can help with this)
gh pr create --title "Add [app name]" --body "Implementation of [description]"
```

## Notes
- This is a prototype project focusing on quick development
- Using tkinter for simple desktop GUI applications
- No production build process needed
- All apps are standalone Python scripts