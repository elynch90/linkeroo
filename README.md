# linkeroo
Don't just do, linkeroo. A simple shell utility tool written in python for mapping out paths of C/C++ dependencies within built libraries for easier static linking.

<img src="./static/img/logo.png" style="width:256px">

## Installation
<pre>
  <code>
    pip3 install linkeroo@git+https://github.com/elynch90/linkeroo/
  </code>
</pre>

## Parameters
<pre>
  <code>
    --fp: the file path to traverse, if None will default to current working directory.
    --o: the output fp for the .txt, if None will default to ./linkeroo.txt
    --suffix: the suffix of the file type. Defaults to .a
  </code>
</pre>


## How to run
<pre>
  <code>
    python3 -m linkeroo --fp $(pwd) --o linkeroo.txt
  </code>
</pre>

### Now you can static link against the library by ensuring all the dependencies are accounted for!
