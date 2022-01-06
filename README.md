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

As neovim plugin

```vim
Plug 'liborw/equals', {'rtp': 'vim'}
```

## Similar tools

 - [Calca](http://calca.io/) great, but closed source, unmantained and lacking linux support.
 - [codi.vim](https://github.com/metakirby5/codi.vim) was close but the results are not persistent, does not support `a = 1 + b #=`, and used has no control what result are included.
 - ...

## Roadmap

 - [x] Support for assignments i.e. `a = 1 + 2 #= 3`
 - [x] Vim integration
 - [x] Async vim integration
 - [ ] Multiline results
 - [x] Move to click and setup tools
 - [ ] Improved formating
 - [x] Improved error handling
 - [x] Markdown support
   - [x] Basic support for code blocks
   - [x] Support for inline code in `a #=`
 - [ ] Add more languages

### Known issues

 -

## References

 - [Vim Loop Question on Reddit](https://www.reddit.com/r/neovim/comments/mw4oe7/lua_cleaning_up_vimloopspawn_properly/)
