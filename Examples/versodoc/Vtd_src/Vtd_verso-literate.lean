-- /home/fordrl/e/versotreedoc/Examples/versodoc/Vtd_src/Vtd_verso-literate.lean
        

-- Imports from child directories.

import «Vtd_src».«Vtd_verso-literate».«Vtd_VersoLiterate»

-- End of Imports from child directories.



import VersoManual
-- This gets access to most of the manual genre (which is also useful for textbooks)
open Verso.Genre Manual

-- This gets access to Lean code that's in code blocks, elaborated in the same process and
-- environment as Verso
open Verso.Genre.Manual.InlineLean

#doc (Manual) "`src/verso-literate`"  =>

%%%
authors := ["Richard L Ford"]
tag := "src/verso-literate"
%%%

TODO


{include «Vtd_src».«Vtd_verso-literate».«Vtd_VersoLiterate»}

# Files in `src/verso-literate`
%%%
tag := "src/verso-literate-files"
%%%

: `VersoLiterate.lean`

  TODO

: `VersoLiterateMain.lean`

  TODO

