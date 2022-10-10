# Equals (#=)


<p align="center">
  <img src="gif/rec2.gif" alt="animated" />
</p>


Equals is a result of a search for a simple text editor based calculator, the idea came from [Calca](http://calca.io/) which is great but lacking linux support and is not maintained very much. Equals takes python code or markdown with python code blocks and append intermediate results to expressions followed by `#=`.

## Installation

As neovim plugin using [vim-plug](https://github.com/junegunn/vim-plug):

```vim
Plug 'liborw/equals'
```

As neovim plugin using [vim-jetpack](https://github.com/tani/vim-jetpack):

```lua
use {'liborw/equals'}
```

As standalone tool using pip:

```shell
pip install git+https://github.com/liborw/equals.git
```

## Usage

Command line:

```sh
# equals --help
usage: equals [-h] [-i | -o OUTPUT | -u] [-d] [-l LANG] input

positional arguments:
  input                 Input file, for input from stdin use '-' as in input.

options:
  -h, --help            show this help message and exit
  -i, --in-place        Update the input file in place.
  -o OUTPUT, --output OUTPUT
                        Output file
  -u, --updates-only    Print out only updateted values in json format.
  -d, --debug           Run in debug mode.
  -l LANG, --lang LANG  Input language

Known languages: python, py, markdown, md
```

Neovim configuration:

```lua
require("equals").setup({
	set_keys = true,
})

-- or

vim.api.nvim_set_keymap('n', 'ee', '<cmd>lua require("equals").buffer()<cr>', {noremap = true})
```

## Similar tools

 - [Calca](http://calca.io/) great, but closed source, unmantained and lacking linux support.
 - [codi.vim](https://github.com/metakirby5/codi.vim) was close but the results are not persistent, does not support `a = 1 + b #=`, and used has no control what result are included.
 - ...

## What works and what is missing

 - [ ] Multiline results
 - [x] Support for assignments i.e. `a = 1 + 2 #= 3`
 - [x] Vim integration
 - [x] Move to click and setup tools
 - [x] Improved error handling
 - [x] Markdown support
   - [x] Basic support for code blocks
   - [x] Support for inline code in `a #=`
 - [ ] Add more languages
 - [ ] Highlighting

## References

 - [Vim Loop Question on Reddit](https://www.reddit.com/r/neovim/comments/mw4oe7/lua_cleaning_up_vimloopspawn_properly/)
