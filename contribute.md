# Tasker Project: Git Version Control & Branching Guide

Welcome to the Tasker project! This guide is written for our team of junior developers who are just getting started with Git. It will explain how to work with branches, make commits, and merge your work in a clear and simple way.

## 1. Getting Started

### 1.1. Prerequisites

- **Git Installed:** Make sure Git is installed on your computer.
- **IDE/Editor:** We recommend using Visual Studio Code or any other editor that supports Git integration.

### 1.2. Clone the Repository

Open your terminal (or use the built-in terminal in your IDE) and run:

```bash
git clone https://github.com/heyibad/tasker.git
cd tasker
```

This command downloads the project and takes you into the project folder.

## 2. Our Branching Strategy

We use a simple feature branch workflow:

- **Main Branch:** This branch (called `main`) always contains production-ready code.
- **Feature Branches:** For each new feature or bug fix, create a branch with a clear name (e.g., `feature/add-login` or `bugfix/fix-input-validation`).

### 2.1. Creating a Feature Branch

Before starting work on a new feature, create a new branch from `main`:

```bash
git checkout -b feature/your-feature-name
```

*Tip: Use descriptive names so everyone knows what your branch is for.*

## 3. Making Changes and Committing

### 3.1. Editing Code

Work on your feature in your branch. When you’ve made changes, check which files have been updated:

```bash
git status
```

### 3.2. Adding Changes

Add the files you want to commit (or all files):

```bash
git add .
```

### 3.3. Commit Your Changes

Commit your changes with a clear message:

```bash
git commit -m "Add feature: describe what you did"
```

*Tip: Write short and clear commit messages that explain your changes.*

## 4. Pushing Your Branch

Once you’re ready to share your work, push your feature branch to the remote repository:

```bash
git push origin feature/your-feature-name
```

This makes your branch available on GitHub so others can review your work.

## 5. Creating a Pull Request (PR)

When your feature is complete:

1. **Open GitHub:** Go to our Tasker repository on GitHub.
2. **Create a Pull Request:** Click on "Compare & pull request" for your branch.
3. **Describe Your Changes:** Write a summary of what you’ve done and reference any issues (if applicable).
4. **Request a Review:** Ask a teammate to review your PR.

*Remember: Your PR will be merged into `main` after review and testing.*

## 6. Merging & Collaboration

- **Keep Your Branch Updated:** Regularly pull changes from `main` into your feature branch to minimize merge conflicts:
  ```bash
  git checkout main
  git pull
  git checkout feature/your-feature-name
  git merge main
  ```
- **Resolve Conflicts:** If there are any merge conflicts, work with your teammate to resolve them before pushing again.
- **Merge When Approved:** Once your PR is approved, it will be merged into `main` by a team member.

## 7. Extra Tips for Beginners

- **Ask Questions:** If you’re not sure about a Git command or how to handle a conflict, ask a teammate or refer to [Git documentation](https://git-scm.com/doc).
- **Practice Commands:** Try these commands in a test repository first to get comfortable.
- **Use Visual Tools:** Visual Studio Code, GitKraken, or GitHub Desktop can help you see branches and history visually.

## 8. Additional Resources

- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)
- [GitHub Learning Lab](https://lab.github.com/)
- [Visual Git Reference](https://ndpsoftware.com/git-cheatsheet.html)

---

By following this guide, our team can work more efficiently and professionally with Git. Let’s keep our code clean, work collaboratively, and improve together!

Happy coding!

---

*References:*
- Git best practices from [Atlassian](citeturn1search16) and [Stack Overflow](citeturn1search3).

