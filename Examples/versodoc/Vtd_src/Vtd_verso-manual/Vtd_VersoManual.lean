-- Vtd_src/Vtd_verso-manual/Vtd_VersoManual.lean
        
-- Imports for contained files or directories.
import «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Basic.lean»
import «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Bibliography.lean»
import «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Diagrams.lean»
import «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Docstring.lean»
import «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Draft.lean»
import «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Ext.lean»
import «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_ExternalLean.lean»
import «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Glossary.lean»
import «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_HighlightedCode.lean»
import «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Html.lean»
import «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Imports.lean»
import «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Index.lean»
import «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_InlineLean.lean»
import «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_License.lean»
import «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_LicenseInfo.lean»
import «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Linters.lean»
import «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Literate.lean»
import «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_LocalContents.lean»
import «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Marginalia.lean»
import «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Markdown.lean»
import «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Row.lean»
import «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Table.lean»
import «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_TeX.lean»
import «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_WebAssets.lean»
import «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_WordCount.lean»
import «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Docstring»
import «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Glossary»
import «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Html»
import «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_InlineLean»
import «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_LicenseInfo»
import «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_TeX»
-- End of Imports.


import VersoManual
import VersoExts
open Verso.Genre Manual
open Verso.Genre.Manual.InlineLean

#doc (Manual) "`src/verso-manual/VersoManual/`"  =>

%%%
authors := ["Richard L Ford"]
tag := "src-verso-manual-VersoManual"
%%%

{editlink "Vtd_src/Vtd_verso-manual/Vtd_VersoManual.lean"}[edit]

TODO

{include 1 «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Basic.lean»}
{include 1 «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Bibliography.lean»}
{include 1 «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Diagrams.lean»}
{include 1 «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Docstring.lean»}
{include 1 «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Draft.lean»}
{include 1 «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Ext.lean»}
{include 1 «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_ExternalLean.lean»}
{include 1 «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Glossary.lean»}
{include 1 «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_HighlightedCode.lean»}
{include 1 «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Html.lean»}
{include 1 «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Imports.lean»}
{include 1 «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Index.lean»}
{include 1 «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_InlineLean.lean»}
{include 1 «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_License.lean»}
{include 1 «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_LicenseInfo.lean»}
{include 1 «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Linters.lean»}
{include 1 «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Literate.lean»}
{include 1 «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_LocalContents.lean»}
{include 1 «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Marginalia.lean»}
{include 1 «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Markdown.lean»}
{include 1 «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Row.lean»}
{include 1 «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Table.lean»}
{include 1 «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_TeX.lean»}
{include 1 «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_WebAssets.lean»}
{include 1 «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_WordCount.lean»}
{include 1 «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Docstring»}
{include 1 «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Glossary»}
{include 1 «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_Html»}
{include 1 «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_InlineLean»}
{include 1 «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_LicenseInfo»}
{include 1 «Vtd_src».«Vtd_verso-manual».«Vtd_VersoManual».«Vtd_TeX»}
