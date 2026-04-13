-- /home/fordrl/e/versotreedoc/Examples/versodoc/Vtd_src/Vtd_verso-util/Vtd_VersoUtil.lean
        

-- Imports from child directories.

import «Vtd_src».«Vtd_verso-util».«Vtd_VersoUtil».«Vtd_BinFiles»

-- End of Imports from child directories.



import VersoManual
-- This gets access to most of the manual genre (which is also useful for textbooks)
open Verso.Genre Manual

-- This gets access to Lean code that's in code blocks, elaborated in the same process and
-- environment as Verso
open Verso.Genre.Manual.InlineLean

#doc (Manual) "`src/verso-util/VersoUtil`"  =>

%%%
authors := ["Richard L Ford"]
tag := "src/verso-util/VersoUtil"
%%%

TODO


{include «Vtd_src».«Vtd_verso-util».«Vtd_VersoUtil».«Vtd_BinFiles»}

# Files in `src/verso-util/VersoUtil`
%%%
tag := "src/verso-util/VersoUtil-files"
%%%

: `BinFiles.lean`

  TODO

: `LzCompress.lean`

  TODO

: `Zip.lean`

  TODO

: `WfRec.lean`

  TODO

