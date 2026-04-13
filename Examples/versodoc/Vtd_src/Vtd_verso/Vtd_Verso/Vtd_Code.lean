-- /home/fordrl/e/versotreedoc/Examples/versodoc/Vtd_src/Vtd_verso/Vtd_Verso/Vtd_Code.lean
        

-- Imports from child directories.

import «Vtd_src».«Vtd_verso».«Vtd_Verso».«Vtd_Code».«Vtd_Highlighted»
import «Vtd_src».«Vtd_verso».«Vtd_Verso».«Vtd_Code».«Vtd_External»

-- End of Imports from child directories.



import VersoManual
-- This gets access to most of the manual genre (which is also useful for textbooks)
open Verso.Genre Manual

-- This gets access to Lean code that's in code blocks, elaborated in the same process and
-- environment as Verso
open Verso.Genre.Manual.InlineLean

#doc (Manual) "`src/verso/Verso/Code`"  =>

%%%
authors := ["Richard L Ford"]
tag := "src/verso/Verso/Code"
%%%

TODO


{include «Vtd_src».«Vtd_verso».«Vtd_Verso».«Vtd_Code».«Vtd_Highlighted»}
{include «Vtd_src».«Vtd_verso».«Vtd_Verso».«Vtd_Code».«Vtd_External»}

# Files in `src/verso/Verso/Code`
%%%
tag := "src/verso/Verso/Code-files"
%%%

: `HighlightedToTex.lean`

  TODO

: `Highlighted.lean`

  TODO

: `External.lean`

  TODO

