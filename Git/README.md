Learn Git
=========

Create and explore a simple Git-managed project

![xkcd: Git](https://imgs.xkcd.com/comics/git.png)

Table of Contents
-----------------

UNIT 1: BASIC GIT WORKFLOW
--------------------------

### Lesson: Basic Git Workflow

An introduction to Git and a few of its core features

#### Exercises

1. Hello Git
2. git init
3. Git Workflow
4. git status
5. git add
6. git diff
7. git commit
8. git log
9. Generalizations

    You have now been introduced to the fundamental Git workflow. You learned a lot! Let's take a moment to generalize:

    - Git is the industry-standard version control system for web developers
    - Use Git commands to help keep track of changes made to a project:
        - `git init` creates a new Git repository
        - `git status` inspects the contents of the working directory and staging area
        - `git add` adds files from the working directory to the staging area
        - `git diff` shows the difference between the working directory and the staging area
        - `git commit` permanently stores file changes from the staging area in the repository
        - `git log` shows a list of all previous commits

#### Codecademy Pro features

- Quiz: Git Workflow Quiz
- Project: Manhattan Zoo
    - Use Git to keep track of changes made to an Manhattan Zoo document.
- Project: SnapFit Robots, Inc.
    - Use Git to help draft customer documents for SnapFit Robots, Inc.

UNIT 2: HOW TO BACKTRACK IN GIT
-------------------------------

### Lesson: How to Backtrack

Learn different ways to undo changes made to a Git project and when to use them.

#### Exercises

1. Backtracking Intro
2. head commit
3. git checkout
4. more git add
5. git reset I
6. git reset II
7. git reset review
8. Generalizations

    Congratulations! You've learned three different ways to backtrack in Git. You can use these skills to undo changes made to your Git project.

    Let's take a moment to review the new commands:

    - `git checkout HEAD filename`: Discards changes in the working directory.
    - `git reset HEAD filename`: Unstages file changes in the staging area.
    - `git reset SHA`: Can be used to reset to a previous commit in your commit history.

    Additionally, you learned a way to add multiple files to the staging area with a single command:

```sh
git add filename_1 filename_2
```

#### Codecademy Pro features

- Quiz: GIt Backtracking Quiz
- Project: Poem Fiasco
    - Use Git backtracking commands to undo mistakes made to poems.
- Project: ASCII Portfolio
    - Use Git backtracking commands to help perfect some ASCII art pieces.


UNIT 3: GIT BRANCHING
---------------------

### Lesson: Git Branching

Learn How to Manage Multiple Versions of a Project with Branching

#### Exercises

1. git branch
2. branching overview
3. git branch 2
4. git checkout
5. commit on a new branch
6. git merge
7. merge conflict I
8. merge conflict II
9. delete branch
10. Generalizations

    Let's take a moment to review the main concepts and commands from the lesson before moving on.

    - Git *branching* allows users to experiment with different versions of a project by checking out separate *branches* to work on.

    The following commands are useful in the Git branch workflow.

    - `git branch`: Lists all a Git project's branches.
    - `git branch branch_name`: Creates a new branch.
    - `git checkout branch_name`: Used to switch from one branch to another.
    - `git merge branch_name`: Used to join file changes from one branch to another.
    - `git branch -d branch_name`: Deletes the branch specified.

#### Codecademy Pro features

- Quiz: Git Branching Quiz
- Project: Birthday Party
    - Use Git to help your friend make different versions of a web invitation.
- Project: Ruby Time Calculator
    - Use Git to fix a merge in the "Ruby Time Calc" Git project.

UNIT 4: GIT TEAMWORK
--------------------

### Lesson: Git Teamwork

An introduction to Git collaborations with remotes, pulling and pushing

#### Exercises

1. Overview
2. git clone
3. git remote -v
4. git fetch
5. git merge
6. Git Workflow
7. git push
8. Generalizations

    Congratulations, you now know enough to start collaborating on Git projects! Let's review.

    - A *remote* is a Git repository that lives *outside* your Git project folder. Remotes can live on the web, on a shared network or even in a separate folder on your local computer.
    - The *Git Collaborative Workflow* are steps that enable smooth project development when multiple collaborators are working on the same Git project.
    We also learned the following commands

    - `git clone`: Creates a local copy of a remote.
    - `git remote -v`: Lists a Git project's remotes.
    - `git fetch`: Fetches work from the remote into the local copy.
    - `git merge origin/master`: Merges origin/master into your local branch.
    - `git push origin <branch_name>`: Pushes a local branch to the origin remote.

    Git projects are usually managed on Github, a website that hosts Git projects for millions of users. With Github you can access your projects from anywhere in the world by using the basic workflow you learned here.

#### Codecademy Pro features

- Quiz: Git Teamwork Quiz
- Project: JavaScript Homework
    - Use Git collaboration skills to make comments on a programming student's JavaScript homework.
- Project: Recipe Book
    - Play the role of two collaborators using Git to work on a book of recipes

