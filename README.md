Git & Git Hub Assessment
Solution: 
Question 1: Project Initialization & First Push
n.exe "e:/PythonLabs/Git & Git Hub Assessment/app.py"
Hello, World!
PS E:\PythonLabs\Git & Git Hub Assessment> git init                                                      
Reinitialized existing Git repository in E:/PythonLabs/Git & Git Hub Assessment/.git/

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        app.py

nothing added to commit but untracked files present (use "git add" to track)
git: 'add.' is not a git command. See 'git --help'.

The most similar command is
        add
On branch master


Changes to be committed:
        new file:   app.py
[master (root-commit) 059ea51] Initial commit: add greet function in app.py
 1 file changed, 6 insertions(+)
 create mode 100644 app.py
PS E:\PythonLabs\Git & Git Hub Assessment> git remote add origin https://github.com/Rahul7387/Git-Git-Hub-Assessment.git
PS E:\PythonLabs\Git & Git Hub Assessment> git remote -v
origin  https://github.com/Rahul7387/Git-Git-Hub-Assessment.git (fetch)
origin  https://github.com/Rahul7387/Git-Git-Hub-Assessment.git (push)
PS E:\PythonLabs\Git & Git Hub Assessment> git push -u origin main
error: failed to push some refs to 'https://github.com/Rahul7387/Git-Git-Hub-Assessment.git'
PS E:\PythonLabs\Git & Git Hub Assessment> git branch
* master
PS E:\PythonLabs\Git & Git Hub Assessment> git branch -m master main
PS E:\PythonLabs\Git & Git Hub Assessment> git push -u origin main
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 4 threads
Compressing objects: 100% (2/2), done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/Rahul7387/Git-Git-Hub-Assessment.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
PS E:\PythonLabs\Git & Git Hub Assessment> git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   app.py

no changes added to commit (use "git add" and/or "git commit -a")

Question 2: Working with Changes & History
PS E:\PythonLabs\Git & Git Hub Assessment> git diff
diff --git a/app.py b/app.py
index 54ab4c9..7d9ec37 100644
--- a/app.py
+++ b/app.py
@@ -1,6 +1,16 @@
+# app.py — updated with new features
+
 def greet(name):
     return f"Hello, {name}!"
 
+# --- New Feature 1: Calculator ---
+def add(a, b):
+    return a + b
+
+def subtract(a, b):
+    return a - b
+
:
--- a/app.py
+++ b/app.py
@@ -1,6 +1,16 @@
+# app.py — updated with new features
+
 def greet(name):
     return f"Hello, {name}!"
 
+# --- New Feature 1: Calculator ---
+def add(a, b):
+    return a + b
+
+def subtract(a, b):
+    return a - b
+
:
--- a/app.py
+++ b/app.py
@@ -1,6 +1,16 @@
+# app.py — updated with new features
+
 def greet(name):
     return f"Hello, {name}!"
 
+# --- New Feature 1: Calculator ---
+def add(a, b):
+    return a + b
+
+def subtract(a, b):
+    return a - b
+
:
+++ b/app.py
+# app.py — updated with new features
+
 
+# --- New Feature 1: Calculator ---
+def add(a, b):
+    return a + b
+
+def subtract(a, b):
+    return a - b
+
PS E:\PythonLabs\Git & Git Hub Assessment> git add app.py
to app.py"
[main f12fd31] feat: add calculator functions (add, subtract) to app.py
PS E:\PythonLabs\Git & Git Hub Assessment> git add .
PS E:\PythonLabs\Git & Git Hub Assessment> git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   app.py

PS E:\PythonLabs\Git & Git Hub Assessment> git commit -m "feat: add temperature converter (Celsius/Fahrenheit) to app.py"
[main f95f4b7] feat: add temperature converter (Celsius/Fahrenheit) to app.py
 1 file changed, 11 insertions(+), 3 deletions(-)
PS E:\PythonLabs\Git & Git Hub Assessment> git log
Author: Rahul7387 <rahulgupta7387@gmail.com>
Date:   Sat May 9 16:20:53 2026 +0530


commit f12fd31b879cf77cf12a3ad09a0fc90ada2a1bfb
Author: Rahul7387 <rahulgupta7387@gmail.com>
Date:   Sat May 9 16:20:13 2026 +0530

    feat: add calculator functions (add, subtract) to app.py

commit 059ea51c8cec01371754d5b74e45e976250376f3 (origin/main, origin/HEAD)
Author: Rahul7387 <rahulgupta7387@gmail.com>
Date:   Sat May 9 16:14:12 2026 +0530
PS E:\PythonLabs\Git & Git Hub Assessment> git log --oneline
f95f4b7 (HEAD -> main) feat: add temperature converter (Celsius/Fahrenheit) to app.py
f12fd31 feat: add calculator functions (add, subtract) to app.py
059ea51 (origin/main, origin/HEAD) Initial commit: add greet function in app.py
PS E:\PythonLabs\Git & Git Hub Assessment> git log --oneline --graph --all
* f95f4b7 (HEAD -> main) feat: add temperature converter (Celsius/Fahrenheit) to app.py
* f12fd31 feat: add calculator functions (add, subtract) to app.py
* 059ea51 (origin/main, origin/HEAD) Initial commit: add greet function in app.py
PS E:\PythonLabs\Git & Git Hub Assessment>

Question 3: Branching & Feature Development
PS E:\PythonLabs\Git & Git Hub Assessment> git branch feature-update
PS E:\PythonLabs\Git & Git Hub Assessment> git branch
  feature-update
* main
PS E:\PythonLabs\Git & Git Hub Assessment> git checkout feature-update
Switched to branch 'feature-update'
PS E:\PythonLabs\Git & Git Hub Assessment> git branch
* feature-update
  Main
PS E:\PythonLabs\Git & Git Hub Assessment> git add app.py
PS E:\PythonLabs\Git & Git Hub Assessment> git commit -m "feat: add string utilities (reverse, palindrome, word count)"
[feature-update f64a8e2] feat: add string utilities (reverse, palindrome, word count)
 1 file changed, 15 insertions(+), 6 deletions(-)
PS E:\PythonLabs\Git & Git Hub Assessment> git checkout main
Switched to branch 'main'
Your branch is ahead of 'origin/main' by 2 commits.
  (use "git push" to publish your local commits)
PS E:\PythonLabs\Git & Git Hub Assessment> git branch
  feature-update
PS E:\PythonLabs\Git & Git Hub Assessment> git merge feature-update
Updating f95f4b7..f64a8e2
Fast-forward
 app.py | 21 +++++++++++++++------
 1 file changed, 15 insertions(+), 6 deletions(-)
PS E:\PythonLabs\Git & Git Hub Assessment> git merge --no-ff feature-update -m "merge: integrate feature-update into main"
Already up to date.
PS E:\PythonLabs\Git & Git Hub Assessment> git log --oneline
f64a8e2 (HEAD -> main, feature-update) feat: add string utilities (reverse, palindrome, word count)
f95f4b7 feat: add temperature converter (Celsius/Fahrenheit) to app.py
f12fd31 feat: add calculator functions (add, subtract) to app.py
059ea51 (origin/main, origin/HEAD) Initial commit: add greet function in app.py
PS E:\PythonLabs\Git & Git Hub Assessment> type app.py
# app.py â€” updated on feature-update branch

def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# --- New Feature: String Utilities ---
    return s[::-1]
def is_palindrome(s):
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    print(greet("World"))
    print(f"Is 'racecar' a palindrome? {is_palindrome('racecar')}")
    print(f"Word count of 'Hello World': {word_count('Hello World')}")
PS E:\PythonLabs\Git & Git Hub Assessment> git branch -d feature-update
PS E:\PythonLabs\Git & Git Hub Assessment> git branch
* main
PS E:\PythonLabs\Git & Git Hub Assessment> git checkout -b dummy-branch
PS E:\PythonLabs\Git & Git Hub Assessment> echo "# temporary test" > temp.py
PS E:\PythonLabs\Git & Git Hub Assessment> git add temp.py
PS E:\PythonLabs\Git & Git Hub Assessment> git commit -m "temp: dummy commit for force-delete demo"
[dummy-branch 2f2bc9b] temp: dummy commit for force-delete demo
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 temp.py
PS E:\PythonLabs\Git & Git Hub Assessment> git checkout main
Switched to branch 'main'
Your branch is ahead of 'origin/main' by 3 commits.
  (use "git push" to publish your local commits)
PS E:\PythonLabs\Git & Git Hub Assessment> git branch -d dummy-branch
error: the branch 'dummy-branch' is not fully merged
hint: If you are sure you want to delete it, run 'git branch -D dummy-branch'
hint: Disable this message with "git config set advice.forceDeleteBranch false"
PS E:\PythonLabs\Git & Git Hub Assessment> git branch -D dummy-branch
Deleted branch dummy-branch (was 2f2bc9b).
PS E:\PythonLabs\Git & Git Hub Assessment>

Question 4: Handling Errors (Stash, Reset, Revert)

PS E:\PythonLabs\Git & Git Hub Assessment> echo "# notes for list utilities" > notes.txt
On branch main
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)

  (use "git add <file>..." to include in what will be committed)

PS E:\PythonLabs\Git & Git Hub Assessment> git stash push -u -m "WIP: list utilities feature"
PS E:\PythonLabs\Git & Git Hub Assessment> git status
On branch main
Your branch is ahead of 'origin/main' by 3 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
PS E:\PythonLabs\Git & Git Hub Assessment> git stash list
stash@{0}: On main: WIP: list utilities feature
PS E:\PythonLabs\Git & Git Hub Assessment> git stash list
stash@{0}: On main: WIP: list utilities feature
PS E:\PythonLabs\Git & Git Hub Assessment> git stash show stash@{0}
Too many revisions specified: 'stash@' 'MAA=' 'xml' 'text'
PS E:\PythonLabs\Git & Git Hub Assessment> git stash show -p stash@{0} 
Too many revisions specified: 'stash@' 'MAA=' 'xml' 'text'
PS E:\PythonLabs\Git & Git Hub Assessment> git stash pop
  (use "git push" to publish your local commits)

Changes not staged for commit:
        modified:   app.py

  (use "git add <file>..." to include in what will be committed)
        notes.txt

no changes added to commit (use "git add" and/or "git commit -a")
Dropped refs/stash@{0} (7601e1f10183c04c5d747a616ec967a89e5dd2a9)
PS E:\PythonLabs\Git & Git Hub Assessment> git add app.py notes.txt
 2 files changed, 11 insertions(+), 1 deletion(-)
 create mode 100644 notes.txt
PS E:\PythonLabs\Git & Git Hub Assessment> git add app.py
PS E:\PythonLabs\Git & Git Hub Assessment> git commit -m "feat: add divide function"
[main 8b8d5cb] feat: add divide function
8b8d5cb (HEAD -> main) feat: add divide function
2aa4fda feat: add list utilities (max, min, average)
f12fd31 feat: add calculator functions (add, subtract) to app.py
059ea51 (origin/main, origin/HEAD) Initial commit: add greet function in app.py
PS E:\PythonLabs\Git & Git Hub Assessment> git log --oneline
2aa4fda (HEAD -> main) feat: add list utilities (max, min, average)
f64a8e2 feat: add string utilities (reverse, palindrome, word count)
f95f4b7 feat: add temperature converter (Celsius/Fahrenheit) to app.py
f12fd31 feat: add calculator functions (add, subtract) to app.py
059ea51 (origin/main, origin/HEAD) Initial commit: add greet function in app.py
PS E:\PythonLabs\Git & Git Hub Assessment> git add app.py
[main 0c63894] feat: add divide function with zero-check
 1 file changed, 4 insertions(+)
PS E:\PythonLabs\Git & Git Hub Assessment> git add app.py
PS E:\PythonLabs\Git & Git Hub Assessment> git commit -m "feat: add square function"
[main 5ccb0d1] feat: add square function
 1 file changed, 2 insertions(+)
PS E:\PythonLabs\Git & Git Hub Assessment> git log --oneline
5ccb0d1 (HEAD -> main) feat: add square function
0c63894 feat: add divide function with zero-check
2aa4fda feat: add list utilities (max, min, average)
f95f4b7 feat: add temperature converter (Celsius/Fahrenheit) to app.py
f12fd31 feat: add calculator functions (add, subtract) to app.py
059ea51 (origin/main, origin/HEAD) Initial commit: add greet function in app.py
PS E:\PythonLabs\Git & Git Hub Assessment> git revert 0c63894       
CONFLICT (content): Merge conflict in app.py
error: could not revert 0c63894... feat: add divide function with zero-check
hint: After resolving the conflicts, mark them with
hint: "git add/rm <pathspec>", then run
hint: You can instead skip this commit with "git revert --skip".
hint: To abort and get back to the state before "git revert",
hint: run "git revert --abort".
hint: Disable this message with "git config set advice.mergeConflict false"
PS E:\PythonLabs\Git & Git Hub Assessment> git revert 0c63894 --no-edit
error: Reverting is not possible because you have unmerged files.
hint: Fix them up in the work tree, and then use 'git add/rm <file>'
hint: as appropriate to mark resolution and make a commit.
fatal: revert failed
PS E:\PythonLabs\Git & Git Hub Assessment> git revert 0c63894 --no-edit
error: Reverting is not possible because you have unmerged files.
hint: Fix them up in the work tree, and then use 'git add/rm <file>'
hint: as appropriate to mark resolution and make a commit.
fatal: revert failed
PS E:\PythonLabs\Git & Git Hub Assessment> git status
You are currently reverting commit 0c63894.
  (fix conflicts and run "git revert --continue")
  (use "git revert --skip" to skip this patch)

Unmerged paths:
        both modified:   app.py
no changes added to commit (use "git add" and/or "git commit -a")
PS E:\PythonLabs\Git & Git Hub Assessment> notepad app.py
PS E:\PythonLabs\Git & Git Hub Assessment> 
PS E:\PythonLabs\Git & Git Hub Assessment> git add app.py
PS E:\PythonLabs\Git & Git Hub Assessment> git revert 0c63894 --no-edit
 Date: Sat May 9 16:46:21 2026 +0530
 1 file changed, 4 deletions(-)
PS E:\PythonLabs\Git & Git Hub Assessment> git revert --abort       # If stuck mid-revert
error: no cherry-pick or revert in progress
fatal: revert failed
fatal: There is no merge to abort (MERGE_HEAD missing).
PS E:\PythonLabs\Git & Git Hub Assessment> git status
On branch main
Your branch is ahead of 'origin/main' by 8 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
PS E:\PythonLabs\Git & Git Hub Assessment> git revert 0c63894 --no-edit
On branch main
Your branch is ahead of 'origin/main' by 8 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
PS E:\PythonLabs\Git & Git Hub Assessment> # Graph view - great for visualizing reverts/branches
PS E:\PythonLabs\Git & Git Hub Assessment> git log --oneline --graph --all
* 887e818 (HEAD -> main) Revert "feat: add divide function with zero-check"
* f78cfe1 Revert "feat: add divide function with zero-check"
* 5ccb0d1 feat: add square function
* 0c63894 feat: add divide function with zero-check
* 2aa4fda feat: add list utilities (max, min, average)
* f64a8e2 feat: add string utilities (reverse, palindrome, word count)
* f95f4b7 feat: add temperature converter (Celsius/Fahrenheit) to app.py
* f12fd31 feat: add calculator functions (add, subtract) to app.py
* 059ea51 (origin/main, origin/HEAD) Initial commit: add greet function in app.py

