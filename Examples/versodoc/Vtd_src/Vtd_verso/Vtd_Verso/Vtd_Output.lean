-- /home/fordrl/e/versotreedoc/Examples/versodoc/Vtd_src/Vtd_verso/Vtd_Verso/Vtd_Output.lean
        

-- Imports from child directories.

import «Vtd_src».«Vtd_verso».«Vtd_Verso».«Vtd_Output».«Vtd_Html»

-- End of Imports from child directories.



import VersoManual
-- This gets access to most of the manual genre (which is also useful for textbooks)
open Verso.Genre Manual

-- This gets access to Lean code that's in code blocks, elaborated in the same process and
-- environment as Verso
open Verso.Genre.Manual.InlineLean

#doc (Manual) "`src/verso/Verso/Output`"  =>

%%%
authors := ["Richard L Ford"]
tag := "src/verso/Verso/Output"
%%%

TODO


{include «Vtd_src».«Vtd_verso».«Vtd_Verso».«Vtd_Output».«Vtd_Html»}

# Files in `src/verso/Verso/Output`
%%%
tag := "src/verso/Verso/Output-files"
%%%

: `TeX.lean`

  TODO

: `Html.lean`

  TODO

