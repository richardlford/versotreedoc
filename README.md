# versotreedoc

Generate verso files to provide a framework for documenting a file tree.
There is a verso file for each file and directory in the file tree,
The verso files for a directory have a description of that
directory and links to contained files and subdirectories.
The verso files for individual files contain a description of the
file as well as vscode links to the file being described and
to the source verso file (for ease of finding it from the
processed html). 

Here is the help message for versotreedoc:

```
$ versotreedoc.py --help
usage: versotreedoc.py [-h] --root-dir ROOT_DIR --output-dir OUTPUT_DIR 
    [--port [PORT]] [--abbrev-level ABBREV_LEVEL]
    [--lean-toolchain LEAN_TOOLCHAIN]
    [--authors [AUTHORS ...]] [--path-excludes [PATH_EXCLUDES ...]] 
    [--dir-excludes [DIR_EXCLUDES ...]] [--prefix PREFIX] [--vscode-links]
    [--include-dot-files] [--update] [--overwrite] [--use-git]

Produce verso documentation skeleton for a directory tree.

options:
  -h, --help            show this help message and exit
  --root-dir ROOT_DIR   Path to directory for which to produce documentation.
  --output-dir OUTPUT_DIR
                        Output directory where the output will be stored.
  --port [PORT]         bind to this port (default: 8000)
  --abbrev-level ABBREV_LEVEL
                        Number of path components to include in the abbreviated path (default: 3).
  --lean-toolchain LEAN_TOOLCHAIN
                        Lean toolchain to use.
  --authors [AUTHORS ...]
                        Authors to list in the verso documentation.
  --path-excludes [PATH_EXCLUDES ...]
                        Directory paths to exclude from the documentation (default tests).
  --dir-excludes [DIR_EXCLUDES ...]
                        Simple directory names to exclude from the documentation (default ["tests", "build"]). Also, all directories starting with "." are automatically
                        excluded.
  --prefix PREFIX       Prefix to add to files to avoid collisions (default Vtd_).
  --vscode-links        Include source links in the generated documentation.
  --include-dot-files   Include dot files in the generated documentation.
  --update              Update existing documentation rather than making new documentation.
  --overwrite           Give permission to overwrite existing files.
  --use-git             Use git to remove files instead of direct filesystem deletion.
```

The Examples/versodoc directory contains an example of the output of versotreedoc. The example was generated with the
following command, where we assume $verso is the path to a clone of the verso tool, and the current
working directory is the root of the versotreedoc repository. 
```
versotreedoc.py --root-dir $verso/src --output-dir Examples/versodoc --vscode-links
```

When the sources being documented change by deleting files or directories, or adding them
a documentation update can be performed with the --update option. The update will remove 
documentation for deleted files and directories, and add documentation skeletons for new files and directories. 
The update will not change existing documentation for files and directories that have not changed,
but it will update the links in the verso files for directories to reflect any changes 
in the contained files and subdirectories. When using the --update option, if you have
your document under version control, it is recommended to use the --use-git option to remove 
files that have been deleted from the source tree. This will ensure that the deletions 
are tracked in your version control system.
