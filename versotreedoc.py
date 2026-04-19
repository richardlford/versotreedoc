#!/usr/bin/env python3

"""
Produce verso documentation skeleton for a directory tree.

Richard L Ford, April 6,  2026
"""

import os
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

def write_file(path, contents):
    """
    Write the given contents to a file at the specified path.

    :param path: The file path where the contents will be written.
    :param contents: The string contents to write to the file.
    """
    with open(path, 'w') as f:
        f.write(contents)
    pass


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
        excludes = set()
        for exclude in args.excludes:
            excludes.add(exclude)
        self.excludes = excludes
        pass

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
        relative_text = Path(*relative_parts).as_posix()
        this_parts = self.output_parts + prefixed_relative_parts
        prefixed_path = Path(*this_parts)
        prefixed_path.mkdir(parents=True, exist_ok=True)
        lean_path = prefixed_path.with_suffix('.lean')
        lean_posix = lean_path.as_posix()
        contents = f"""-- {lean_posix}
        
"""
        if len(dirs) > 0:
            contents = contents + f"""
-- Imports from child directories.

"""

            for d in dirs:
                dir_parts = quoted_prefixed_relative_parts + [f"«{self.prefix}{d}»"]
                import_text = f"""import {".".join(dir_parts)}\n"""
                contents = contents + import_text
                pass

            contents = contents + f"""
-- End of Imports from child directories.

"""

        contents = contents + f"""

import VersoManual
-- This gets access to most of the manual genre (which is also useful for textbooks)
open Verso.Genre Manual

-- This gets access to Lean code that's in code blocks, elaborated in the same process and
-- environment as Verso
open Verso.Genre.Manual.InlineLean

#doc (Manual) "`{relative_text}`"  =>

%%%
authors := {self.authors}
tag := "{relative_text}"
%%%

TODO

"""
        if len(dirs) > 0:
            contents = contents + f"""
"""

            for d in dirs:
                dir_parts = quoted_prefixed_relative_parts + [f"«{self.prefix}{d}»"]
                include_text = f"""{{include {".".join(dir_parts)}}}\n"""
                contents = contents + include_text
                pass

        if len(files) > 0:
            contents = contents + f"""
# Files in `{relative_text}`
%%%
tag := "{relative_text}-files"
%%%

"""
            for f in files:
                contents = contents + f""": `{f}`\n\n  """
                if self.vscode_links:
                    contents = contents + f"""[source](vscode:{root}/{f})"""
                contents = contents + f"""TODO\n\n"""
            pass

# File in `{lean_posix}`
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
                d_path = Path(*(relative_root_parts + [d])).as_posix()
                if d_path in self.excludes:
                    continue
                updated_dirs.append(d)

            dirs[:] = updated_dirs
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

[[lean_lib]]
name = "{self.prefix}{self.lib_name}"

[[lean_exe]]
name = "internals"
root = "Main"
"""
        write_file(os.path.join(self.output_dir, "lakefile.toml"), contents)
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
        write_file(os.path.join(self.output_dir, "serve.py"), contents)
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
        write_file(os.path.join(self.output_dir, "Main.lean"), contents)
        pass

    def write_toolchain(self):
        contents = f"""{self.lean_toolchain}
        """
        write_file(os.path.join(self.output_dir, "lean-toolchain"), contents)
        pass

def parse_args():
    parser = argparse.ArgumentParser(description="Produce verso documentation skeleton for a directory tree.")
    parser.add_argument('--root-dir', required=True, help='Path to directory for which to produce documentation.')
    parser.add_argument('--output-dir', required=True, help='Output directory where the output will be stored.')
    parser.add_argument('--port', default=8000, type=int, nargs='?',
                        help='bind to this port '
                             '(default: %(default)s)')
    parser.add_argument('--lean-toolchain', default="leanprover/lean4:v4.30.0-rc2", help='Lean toolchain to use.')
    parser.add_argument('--authors', nargs="*", type=str, default=["Richard L Ford"], help='Authors to list in the verso documentation.')
    parser.add_argument('--excludes', nargs="*", type=str, default=["tests"], help='Directories to exclude from the documentation (default tests).')
    parser.add_argument('--prefix', default="Vtd_", help='Prefix to add to files to avoid collisions (default Vtd_).')
    parser.add_argument('--vscode-links', action='store_true',
                        help='Include source links in the generated documentation.')
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    current_path = args.root_dir
    vtd = VersoTreeDoc(args)
    vtd.write_lakefile()
    vtd.write_serve_py()
    vtd.write_main()
    vtd.write_toolchain()
    vtd.traverse(current_path)
    pass

if __name__ == "__main__":
    main()

