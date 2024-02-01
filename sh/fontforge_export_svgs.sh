fontforge -lang=ff -c 'Open($1); SelectWorthOutputting(); selection.select(("ranges"), 0xF1900, 0xF19FF); foreach Export("svg"); endloop;' ../ssk/sitelenselikiwenjuniko.ttf
