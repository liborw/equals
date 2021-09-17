

 - Vim pass selection to a command and replace the selevtion with its output:

```vim
:vnoremap qq c<C-R>=system('./equals -', @")<CR><ESC>
```
