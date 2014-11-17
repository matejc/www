Contributing & git workflow
===========================

Please don't commit directly in the repo; instead submit pull requests
for others to comment on — rigorous code review process should make
everyone a better coder.

1. fork the repository,
2. `git clone git@github.com:<your-username>/www.git kiberpipa-www` to
   clone your fork,
3. `git checkout master` to switch to default, `master` branch,
3. `git pull --ff` to fetch any updates,
3. `git checkout --branch <feature_name>` to create a feature branch for
   your shiny new feature, deriving from `master` from step 3,
3. make feature changes in your feature branch,
3. `make test && make html` to ensure the site builds properly,
3. check for unnecessary whitespace with `git diff --check` before
   committing,
3. selectively commit¹ changes into reasonable commits
   (with `git add --patch` or as you prefer) with reasonable
   commit titles,
3. [squash] unreasonable commits for a tidier commit history,
3. push the changes to your fork and submit a pull request.

[squash]: https://www.google.com/search?q=github+squash

When you are ready to work on another feature, repeat steps from 3rd on.
In other words, don't put multiple unrelated fixes/features in the same
branch / pull request. If you're hacking on a new feature and find a
bugfix that doesn't require your new feature, make a new distinct branch
and pull request for the bugfix.

**¹** First line of your commit message should start with present-tense
verb, be 60 characters or less, and include the relevant issue number(s)
if applicable. Example: `Ensure proper PLUGIN_PATH behavior. Fixes #27`.


Reviewing others' code
----------------------

You can easily review other user's code by adding their repo as one of
the remotes: `git remote add <username> git@github.com:<username>/www.git`.

You can then checkout their changes with: `git checkout <username>/<feature_name>`.


Additional resources
--------------------

- [Using pull requests on GitHub][pull-requests]

[pull-requests]: https://help.github.com/articles/using-pull-requests/
