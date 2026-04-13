-- /home/fordrl/e/versotreedoc/Examples/versodoc/Vtd_src/Vtd_verso-blog/Vtd_VersoBlog.lean
        

-- Imports from child directories.

import «Vtd_src».«Vtd_verso-blog».«Vtd_VersoBlog».«Vtd_LiterateLeanPage»
import «Vtd_src».«Vtd_verso-blog».«Vtd_VersoBlog».«Vtd_Component»
import «Vtd_src».«Vtd_verso-blog».«Vtd_VersoBlog».«Vtd_Site»

-- End of Imports from child directories.



import VersoManual
-- This gets access to most of the manual genre (which is also useful for textbooks)
open Verso.Genre Manual

-- This gets access to Lean code that's in code blocks, elaborated in the same process and
-- environment as Verso
open Verso.Genre.Manual.InlineLean

#doc (Manual) "`src/verso-blog/VersoBlog`"  =>

%%%
authors := ["Richard L Ford"]
tag := "src/verso-blog/VersoBlog"
%%%

TODO


{include «Vtd_src».«Vtd_verso-blog».«Vtd_VersoBlog».«Vtd_LiterateLeanPage»}
{include «Vtd_src».«Vtd_verso-blog».«Vtd_VersoBlog».«Vtd_Component»}
{include «Vtd_src».«Vtd_verso-blog».«Vtd_VersoBlog».«Vtd_Site»}

# Files in `src/verso-blog/VersoBlog`
%%%
tag := "src/verso-blog/VersoBlog-files"
%%%

: `Basic.lean`

  TODO

: `Template.lean`

  TODO

: `LexedText.lean`

  TODO

: `Site.lean`

  TODO

: `Component.lean`

  TODO

: `LiterateLeanPage.lean`

  TODO

: `LiterateModuleDocs.lean`

  TODO

: `Generate.lean`

  TODO

: `Traverse.lean`

  TODO

: `Theme.lean`

  TODO

