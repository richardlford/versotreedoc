#!/usr/bin/env python3

"""
Produce the verso documentation skeleton for a directory tree.

Richard L Ford, April 6, 2026
"""

import os
import sys
import argparse
from pathlib import Path

def read_file(path):
    """
    Read the contents of a file at the specified path.

    :param path: The file path to read from.
    :return: The string contents of the file.
    """
    with open(path, 'r') as f:
        return f.read()

def sanitize_tag(tag: str) -> str:
    """Change an non-alphanumeric character to a hyphen."""
    sanitized = ""
    for c in tag:
        if c.isalnum():
            sanitized = sanitized + c
        else:
            sanitized = sanitized + "-"
    return sanitized

def is_included(output_dir: str, root: str) -> (bool, Path):
    """
    Check if the given root directory is included in the given output_dir directory.
    :param output_dir: The directory that will contain the verso documentation.
    :param root: The root of the artifact tree for which to produce documentation.
    :return: True if root is included in the artifact tree.
    """
    output_path = Path(output_dir).resolve()
    root_path = Path(root).resolve()
    try:
        rel = root_path.relative_to(output_path, walk_up=False)
        return True, rel
    except ValueError:
        return False, Path()

class VersoTreeDoc(object):
    def __init__(self, args):
        path = args.root_dir
        self.path = path
        self.path_path = Path(path)
        self.path_parts = list(self.path_path.parts)
        self.parent: str = os.path.dirname(self.path)
        self.parent_path = Path(self.parent)
        self.parent_path_parts = list(self.parent_path.parts)
        self.output_dir = args.output_dir
        self.output_path = Path(args.output_dir)
        self.output_parts = list(self.output_path.parts)
        self.port = args.port
        self.abbrev_level = args.abbrev_level
        self.lib_name = os.path.basename(path)
        self.lean_toolchain = args.lean_toolchain
        authors = "["
        for author in args.authors:
            if len(authors) > 1:
                authors = authors + ", "
            authors = authors + f'"{author}"'
        authors = authors + "]"
        self.authors = authors
        os.makedirs(self.output_dir, exist_ok=True)
        self.prefix = args.prefix
        self.vscode_links = args.vscode_links
        self.include_dot_files = args.include_dot_files
        path_excludes = set()
        for exclude in args.path_excludes:
            path_excludes.add(exclude)
        self.path_excludes = path_excludes
        dir_excludes = set()
        for exclude in args.dir_excludes:
            dir_excludes.add(exclude)
        self.dir_excludes = dir_excludes
        self.is_included, self.relpath = is_included(self.output_dir, self.path)
        self.update = args.update
        self.overwrite = args.overwrite
        pass

    def write_file(self, path, contents):
        """
        Write the given contents to a file at the specified path.

        :param path: The file path where the contents will be written.
        :param contents: The string contents to write to the file.
        """

        if not self.overwrite and not self.update and os.path.exists(path):
            print(f"Error: file already exists: {path}", file=sys.stderr)
            sys.exit(1)
        with open(path, 'w') as f:
            f.write(contents)
        pass

    def make_file_description(self, root, file):
        """
        Make a description for a file in the given directory.

        :param root: Path to the directory containing the file.
        :param file: The name of the file.
        :return: A string description of the file.
        """
        root_path = Path(root)
        parts = list(root_path.parts)
        file_parts = parts.copy()
        file_parts.append(file)
        file_path = Path(*file_parts)
        relative_parts = parts[len(self.parent_path_parts):]
        relative_parts.append(file)
        prefixed_relative_parts = [f"{self.prefix}{part}" for part in relative_parts]
        hyphen_text = sanitize_tag("-".join(relative_parts))
        abbrev_relative_parts = relative_parts.copy()
        if len(abbrev_relative_parts) > self.abbrev_level:
            for i in range(len(abbrev_relative_parts) - self.abbrev_level):
                abbrev_relative_parts[i] = abbrev_relative_parts[i][0]
        abbrev_relative_text = Path(*abbrev_relative_parts).as_posix()
        lean_parts = self.output_parts + prefixed_relative_parts
        lean_parts[-1] = lean_parts[-1] + ".lean"
        lean_path = Path(*lean_parts)
        lean_posix = lean_path.as_posix()
        lean_prefixed_relative_parts = prefixed_relative_parts.copy()
        lean_prefixed_relative_parts[-1] = lean_prefixed_relative_parts[-1] + ".lean"
        lean_prefixed_posix = Path(*lean_prefixed_relative_parts).as_posix()
        contents = f"""-- {lean_prefixed_posix}
"""
        contents = contents + f"""

import VersoManual
import VersoExts
open Verso.Genre Manual
open Verso.Genre.Manual.InlineLean

#doc (Manual) "`{abbrev_relative_text}`"  =>

%%%
authors := {self.authors}
tag := "{hyphen_text}"
%%%

"""
        if self.vscode_links:
            if self.is_included:
                source_relative_path = file_path.relative_to(self.output_path)
                contents = contents + f"""\n{{editlink "{source_relative_path}"}}[source]\n"""
            else:
                source_relative_path = file_path.relative_to(self.path_path)
                contents = contents + f"""\n{{srclink "{source_relative_path}"}}[source]\n"""
            lean_relative_path = lean_path.relative_to(self.output_path)
            contents = contents + f"""\n{{editlink "{lean_relative_path}"}}[edit]\n"""

        contents = contents + f"""
TODO

"""

        lean_path.write_text(contents)
        return

    def make_verso(self, root, dirs, files):
        """
        Make a verso skeleton for the given directory, its subdirectories, and files.
        The skeleton is written to a file named dir.lean.

        :param root: Path to the root directory of the tree.
        :param dirs: The list of contained directories.
        :param files: The list of contained files.
        :return:
        """
        this_dir = os.path.basename(root)
        if this_dir[0] == '.':
            return

        root_path = Path(root)
        parts = list(root_path.parts)
        relative_parts = parts[len(self.parent_path_parts):]
        prefixed_relative_parts = [f"{self.prefix}{part}" for part in relative_parts]
        quoted_prefixed_relative_parts = [f"«{self.prefix}{part}»" for part in relative_parts]
        hyphen_text = sanitize_tag("-".join(relative_parts))
        abbrev_relative_parts = relative_parts.copy()
        if len(abbrev_relative_parts) > self.abbrev_level:
            for i in range(len(abbrev_relative_parts) - self.abbrev_level):
                abbrev_relative_parts[i] = abbrev_relative_parts[i][0]
        abbrev_relative_text = Path(*abbrev_relative_parts).as_posix()
        this_parts = self.output_parts + prefixed_relative_parts
        prefixed_path = Path(*this_parts)
        prefixed_path.mkdir(parents=True, exist_ok=True)
        lean_parts = this_parts.copy()
        lean_parts[-1] = lean_parts[-1] + ".lean"
        lean_path = Path(*lean_parts)
        lean_posix = lean_path.as_posix()
        file_caption = "/".join(prefixed_path.parts) + ".lean"
        lean_prefixed_relative_parts = prefixed_relative_parts.copy()
        lean_prefixed_relative_parts[-1] = lean_prefixed_relative_parts[-1] + ".lean"
        lean_prefixed_posix = Path(*lean_prefixed_relative_parts).as_posix()
        contents = f"""-- {lean_prefixed_posix}
        """
        # Now that we've made the directory, write file description files, and
        # import the file descriptor files.
        contents = contents + f"""
-- Imports for contained files or directories.
"""
        if len(files) > 0:
            for file in files:
                self.make_file_description(root, file)
                file_parts = quoted_prefixed_relative_parts + [f"«{self.prefix}{file}»"]
                import_text = f"""import {".".join(file_parts)}\n"""
                contents = contents + import_text

        if len(dirs) > 0:
            for d in dirs:
                dir_parts = quoted_prefixed_relative_parts + [f"«{self.prefix}{d}»"]
                import_text = f"""import {".".join(dir_parts)}\n"""
                contents = contents + import_text
                pass

        contents = contents + f"""-- End of Imports.\n"""

        contents = contents + f"""

import VersoManual
import VersoExts
open Verso.Genre Manual
open Verso.Genre.Manual.InlineLean

#doc (Manual) "`{abbrev_relative_text}/`"  =>

%%%
authors := {self.authors}
tag := "{hyphen_text}"
%%%
"""
        if self.vscode_links:
            lean_relative_path = lean_path.relative_to(self.output_path)
            contents = contents + f"""\n{{editlink "{lean_relative_path}"}}[edit]\n"""

        contents = contents + f"""
TODO

"""
        for file in files:
            file_parts = quoted_prefixed_relative_parts + [f"«{self.prefix}{file}»"]
            include_text = f"""{{include 1 {".".join(file_parts)}}}\n"""
            contents = contents + include_text

        for d in dirs:
            dir_parts = quoted_prefixed_relative_parts + [f"«{self.prefix}{d}»"]
            include_text = f"""{{include 1 {".".join(dir_parts)}}}\n"""
            contents = contents + include_text
            pass


        lean_path.write_text(contents)
        pass


    def traverse(self, dirpath):
        for root, dirs, files in os.walk(dirpath):
            root_path = Path(root)
            root_path_parts = list(root_path.parts)
            relative_root_parts = root_path_parts[len(self.path_parts):]
            updated_dirs = []
            for d in dirs:
                if d.startswith("."):
                    continue
                if d in self.dir_excludes:
                    continue
                d_path = Path(*(relative_root_parts + [d])).as_posix()
                if d_path in self.path_excludes:
                    continue
                updated_dirs.append(d)

            updated_dirs.sort()
            dirs[:] = updated_dirs
            updated_files = []
            for f in files:
                if not self.include_dot_files and f.startswith("."):
                    continue
                updated_files.append(f)
            files[:] = updated_files
            files.sort()
            self.make_verso(root, dirs, files)
            pass

    def write_lakefile(self):
        """
        Write the lakefile.toml
        """
        contents = f"""name = "internals"
version = "0.1.0"
defaultTargets = ["internals"]

[[require]]
name = "verso"
git = "https://github.com/leanprover/verso"
rev = "main"

[[require]]
name = "versoexts"
git = "https://github.com/richardlford/versoexts"
rev = "main"

[[lean_lib]]
name = "{self.prefix}{self.lib_name}"

[[lean_exe]]
name = "internals"
root = "Main"
"""
        self.write_file(os.path.join(self.output_dir, "lakefile.toml"), contents)
        pass

    def write_serve_py(self):
        """
        Write the serve.py script.
        """
        contents = f"""#!/usr/bin/env python3

# This wrapper turns off the Python HTTP server's overly aggressive
# cache headers, which can get in the way of Verso hovers.

from http import server # Python 3
from http.server import ThreadingHTTPServer, test
import os


class NonCachingHTTPRequestHandler(server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_my_headers()
        server.SimpleHTTPRequestHandler.end_headers(self)

    def send_my_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")

if __name__ == '__main__':
    import argparse
    import contextlib

    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--bind', metavar='ADDRESS',
                        help='bind to this address '
                             '(default: all interfaces)')
    parser.add_argument('-d', '--directory', default="_out",
                        help='serve this directory '
                             '(default: out)')
    parser.add_argument('-p', '--protocol', metavar='VERSION',
                        default='HTTP/1.0',
                        help='conform to this HTTP version '
                             '(default: %(default)s)')
    parser.add_argument('port', default={self.port}, type=int, nargs='?',
                        help='bind to this port '
                             '(default: %(default)s)')
    args = parser.parse_args()

    # ensure dual-stack is not disabled; ref #38907
    class DualStackServer(ThreadingHTTPServer):

        def server_bind(self):
            # suppress exception when protocol is IPv4
            with contextlib.suppress(Exception):
                self.socket.setsockopt(
                    socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
            return super().server_bind()

        def finish_request(self, request, client_address):
            self.RequestHandlerClass(request, client_address, self,
                                     directory=args.directory)

    print(args)

    test(
        HandlerClass=NonCachingHTTPRequestHandler,
        ServerClass=DualStackServer,
        port=args.port,
        bind=args.bind,
        protocol=args.protocol,
    )
"""
        self.write_file(os.path.join(self.output_dir, "serve.py"), contents)
        pass

    def write_main(self):
        """
        Write the Main.lean file.
        """
        contents = f"""/-
Copyright (c) 2024-2025 Lean FRO LLC. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Author: David Thrane Christiansen
-/

import Std.Data.HashMap
import VersoManual
import «{self.prefix}{self.lib_name}»

open Verso Doc
open Verso.Genre Manual

open Std (HashMap)

def config : RenderConfig where
  emitTeX := false
  emitHtmlSingle := .no
  emitHtmlMulti := .immediately
  htmlDepth := 3

def main := manualMain (%doc «{self.prefix}{self.lib_name}») (config := config)
"""
        self.write_file(os.path.join(self.output_dir, "Main.lean"), contents)
        pass

    def write_toolchain(self):
        contents = f"""{self.lean_toolchain}
        """
        self.write_file(os.path.join(self.output_dir, "lean-toolchain"), contents)
        pass

    def get_existing_documentation_files(self):
        """
        Get the existing documentation files in the output directory.
        :return: A set of paths to the existing documentation files, and a sorted list of the paths.
        """
        existing_file_set = set()
        for root, dirs, files in os.walk(self.output_dir):
            updated_dirs = []
            for d in dirs:
                if not d.startswith(self.prefix):
                    continue
                updated_dirs.append(d)
            updated_dirs.sort()
            dirs[:] = updated_dirs

            for file in files:
                if file.startswith(self.prefix) and file.endswith(".lean"):
                    file_path = Path(root) / file
                    existing_file_set.add(file_path)
        existing_file_list = list(existing_file_set)
        existing_file_list.sort()
        return existing_file_set, existing_file_list

    def get_updated_documentation_files(self):
        """
        Using the logic of traverse, make_verso, and make_file_description,
        get the set of updated documentation files.
        """
        updated_file_set = set()
        for root, dirs, files in os.walk(self.path):
            this_dir = os.path.basename(root)
            if this_dir[0] == '.':
                continue
            root_path = Path(root)
            root_path_parts = list(root_path.parts)
            relative_root_parts = root_path_parts[len(self.parent_path_parts):]
            updated_dirs = []
            for d in dirs:
                if d.startswith("."):
                    continue
                if d in self.dir_excludes:
                    continue
                d_path = Path(*(relative_root_parts + [d])).as_posix()
                if d_path in self.path_excludes:
                    continue
                updated_dirs.append(d)

            updated_dirs.sort()
            dirs[:] = updated_dirs

            prefixed_relative_parts = [f"{self.prefix}{part}" for part in relative_root_parts]
            this_parts = self.output_parts + prefixed_relative_parts
            lean_parts = this_parts.copy()
            lean_parts[-1] = lean_parts[-1] + ".lean"
            lean_path = Path(*lean_parts)
            updated_file_set.add(lean_path.as_posix())

            updated_files = []
            for f in files:
                if not self.include_dot_files and f.startswith("."):
                    continue
                updated_files.append(f)
            files[:] = updated_files
            files.sort()

            for file in files:
                file_relative_root_parts = relative_root_parts.copy()
                file_relative_root_parts.append(file)
                file_prefixed_relative_parts = [f"{self.prefix}{part}" for part in file_relative_root_parts]
                lean_parts = self.output_parts + file_prefixed_relative_parts
                lean_parts[-1] = lean_parts[-1] + ".lean"
                lean_path = Path(*lean_parts)
                lean_posix = lean_path.as_posix()
                updated_file_set.add(lean_posix)
        updated_file_list = list(updated_file_set)
        updated_file_list.sort()
        return updated_file_set, updated_file_list

    def update_tree(self):
        """
        Update the verso documentation tree after addition or deletion of files and directories.
        :return: None
        """

        # For now, assume lakefile, serve.py, toolchain and the main file do not need changes.
        # self.write_lakefile()
        # self.write_serve_py()
        # self.write_main()
        # self.write_toolchain()
        existing_file_set, existing_file_list = self.get_existing_documentation_files()
        updated_file_set, updated_file_list = self.get_updated_documentation_files()

        pass

def parse_args():
    parser = argparse.ArgumentParser(description="Produce verso documentation skeleton for a directory tree.")
    parser.add_argument('--root-dir', required=True, help='Path to directory for which to produce documentation.')
    parser.add_argument('--output-dir', required=True, help='Output directory where the output will be stored.')
    parser.add_argument('--port', default=8000, type=int, nargs='?',
                        help='bind to this port '
                             '(default: %(default)s)')
    parser.add_argument('--abbrev-level', default=3, type=int,
                        help='Number of path components to include in the abbreviated path (default: %(default)s).')
    parser.add_argument('--lean-toolchain', default="leanprover/lean4:v4.31.0", help='Lean toolchain to use.')
    parser.add_argument('--authors', nargs="*", type=str, default=["Richard L Ford"], help='Authors to list in the verso documentation.')
    parser.add_argument('--path-excludes', nargs="*", type=str, default=["tests"], help='Directory paths to exclude from the documentation (default tests).')
    parser.add_argument('--dir-excludes', nargs="*", type=str, default=["tests", "build"],
                        help='''Simple directory names to exclude from the documentation (default ["tests", "build"]).
                        Also, all directories starting with "." are automatically excluded.''')
    parser.add_argument('--prefix', default="Vtd_", help='Prefix to add to files to avoid collisions (default Vtd_).')
    parser.add_argument('--vscode-links', action='store_true',
                        help='Include source links in the generated documentation.')
    parser.add_argument('--include-dot-files', action='store_true',
                        help='Include dot files in the generated documentation.')
    parser.add_argument('--update', action='store_true',
                        help='Update existing documentation rather than making new documentation.')
    parser.add_argument('--overwrite', action='store_true',
                        help='Give permission to overwrite existing files.')
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    current_path = args.root_dir
    vtd = VersoTreeDoc(args)
    if vtd.update:
        vtd.update_tree()
    else:
        vtd.write_lakefile()
        vtd.write_serve_py()
        vtd.write_main()
        vtd.write_toolchain()
        vtd.traverse(current_path)
    pass

if __name__ == "__main__":
    main()

