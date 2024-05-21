# helios-procedures
LaTeX source for HELIOS related procedures

To get the procedures, go to the [release page on right side](https://github.com/aris-space/helios-procedures/releases) and download it from the release assets.

## Usage

### Doing changes

Commit messages should follow [conventional commit message structure](https://www.conventionalcommits.org/)

TODO: examples

Changes should be small and atomic.
Basically make many small PRs rather than one big one.

⚠️ Note that the `main` branch is protected, all changes have to be made to new branches and then merged via a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) ⚠️
⚠️ You will **NOT** be able to push to `main` ⚠️

Whenenever there are unreleased changes on main, `tagpr` will create a new release pull request.
Merging that PR will automatically create a new release.

If you want to remove an entry in a procedure, make sure to comment it out in the source rather than deleting the line.
This makes it easier to see who "removed" an entry when using [`git blame`](https://git-scm.com/docs/git-blame).
This is important as procedures often get entries removed that are assumed trivial or unnecessary.
As each team member has their own definition of what is "unnecessary", it is important to be able to easily see who removed an entry.

This only applies to procedure contents.
LaTeX commands etc can be deleted just fine if they are no longer needed.

### Structure

All LaTeX source is located in `src/` and from there separated by subteam (`dacs-sw`, ...).
The `src/common/` folder contains shared content like assets.

### Other

By default, documents will have a draft watermark controlled by a single LaTeX variable unless they are compiled by the release pipeline.
