" Variables for url highlighting
" Taken from here https://github.com/vim-scripts/TwitVim
let s:URL_PROTOCOL = '\%([Hh][Tt][Tt][Pp]\|[Hh][Tt][Tt][Pp][Ss]\|[Ff][Tt][Pp]\)://'
let s:URL_PROTOCOL_HTTPS = '\%([Hh][Tt][Tt][Pp][Ss]\)://'
let s:URL_PROTOCOL_NON_HTTPS = '\%([Hh][Tt][Tt][Pp]\|[Ff][Tt][Pp]\)://'
let s:URL_DOMAIN = '[^[:space:])/]\+'
let s:URL_PATH_CHARS = '[^[:space:]()]'
let s:URL_PARENS = '('.s:URL_PATH_CHARS.'*)'
let s:URL_PATH_END = '\%([^[:space:]\.,;:()]\|'.s:URL_PARENS.'\)'
let s:URL_PATH = '\%('.s:URL_PATH_CHARS.'*\%('.s:URL_PARENS.s:URL_PATH_CHARS.'*\)*'.s:URL_PATH_END.'\)\|\%('.s:URL_PATH_CHARS.'\+\)'
let s:URLMATCH = s:URL_PROTOCOL.s:URL_DOMAIN.'\%(/\%('.s:URL_PATH.'\)\=\)\='
let s:URLMATCH_HTTPS = s:URL_PROTOCOL_HTTPS.s:URL_DOMAIN.'\%(/\%('.s:URL_PATH.'\)\=\)\='
let s:URLMATCH_NON_HTTPS = s:URL_PROTOCOL_NON_HTTPS.s:URL_DOMAIN.'\%(/\%('.s:URL_PATH.'\)\=\)\='

syntax match subreddit /^.\{-1,} ▶/

execute 'syntax match url "\<'.s:URLMATCH.'"'

syntax match author /^.\{-1,} ▷/

syntax match title /^.\{-1,} ☢/
highlight title gui=bold guifg=yellowgreen

highlight default link subreddit Identifier
highlight default link url Underlined
highlight default link author String
