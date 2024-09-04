# linkeroo
Don't just do, linkeroo. A shell utility tool written in python for mapping out paths of C/C++ dependencies for static linking.

## installation

pip3 install linkeroo@git+https://github.com/elynch90/linkeroo/


## Parameters
--fp: the file path to traverse, if None will default to current working directory.
--o: the output fp for the .txt, if none will default to ./linkeroo.txt
--suffix: the suffix of the file type. Defaults to .a

## How to run
<pre>
  <code>
    python3 -m linkeroo --fp $(pwd) 
  </code>
</pre>
