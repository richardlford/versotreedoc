-- /home/fordrl/e/versotreedoc/Examples/versodoc/Vtd_src/Vtd_verso-blog.lean
        

-- Imports from child directories.

import «Vtd_src».«Vtd_verso-blog».«Vtd_VersoBlog»

-- End of Imports from child directories.



import VersoManual
-- This gets access to most of the manual genre (which is also useful for textbooks)
open Verso.Genre Manual

-- This gets access to Lean code that's in code blocks, elaborated in the same process and
-- environment as Verso
open Verso.Genre.Manual.InlineLean

#doc (Manual) "`src/verso-blog`"  =>

%%%
authors := ["Richard L Ford"]
tag := "src/verso-blog"
%%%

TODO


{include «Vtd_src».«Vtd_verso-blog».«Vtd_VersoBlog»}

# Files in `src/verso-blog`
%%%
tag := "src/verso-blog-files"
%%%

: `VersoBlog.lean`

  TODO

