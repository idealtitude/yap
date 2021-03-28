# YAP command line help

**Use the `-h` options to display the help**

It will outupt the following (at the moment (it will be enhanced with more options as the application evolves)):

```
usage: yap [-h] [-o [OUTPUT]] [-v] file

YAP, Yet Another -html pre- Processor

positional arguments:
  file                  The yap file to transpile to html

optional arguments:
  -h, --help            show this help message and exit
  -o [OUTPUT], --output [OUTPUT]
                        The destination file to output the html
  -v, --version         show program's version number and exit

Help and documentation at https://github.com/idealtitude/yap
```

## Basic usage

Open a terminal to invoke the yap transpiler:

```
yap document.yp
```

You can either specify a relative or an absolute path, both for the input and the output.

To specify an output file, use the `-o` (or `--output`) option:

```
yap document.yp -o document.html
```

Without the `-o` option, yap will produce a `yap.out.html` file in the current directory where it is used.


## TODO's

### Config file

I plan to use a config file to enhance the use of yap. Such file will be used to specify (for example) the type and the width of indentation, etc.
