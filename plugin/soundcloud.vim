if !has('python')
    echo "Error: Required vim compiled with +python"
    finish
endif

if exists('g:vim_reddit_module')
    finish
endif
let g:vim_reddit_module = 1

if !exists('g:vim_reddit_root') || g:vim_reddit_root == ''
    let g:vim_reddit_root = expand("<sfile>:p:h")
endif

if !exists('g:vim_reddit_config') || g:vim_reddit_config == ''
    let g:vim_reddit_config = g:vim_reddit_root."/default.json"
endif


python << EOF
import sys, vim
sys.path.append(vim.eval("g:vim_reddit_root"))
EOF

function! Reddit()

python << EOF

from reddit import main
main()

EOF
setlocal nomodifiable
setlocal buftype=nofile
set ft=reddit
execute ":f Reddit"
endfunction

if !exists(":Reddit")
    command Reddit :call Reddit()
endif
