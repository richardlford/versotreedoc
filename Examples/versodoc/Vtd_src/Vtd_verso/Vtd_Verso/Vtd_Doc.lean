-- /home/fordrl/e/versotreedoc/Examples/versodoc/Vtd_src/Vtd_verso/Vtd_Verso/Vtd_Doc.lean
        

-- Imports from child directories.

import «Vtd_src».«Vtd_verso».«Vtd_Verso».«Vtd_Doc».«Vtd_Suggestion»
import «Vtd_src».«Vtd_verso».«Vtd_Verso».«Vtd_Doc».«Vtd_Concrete»
import «Vtd_src».«Vtd_verso».«Vtd_Verso».«Vtd_Doc».«Vtd_Elab»

-- End of Imports from child directories.



import VersoManual
-- This gets access to most of the manual genre (which is also useful for textbooks)
open Verso.Genre Manual

-- This gets access to Lean code that's in code blocks, elaborated in the same process and
-- environment as Verso
open Verso.Genre.Manual.InlineLean

#doc (Manual) "`src/verso/Verso/Doc`"  =>

%%%
authors := ["Richard L Ford"]
tag := "src/verso/Verso/Doc"
%%%

TODO


{include «Vtd_src».«Vtd_verso».«Vtd_Verso».«Vtd_Doc».«Vtd_Suggestion»}
{include «Vtd_src».«Vtd_verso».«Vtd_Verso».«Vtd_Doc».«Vtd_Concrete»}
{include «Vtd_src».«Vtd_verso».«Vtd_Verso».«Vtd_Doc».«Vtd_Elab»}

# Files in `src/verso/Verso/Doc`
%%%
tag := "src/verso/Verso/Doc-files"
%%%

: `Name.lean`

  TODO

: `TeX.lean`

  TODO

: `PointOfInterest.lean`

  TODO

: `Html.lean`

  TODO

: `Suggestion.lean`

  TODO

: `Concrete.lean`

  TODO

: `Helpers.lean`

  TODO

: `ArgParse.lean`

  TODO

: `Lsp.lean`

  TODO

: `Elab.lean`

  TODO

: `DocName.lean`

  TODO

