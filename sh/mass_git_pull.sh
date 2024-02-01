!#/bin/bash
ls -R --directory --color=never */.git | sed 's/\/.git//' | xargs -P10 -I{} git -C {} pull
