-- /home/fordrl/e/versotreedoc/Examples/versodoc/Vtd_src.lean
        

-- Imports from child directories.

import «Vtd_src».«Vtd_verso-html»
import «Vtd_src».«Vtd_multi-verso»
import «Vtd_src».«Vtd_verso-literate-code»
import «Vtd_src».«Vtd_verso-blog»
import «Vtd_src».«Vtd_verso-util»
import «Vtd_src».«Vtd_verso-manual»
import «Vtd_src».«Vtd_cli»
import «Vtd_src».«Vtd_verso-search»
import «Vtd_src».«Vtd_verso-literate-html»
import «Vtd_src».«Vtd_verso-tutorial»
import «Vtd_src».«Vtd_verso»
import «Vtd_src».«Vtd_verso-literate-plan»
import «Vtd_src».«Vtd_verso-literate»

-- End of Imports from child directories.



import VersoManual
-- This gets access to most of the manual genre (which is also useful for textbooks)
open Verso.Genre Manual

-- This gets access to Lean code that's in code blocks, elaborated in the same process and
-- environment as Verso
open Verso.Genre.Manual.InlineLean

#doc (Manual) "`src`"  =>

%%%
authors := ["Richard L Ford"]
tag := "src"
%%%

TODO


{include «Vtd_src».«Vtd_verso-html»}
{include «Vtd_src».«Vtd_multi-verso»}
{include «Vtd_src».«Vtd_verso-literate-code»}
{include «Vtd_src».«Vtd_verso-blog»}
{include «Vtd_src».«Vtd_verso-util»}
{include «Vtd_src».«Vtd_verso-manual»}
{include «Vtd_src».«Vtd_cli»}
{include «Vtd_src».«Vtd_verso-search»}
{include «Vtd_src».«Vtd_verso-literate-html»}
{include «Vtd_src».«Vtd_verso-tutorial»}
{include «Vtd_src».«Vtd_verso»}
{include «Vtd_src».«Vtd_verso-literate-plan»}
{include «Vtd_src».«Vtd_verso-literate»}
