# versotreedoc

Generate verso files to provide a framework for documenting a file tree.
There is a verso file for each directory in the file tree, and each verso file contains a list of the files and 
subdirectories in that directory. 

Here is the help message for versotreedoc:

```
$ versotreedoc.py --help
usage: versotreedoc.py [-h] --root-dir ROOT_DIR --output-dir OUTPUT_DIR [--port [PORT]] 
                       [--lean-toolchain LEAN_TOOLCHAIN]
                       [--authors AUTHORS] [--excludes EXCLUDES] [--prefix PREFIX]

Produce verso documentation skeleton for a directory tree.

options:
  -h, --help            show this help message and exit
  --root-dir ROOT_DIR   Path to directory for which to produce documentation.
  --output-dir OUTPUT_DIR
                        Output directory where the output will be stored.
  --port [PORT]         bind to this port (default: 8000)
  --lean-toolchain LEAN_TOOLCHAIN
                        Lean toolchain to use.
  --authors AUTHORS     Authors to list in the verso documentation.
  --excludes EXCLUDES   Directories to exclude from the documentation (default tests).
  --prefix PREFIX       Prefix to add to files to avoid collisions (default Vtd_).
```

The Examples/versodoc directory contains an example of the output of versotreedoc. The example was generated with the
following command, where we assume $verso is the path to a clone of the verso tool, and the current
working directory is the root of the versotreedoc repository. 
```
versotreedoc.py --root-dir $verso/src --output-dir Examples/versodoc 
```
