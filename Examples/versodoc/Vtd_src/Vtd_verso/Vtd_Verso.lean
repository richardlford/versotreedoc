-- /home/fordrl/e/versotreedoc/Examples/versodoc/Vtd_src/Vtd_verso/Vtd_Verso.lean
        

-- Imports from child directories.

import «Vtd_src».«Vtd_verso».«Vtd_Verso».«Vtd_Doc»
import «Vtd_src».«Vtd_verso».«Vtd_Verso».«Vtd_Instances»
import «Vtd_src».«Vtd_verso».«Vtd_Verso».«Vtd_Parser»
import «Vtd_src».«Vtd_verso».«Vtd_Verso».«Vtd_Output»
import «Vtd_src».«Vtd_verso».«Vtd_Verso».«Vtd_Code»

-- End of Imports from child directories.



import VersoManual
-- This gets access to most of the manual genre (which is also useful for textbooks)
open Verso.Genre Manual

-- This gets access to Lean code that's in code blocks, elaborated in the same process and
-- environment as Verso
open Verso.Genre.Manual.InlineLean

#doc (Manual) "`src/verso/Verso`"  =>

%%%
authors := ["Richard L Ford"]
tag := "src/verso/Verso"
%%%

TODO


{include «Vtd_src».«Vtd_verso».«Vtd_Verso».«Vtd_Doc»}
{include «Vtd_src».«Vtd_verso».«Vtd_Verso».«Vtd_Instances»}
{include «Vtd_src».«Vtd_verso».«Vtd_Verso».«Vtd_Parser»}
{include «Vtd_src».«Vtd_verso».«Vtd_Verso».«Vtd_Output»}
{include «Vtd_src».«Vtd_verso».«Vtd_Verso».«Vtd_Code»}

# Files in `src/verso/Verso`
%%%
tag := "src/verso/Verso-files"
%%%

: `SyntaxUtils.lean`

  TODO

: `Output.lean`

  TODO

: `ExpectString.lean`

  TODO

: `Method.lean`

  TODO

: `Log.lean`

  TODO

: `BEq.lean`

  TODO

: `Linters.lean`

  TODO

: `FS.lean`

  TODO

: `Instances.lean`

  TODO

: `CLI.lean`

  TODO

: `Hover.lean`

  TODO

: `Hint.lean`

  TODO

: `Code.lean`

  TODO

: `Doc.lean`

  TODO

: `Parser.lean`

  TODO

: `WithoutAsync.lean`

  TODO

