# Files lister

straiforward, a package to list all files in a project depending on the arguments given

**this is only a POC, it work, but there is a lot to do (refactoring, tests, packaging, doc...)**

## How to use it

```shell
git clone https://github.com/obliguedon/src_lister.git
cd ./src_lister
pip install .
```

then run `files-lister --help`

## Examples

Go check the [./examples](./examples) dir to see the syntax and how to use it

## What's next ?
- creating a new syntax for the filelist instead of YAML with its own extention (`*.flt` probably)
- packaging the app to publish it on pip
- a language server that check the dependencies and the default arguments ?
- a VS Code extension ?
