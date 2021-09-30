# Equals (#=)


<p align="center">
  <img src="gif/rec2.gif" alt="animated" />
</p>

Equals is a result of a search for a simple text editor based calculator, the idea came from [Calca](http://calca.io/) which is great but lacking linux support and is not maintained very much. Equals takes python code or markdown with python code blocks and append intermediate results to expressions followed by `#=`.

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

## Similar tools

 - [Calca](http://calca.io/) great, but closed source, unmantained and lacking linux support.
 - [codi.vim](https://github.com/metakirby5/codi.vim) was close but the results are not persistent, does not support `a = 1 + b #=`, and used has no control what result are included.
 - ...

## Roadmap

 - [x] Support for assignments i.e. `a = 1 + 2 #= 3`
 - [x] Vim integration
 - [ ] Async vim integration
 - [ ] Multiline results
 - [x] Move to click and setup tools
 - [ ] Improved formating
 - [ ] Improved error handling
 - [ ] Markdown support
   - [x] Basic support for code blocks
   - [ ] Support for inline code in `a #=`






