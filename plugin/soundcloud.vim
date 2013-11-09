if !has('python')
    echo "Error: Required vim compiled with +python"
    finish
endif

if exists('g:vim_soundcloud_module')
    finish
endif
let g:vim_soundcloud_module = 1

if !exists('g:vim_soundcloud_root') || g:vim_soundcloud_root == ''
    let g:vim_soundcloud_root = expand("<sfile>:p:h")
endif

if !exists('g:vim_soundcloud_config') || g:vim_soundcloud_config == ''
    let g:vim_soundcloud_config = g:vim_soundcloud_root."/default.json"
endif


python << EOF
import sys, vim
sys.path.append(vim.eval("g:vim_soundcloud_root"))
EOF

function! SoundPlay()

python << EOF

script_path = vim.eval("g:vim_soundcloud_root") + "/" + "play.sh"

from soundcloud import play
play(script_path)

EOF
endfunction

function! NextTrack()

python << EOF

from soundcloud import next
next()

EOF
endfunction

function! StopPlay()

python << EOF

from soundcloud import stop
stop()

EOF
endfunction

function! GetInfo()

python << EOF

from soundcloud import get_info
get_info()

EOF
endfunction

function! SetGenres(...)

python << EOF

from soundcloud import set_genres
genres = vim.eval("a:000")
set_genres(genres)

EOF

endfunction



if !exists(":SoundPlay")
    command SoundPlay :call SoundPlay()
endif
if !exists(":NextTrack")
    command NextTrack :call NextTrack()
endif
if !exists(":Stop")
    command StopPlay :call StopPlay()
endif

if !exists(":GetInfo")
    command GetInfo :call GetInfo()
endif

if !exists(":SetGenres")
    command -nargs=* SetGenres call SetGenres(<f-args>)
endif

autocmd VimLeave * :call StopPlay()
