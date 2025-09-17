
# s1_neg_macros.txt සියළුම VBA මැක්‍රෝ වල සිංහල විස්තර

මෙම Markdown ගොනුවේදී `s1_neg_macros.txt` හි සියළුම VBA මැක්‍රෝ සදහා පේළි අනුව සිංහලෙන් විස්තර ලබා දේ.

---

## Module8.bas

### Sub Marks_AN_1()
- ActiveSheet.Unprotect "lk573" — ක්‍රියාකාරී පත්‍රය ආරක්ෂාව ඉවත් කරයි (මුරපදය: lk573)
- Range("E15:AL64").Select — E15 සිට AL64 දක්වා ප්‍රදේශය තෝරයි
- Application.CutCopyMode = False — Copy/ Cut ක්‍රියාවන් අවලංගු කරයි
- Selection.FormatConditions.Add ... — තෝරාගත් ප්‍රදේශයට වර්ණකරණ නියමයන් එකතු කරයි (1-19, 20-34, 35-49, 50-64, 65-74, 75-100)
- Application.Goto Reference:="R2C1" — පත්‍රයේ R2C1 (Row 2, Column 1) වෙත යයි
- ActiveSheet.Protect "lk573" — ක්‍රියාකාරී පත්‍රය ආරක්ෂා කරයි (මුරපදය: lk573)

### Sub Pass_6_1()
- ActiveSheet.Unprotect "lk573" — ක්‍රියාකාරී පත්‍රය ආරක්ෂාව ඉවත් කරයි
- Range("A14:CE14").Select — A14 සිට CE14 දක්වා තෝරයි
- Selection.AutoFilter — තෝරාගත් ප්‍රදේශයට පෙරහන් යෙදයි
- ActiveSheet.Range("$A$14:$CE$85").AutoFilter Field:=83, Criteria1:="6/3 ????" — 83 වන තීරුවේ "6/3 ????" ලෙස පෙරහන් කරයි
- Application.Goto Reference:="R1C1" — පත්‍රයේ R1C1 වෙත යයි
- ActiveSheet.Protect "lk573" — පත්‍රය ආරක්ෂා කරයි

### Sub pass_5_1()
- ActiveSheet.Unprotect "lk573"
- Range("A14:CE14").Select
- Selection.AutoFilter
- ActiveSheet.Range("$A$14:$CE$85").AutoFilter Field:=83, Criteria1:="5/3 ????"
- Application.Goto Reference:="R1C1"
- Range("A1").Select
- ActiveSheet.Protect "lk573"

### Sub May_be_pass_1()
- ActiveSheet.Unprotect "lk573"
- Range("A14:CE14").Select
- Selection.AutoFilter
- ActiveSheet.Range("$A$14:$CE$85").AutoFilter Field:=83, Criteria1:="???? ?? ????"
- Application.Goto Reference:="R1C1"
- ActiveSheet.Protect "lk573"

### Sub Fail_1()
- ActiveSheet.Unprotect "lk573"
- Range("A14:CE14").Select
- Selection.AutoFilter
- ActiveSheet.Range("$A$14:$CE$85").AutoFilter Field:=83, Criteria1:="????? ~?"
- Application.Goto Reference:="R1C1"
- ActiveSheet.Protect "lk573"

### Sub W_9_1()
- ActiveSheet.Unprotect "lk573"
- Range("A14:CE14").Select
- Selection.AutoFilter
- ActiveSheet.Range("$A$14:$CE$85").AutoFilter Field:=83, Criteria1:="W9"
- Application.Goto Reference:="R1C1"
- Range("A1").Select
- ActiveSheet.Protect "lk573"

### Sub Filter_cl_1()
- ActiveSheet.Unprotect "lk573"
- Selection.AutoFilter
- Application.Goto Reference:="R1C1"
- ActiveSheet.Protect "lk573"

### Sub Anlays_cl_1()
- ActiveSheet.Unprotect "lk573"
- Range("E15:AL64").Select
- Selection.FormatConditions.Delete — වර්ණකරණ නියමයන් ඉවත් කරයි
- Application.Goto Reference:="R1C1"
- ActiveSheet.Protect "lk573"

### Sub Marks_an_2()
- ActiveSheet.Unprotect "lk573"
- Range("E100:AL149").Select
- Selection.FormatConditions.Add ... — වර්ණකරණ නියමයන් එකතු කරයි (1-19, 20-34, 35-49, 50-64, 65-74, 75-100)
- Application.Goto Reference:="R100C1"
- ActiveSheet.Protect "lk573"

### Sub An_cl_2()
- ActiveSheet.Unprotect "lk573"
- Range("E100:AL149").Select
- Selection.FormatConditions.Delete — වර්ණකරණ නියමයන් ඉවත් කරයි
- Application.Goto Reference:="R100C1"
- ActiveWindow.SmallScroll Down:=3 — පත්‍රය පහළට ස්ක්‍රෝල් කරයි
- ActiveSheet.Protect "lk573"

### Sub pass_6_2()
- ActiveSheet.Unprotect "lk573"
- Range("A99:CE99").Select
- Selection.AutoFilter
- ActiveSheet.Range("$A$99:$CE$170").AutoFilter Field:=83, Criteria1:="6/3 ????"
- Application.Goto Reference:="R88C1"
- ActiveSheet.Protect "lk573"

### Sub Pass_5_2()
- ActiveSheet.Unprotect "lk573"
- Range("A99:CE99").Select
- Selection.AutoFilter
- ActiveSheet.Range("$A$99:$CE$170").AutoFilter Field:=83, Criteria1:="5/3 ????"
- Application.Goto Reference:="R88C1"
- ActiveSheet.Protect "lk573"

### Sub Maybe_p_2()
- ActiveSheet.Unprotect "lk573"
- Range("A99:CE99").Select
- Selection.AutoFilter
- ActiveSheet.Range("$A$99:$CE$170").AutoFilter Field:=83, Criteria1:="???? ?? ????"
- Application.Goto Reference:="R88C1"
- ActiveSheet.Protect "lk573"

### Sub Fail_2()
- ActiveSheet.Unprotect "lk573"
- Range("A99:CE99").Select
- Selection.AutoFilter
- ActiveSheet.Range("$A$99:$CE$170").AutoFilter Field:=83, Criteria1:="????? ~?"
- Application.Goto Reference:="R88C1"
- Range("W92").Select
- ActiveSheet.Protect "lk573"

### Sub W_9_2()
- ActiveSheet.Unprotect "lk573"
- Range("A99:CE99").Select
- Selection.AutoFilter
- ActiveSheet.Range("$A$99:$CE$170").AutoFilter Field:=83, Criteria1:="W9"
- Application.Goto Reference:="R88C1"
- ActiveSheet.Protect "lk573"

### Sub Filter_clear_2()
- ActiveSheet.Unprotect "lk573"
- Selection.AutoFilter
- Application.Goto Reference:="R88C1"
- ActiveSheet.Protect "lk573"

### Sub Marks_An_3()
- ActiveSheet.Unprotect "lk573"
- Range("E186:AL235").Select
- Selection.FormatConditions.Add ... — වර්ණකරණ නියමයන් එකතු කරයි (1-19, 20-34, 35-49, 50-64, 65-74, 75-100)
- Application.Goto Reference:="R174C1"
- ActiveSheet.Protect "lk573"

### Sub Marka_An_cl_3()
- ActiveSheet.Unprotect "lk573"
- Range("E186:AL235").Select
- Selection.FormatConditions.Delete — වර්ණකරණ නියමයන් ඉවත් කරයි
- Application.Goto Reference:="R174C1"
- ActiveSheet.Protect "lk573"

### Sub pass_6_3()
- ActiveSheet.Unprotect "lk573"
- Range("A185:CE185").Select
- Selection.AutoFilter
- ActiveSheet.Range("$A$185:$CE$256").AutoFilter Field:=83, Criteria1:="6/3 ????"
- Application.Goto Reference:="R174C1"
- ActiveSheet.Protect "lk573"

### Sub pass_5_3()
- ActiveSheet.Unprotect "lk573"
- Range("A185:CE185").Select
- Selection.AutoFilter
- ActiveSheet.Range("$A$185:$CE$256").AutoFilter Field:=83, Criteria1:="5/3 ????"
- Application.Goto Reference:="R174C1"
- ActiveSheet.Protect "lk573"

### Sub May_be_Pass_3()
- ActiveSheet.Unprotect "lk573"
- Range("A185:CE185").Select
- Selection.AutoFilter
- ActiveSheet.Range("$A$185:$CE$256").AutoFilter Field:=83, Criteria1:="???? ?? ????"
- Application.Goto Reference:="R174C1"
- ActiveSheet.Protect "lk573"

### Sub fail_3()
- ActiveSheet.Unprotect "lk573"
- Range("A185:CE185").Select
- Selection.AutoFilter
- ActiveSheet.Range("$A$185:$CE$256").AutoFilter Field:=83, Criteria1:="????? ~?"
- Application.Goto Reference:="R174C1"
- ActiveSheet.Protect "lk573"

### Sub W_9_3()
- ActiveSheet.Unprotect "lk573"
- Range("A185:CE185").Select
- Selection.AutoFilter
- ActiveSheet.Range("$A$185:$CE$256").AutoFilter Field:=83, Criteria1:="W9"
- Application.Goto Reference:="R174C1"
- Range("R176").Select
- ActiveSheet.Shapes.Range(Array("Oval 4")).Select
- Selection.OnAction = "Filter_Clear_3" — "Oval 4" හැඳින්වීමේ හැඩය තෝරාගෙන "Filter_Clear_3" ක්‍රියාවට සම්බන්ධ කරයි
- ActiveSheet.Protect "lk573"

### Sub Fil_clear_3()
- ActiveSheet.Unprotect "lk573"
- Selection.AutoFilter
- Application.Goto Reference:="R174C1"
- ActiveSheet.Protect "lk573"

### Sub filter_clear_3()
- ActiveSheet.Unprotect "lk573"
- Selection.AutoFilter
- Range("A174").Select
- ActiveSheet.Protect "lk573"

### Sub All_clear()
- ActiveSheet.Unprotect "lk573"
- Range("B15:AL64").Select
- Selection.ClearContents — තෝරාගත් ප්‍රදේශයේ අන්තර්ගතය ඉවත් කරයි
- Application.Goto Reference:="R1C1"
- Application.Goto Reference:="R10C13"
- Selection.ClearContents
- Range("M11").Select
- ActiveSheet.Protect "lk573"

### Sub All_clear_2()
- ActiveSheet.Unprotect "lk573"
- Range("B100:AL149").Select
- Selection.ClearContents
- Application.Goto Reference:="R88C1"
- Application.Goto Reference:="R95C13"
- Selection.ClearContents
- Range("M96").Select
- ActiveSheet.Protect "lk573"

### Sub All_clear_3()
- ActiveSheet.Unprotect "lk573"
- Range("B186:AL235").Select
- Selection.ClearContents
- Application.Goto Reference:="R174C1"
- Range("M182").Select
- Application.Goto Reference:="R181C13"
- Selection.ClearContents
- Range("M182").Select
- ActiveSheet.Protect "lk573"

---

## අනෙක් Modules/Sheets

Module1.bas, Module2.bas, ... Sheet1.cls, Sheet2.cls, ...
- (empty macro) — මෙහි කිසිදු ක්‍රියාවක් නොමැත

---

මෙම ගොනුවේ වැඩි විස්තර අවශ්‍ය නම් කරුණාකර දැනුම් දෙන්න.