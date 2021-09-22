# Equals (#=)

Equals is simple tool that evaluates source code, and places intermediate results as comments where specified by (#=). No that this version is just a proof of concept, it was inspired by the [codi.vim](https://github.com/metakirby5/codi.vim) and calca.


## Usage

Command line

```sh
$ equals --help

Usage: equals [OPTIONS] [INPUT]

Options:
  -i, --in-place
  -d, --debug
  -o, --output PATH
  -u, --updates-only  Print just updates to the file
  --help              Show this message and exit.

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
 - [ ] Markdown support
   - [ ] Basic support for code blocks
   - [ ] Support for inline code in `a #=`








