# linkeroo
Don't just do, linkeroo. A shell utility tool written in python for mapping out paths of C/C++ dependencies for static linking.

## installation
<pre>
  <code>
    pip3 install linkeroo@git+https://github.com/elynch90/linkeroo/
  </code>
</pre>

## Parameters
<pre>
  <code>
    --fp: the file path to traverse, if None will default to current working directory.
    --o: the output fp for the .txt, if none will default to ./linkeroo.txt
    --suffix: the s
  </code>
</pre>
uffix of the file type. Defaults to .a

## How to run
<pre>
  <code>
    python3 -m linkeroo --fp $(pwd) --o linkeroo.txt
  </code>
</pre>
