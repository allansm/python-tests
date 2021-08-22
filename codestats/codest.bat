@echo off
codestats --folder %1 --extensions .py;.php;.java;.cpp;.html;.css;.js;.asm --names python;php;java;c++;html;css;javascript;assembly %2 %3
