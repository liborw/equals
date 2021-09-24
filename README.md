# Equals (#=)

p align="center">
  <img src="gif/rec2.gif" alt="animated" />
</p>

## Usage

Command line

```sh
$ equals --help

Usage: equals [OPTIONS] [INPUT]

Options:
  -i, --in-place
  -d, --debug
  -o, --output PATH
  -u, --updates-only              Print just updates to the file
  -l, --language [python|py|mdpy]
  --help                          Show this message and exit.

```

In vim

```vim
" Map ee to run equals just for python (normal mode)
autocmd FileType python nnoremap <buffer> ee me <bar> :%!./equals<CR> <bar> 'e <bar> :delmarks e<CR>

" Map ee to run equals just for python (visual mode)
autocmd FileType python vnoremap ee c<C-R>=system('./equals -', @")<CR><ESC>
```

## Roadmap

 - [x] Support for assignments i.e. `a = 1 + 2 #= 3`
 - [x] Vim integration
 - [ ] Async vim integration
 - [ ] Multiline results
 - [x] Move to click and setup tools
 - [ ] Improved formating
 - [ ] Markdown support
   - [x] Basic support for code blocks
   - [ ] Support for inline code in `a #=`






