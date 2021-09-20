# Equals (#=)

Equals is simple tool that evaluates source code, and places intermediate results as comments where specified by (#=). No that this version is just a proof of concept, it was inspired by the [codi.vim](https://github.com/metakirby5/codi.vim) and calca.


## Usage

Command line

```sh
$ equals -h

 Equals a proof of concept

Usage:
    equals [options] <infile>
    equals [options] -

Options:
    -i, --in-place                  Edits file in place
    -o OUTFILE, --output OUTFILE    Output to a file
    -e, --edits
```


In vim


## Roadmap

 - [x] Support for assignments i.e. `a = 1 + 2 #= 3`
 - [ ] Multiline results
 - [ ] Markdown support
   - [ ] Basic support for code blocks
   - [ ] Support for inline code in `a #=`








