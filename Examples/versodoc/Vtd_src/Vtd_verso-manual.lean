-- /home/fordrl/e/versotreedoc/Examples/versodoc/Vtd_src/Vtd_verso-manual.lean
        

-- Imports from child directories.

import «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual»

-- End of Imports from child directories.



import VersoManual
-- This gets access to most of the manual genre (which is also useful for textbooks)
open Verso.Genre Manual

-- This gets access to Lean code that's in code blocks, elaborated in the same process and
-- environment as Verso
open Verso.Genre.Manual.InlineLean

#doc (Manual) "`src/verso-manual`"  =>

%%%
authors := ["Richard L Ford"]
tag := "src/verso-manual"
%%%

TODO


{include «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual»}

# Files in `src/verso-manual`
%%%
tag := "src/verso-manual-files"
%%%

: `VersoManual.lean`

  TODO

