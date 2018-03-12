## Project Status: Abandoned

# Nepal Loadshedding Unity Indicator (Py3) [:link:] [web]

Nepal Loadshedding Unity Indicator ported to py3.

This package makes uses of [batti][batti] project, to fetch latest
routine.

### How to clone this project?

```bash
   $ git clone https://github.com/samundra/Nep_Loadshedding_Py3.git --recursive
```

Starting with *v1.6* of [batti], can be install as the package.

If you have not install batti separately use recusive to fetch [batti]
as submodule, `routine.xml` to be generated done manually.

_Note: for latest [batti] refer to its own documentation _

#### maunally generate routine.xml

- Get to the folder where Nepal Loadshedding has been cloned. open the
  submodule.

```bash
   $ ./main.sh -x > ~/.cache/routine.xml
```

**Note:** `routine.xml` should be placed in user cache

When we are running [batti] for the first time, It will download the
latest routine file from [nea][nea] website and extract the contents
from it.

### How to run unity indicator

#### From command line

```bash
   $ python main.py &
```

#### For Issues
- For feature request and issues please use github issues tracker
  [Create Issue][create_new_issue]

[web]:https://github.com/samundra/Nep_Loadshedding_Py3
[rhoit]:https://github.com/rhoit
[batti]:https://github.com/foss-np/batti
[create_new_issue]:https://github.com/samundra/Nep_Loadshedding_Py3/issues/new
[nea]:http://www.nea.org.np/loadshedding.html
[2utf8]:https://github.com/foss-np/2utf8
