# TaskMate - Student Task Management System
TaskMate is a small Python command-line application in which students can add tasks , view tasks , complete tasks and delete tasks.

## Features

- Add Task
- View Tasks
- Mark Task as Complete
- Delete Task

## How to Run

1. Clone Repo:
   git clone <repo-link>
2. Go into folder:
   cd <repo-name>
3. Rum Program:
   python main.py

## Team

1.Faryal Fatima :  Team Lead + Developer   | Repo setup, Add Task, View Tasks, PR merge |

2.Laiba Razzaq  :  Developer + Documentation Lead    | Mark Complete feature, README

3.Riffat Shaheen : Developer + QA/Reviewer    | Delete Task feature, Definition of Done, testing |

## Workflow We Followed

1. Team Lead ne repo banayi aur starter code push kiya
2. 3 GitHub Issues banaye aur members ko assign kiye
3. Har member ne apni feature branch banayi
4. Code likh kar Pull Request submit ki
5. Teammate ne peer review kiya aur comments diye
6. Author ne review comments resolve kiye
7. Approved code `main` branch me merge kiya gaya


## Definition of Done

A task or feature is considered **done** only when all of the following criteria are met:

### Code Quality
- The feature is fully implemented as described in its GitHub Issue.
- The code runs without errors or crashes.
- The code follows a clear structure with meaningful function and variable names.
- Each function includes a docstring or comment explaining its purpose.

### Testing
- The feature has been manually tested by the team leam.
- The feature works correctly with the rest of the application (`main.py`).
- Invalid input (e.g., a non-existent task ID) is handled without crashing.

### Version Control
- Work was done on a separate feature branch, not directly on `main`.
- Commits have clear, descriptive messages.
- A Pull Request was created and linked to the related issue (e.g., "Closes #2").

### Code Review
- At least one teammate has reviewed the Pull Request.
- All review comments have been addressed and resolved.
- The reviewer has approved the Pull Request.

### Merge and Closure
- The approved Pull Request is merged into `main` by the Team Lead.
- The related GitHub Issue is closed.
- The README is updated if the feature affects usage.