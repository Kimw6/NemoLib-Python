# Git
Ryan Berge

Git is, by far, the most-used source control tool in computing. Its purpose is to help teams work on the same projects at the same time while maintaining histories and backups of all your code.  You begin by creating a git _repository_, which is a server where your main codebase lives.  Users then copy that repository to their local machine (after installing Git) by using Git Clone:

`git clone <URL-to-your-repo>.git`

The git repository has now been copied to your machine. Note that it is a _copy_, not a link to the source repository on the server. Any work that you do is always done on the local copy.

Git repositories are organized into _branches_. A branch is a diverging path of code changes. By default, everyone will start on the `master` branch. When you want to work on a new feature, you should checkout a new branch:

`git checkout -b ExampleBranch`

The `-b` argument specifies that this branch is to be created first, then checked out. You are now on `ExampleBranch`. If you want to check out a branch that already exists, the `-b` is omitted. The original state of a branch will be identical to the branch you were on when you created it _at the time you created it_. `ExampleBranch` will have everything `master` had at the time.

Now you can start work on your code. Remember that you are still working on a _copy_ of the git repository. No one else can see your changes, or even the branch you've created. That's fine.

As you're working, try looking at the status of your repo:

`git status`

Depending on what you've done so far, you may see zero, one, or two categories: Files labeled as _unstaged_ and files labeled as _untracked_. Untracked files will be files you have just created inside the git repository that have never been committed. Untracked files are not edited by Git as you change branches or mess with anything in any way.  Unstaged files are files that _are_ being tracked by Git and have been changed since they were last committed. Once you are happy with your changes, you must _stage_ and then _commit_ them for Git to remember your changes.

To stage a file, the command is:
`git add my_file.txt`
If you want to stage _all_ your files (including untracked files!) you can instead use:
`git add .`

If you type `git status` again, you will see that your files are now Staged. This means Git is prepared to commit these changes.  Let's do that:

`git commit`

Git will now prompt you to enter a commit message. The default editor for this message will depend on a few things, but it will probably open up in Vim. We'll go over how to change this default later. There are different philosophies for how much you should put in a commit message, but generally it should describe the changes you made. One stipulation that _I_ think you should have is to keep the first line of the commit message under 70 or 80 characters, because some ways of viewing the Git history shows each commit on a single line with only the first line of the commit message. At my internship, we also used the branch name in the commit message:
`ExampleBranch: Implement Feature X`

Once you save the commit message and close the editor, your changes will have been committed! To verify this, you can view your Git history:

`git log`
Or if you want to be fancy:
`git log --oneline --graph --decorate -25`

- `--oneline` causes each commit to show up on a single output line

- `--graph` causes the output to render a cute ASCII representation of the branch tree structure

- `--decorate` causes the output to display the "head" of each branch next to the relevant commit

- `-25` says we only want to display the last 25 commits

You now have your first commit. But again, you are still working your own local copy of your repository. The server doesn't know about your commit (and if you made it on a new branch, it doesn't even know about your branch). Assuming for the moment that developers and branches have a one-to-one relationship (only one developer will ever work on each branch), you can now _push_ your changes to the remote repository:

`git push origin ExampleBranch`

This will now update to remote branch to include your new changes (again, assuming no one else has also updated that branch in the meantime).

The remote repository now sees your changes! But _you_ still don't know anything about changes other developers may have made. You can use:

`git fetch`

to help you with this. `git fetch` will update your _remote references_ to the remote repository. This is not the same thing as updating your local repository. What it does is tell your local Git about changes that have happened in the remote repository. If some other developer has updated the `master` branch and you want to incorporate their changes, you have a couple options.

```
git checkout master
git pull
```

This option makes sense if your version of `master` has changes that haven't been pushed yet and you need to perform some kind of merge. Hopefully, however, this isn't the case because you've been working on `ExampleBranch` and not `master`! Note also that this option still works even if you haven't changed `master`. 

The other option is:

`git fetch origin master:master`

This does not work if you are currently checked in to `master`. What it does is _replace_ your version of `master` with the remote version of `master`. This option makes sense if you've done something weird and you just want to get your branch back into the state that the server knows about. It also makes sense if you want to update `master` and continue working on your own branch, because it means you don't need to check into `master`, do a pull, then check back into your own branch. _Note: I believe you can also use this to replace any branch with any other branch, but I've never tried using it that way._

So now you know how to use Git to create branches, stay synchronized with a remote Git repository, and make changes and commit them. You have finished working on a feature and you want it to be incorporated into the main development branch of the repository (often `master`).  You can do:

```
git checkout master
git merge ExampleBranch
```

... but you shouldn't. Different organizations have different philosophies about this, but most of them will not let you modify the primary development branch directly. Instead, they will ask that you go to the server website (usually Github or Bitbucket or something similar) and submit a _pull request_. You do this through the website. Your pull request will then go into a review process where other developers can look at your code and comment on it or request changes. Generally speaking, one or more developers will "approve" your code and then a software director or administrator will merge it.

Once it's merged, you will need to update your remote references again, because the `master` branch will have changed.

# Merge Conflicts
Imagine for the moment that Sam and Kathy both follow this process for two separate features. They each open a pull request when they have finished. Sam's code has a couple bugs that people catch during review, so he goes back to fix them. Kathy's code, however, gets approved without needing changes, and the system administrator merges her code in.

Sam has fixed his bug and updated his pull request. The other developers approve the changes, and the system administrator goes to merge.

Sam and Kathy were both working on different features, but they each needed to edit a configuration file. Now that Kathy's changes have been incorporated, Sam's version of the configuration file has merge conflicts! During the merge, Git will enter a transitory state and apply some strange-looking text into the file in question:

```
<<<<<<< destination:2bc831936fe89e017f182acb
HardwareID: 17, 15, 13
=======
HardwareID: 17, 15, 18
>>>>>>> source:1561ab54651c6b6a41e64f1a61c67
```

Each of them needed to an an ID. Kathy added `13` and Sam added `18`. In this trivial case, the solution should probably look like:
`HardwareID: 17, 15, 13, 18`

The person doing the merge will now go edit the file, delete the weird things Git has added, and combine things in the way that is needed. He or she will then complete the merge.

The problem with this workflow is that the person resolving the merge conflict is now the system administrator, rather than the engineer who wrote the code.  There are other workflows we can use instead.

# Rebasing

A rebase is a little weird in Git. When you _rebase_ a branch, you do it _onto_ another branch.  Say we want to rebase `ExampleBranch` onto `master`. We call:

```
git checkout ExampleBranch
git rebase master
```

If the current state of `master` matches the state of `master` saved in the history of `ExampleBranch`, this will have no effect. If, however, the state of `master` has changed since `ExampleBranch` was created (or last rebased), Git will now "replay" all the commits in `ExampleBranch` on top of the new state in `master`. If there are merge conflicts, it will pause in a transitory state and allow you to manually merge them as you go.

`git rebase --continue` (during a conflict)

`git rebase --abort` (if you're panicking and everything is awful forever)

Once the rebase has been completed, your local Git history will now show your commits as having been made on top of the new state of `master`, which means merging that branch into `master` will have no merge conflicts. Note that this is _not_ representative of the way those commits were actually developed! `git rebase` modifies the actual history of the branch. If that is undesirable to your team, this option should be avoided.

Now push your changes:

`git push origin ExampleBranch --force`

The `--force` option is required whenever you push changes that directly modify the history (`git commit --amend` needs this as well).

The advantages of using `git rebase` are that it leaves your repository with a history that is much easier to read and, more importantly, that it offloads the process of resolving merge conflicts onto the engineer actually working on the branch.

This is the workflow I was taught when I interned at Universal Avionics. It is not the only workflow and it is not necessarily the best workflow, but it _is_ the one with which I am most familiar.

# A Day in the Life of a Feature
```
git clone <Repo>.git
cd <Repo>
git checkout -b NewFeature
(do some work)
git add .
git commit
(check to see if there are updates)
git fetch
(if master has been updated: )
git fetch origin master:master
git rebase master
(fix conflicts, if there are any)
git push origin NewFeature --force
(Submit a pull request)
(or don't, if you aren't done)
. . .
```

# Advanced Features
### Configuring other tools
You can configure a default text editor that will open whenever Git needs you to edit text. I don't remember how and I always google it whenever I need to edit that. I suggest doing the same.

TODO: Add commands for changing text editor

You can also configure a Mergetool, which is a program that will open to assist you in resolving merge conflicts. I recommend you do this, but you're the master of your own destiny.

TODO: Recommend mergetool and add commands to configure it
