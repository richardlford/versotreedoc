-- /home/fordrl/e/versotreedoc/Examples/versodoc/Vtd_src/Vtd_verso-search.lean
        

-- Imports from child directories.

import «Vtd_src».«Vtd_verso-search».«Vtd_VersoSearch»

-- End of Imports from child directories.



import VersoManual
-- This gets access to most of the manual genre (which is also useful for textbooks)
open Verso.Genre Manual

-- This gets access to Lean code that's in code blocks, elaborated in the same process and
-- environment as Verso
open Verso.Genre.Manual.InlineLean

#doc (Manual) "`src/verso-search`"  =>

%%%
authors := ["Richard L Ford"]
tag := "src/verso-search"
%%%

TODO


{include «Vtd_src».«Vtd_verso-search».«Vtd_VersoSearch»}

# Files in `src/verso-search`
%%%
tag := "src/verso-search-files"
%%%

: `VersoSearch.lean`

  TODO

