# Nepal Loadshedding Unity Indicator (Py3) [:link:] [web]

Nepal Loadshedding Unity Indicator ported to py3.

Thanks to [rohit][rhoit] for the `routine.xml`. This package makes use of [batti][batti] project.

To generate the latest `routine.xml` [batti] is must.

### Cloning Project
```bash
$ git clone https://github.com/samundra/Nep_Loadshedding_Py3.git
$ cd Nep_Loadshedding_Py3
$ git submodule init
$ git submodule update
$ cd batti
$ git submodule init
$ git submodule update
```
Since, [batti] is used as submodule, and [batti] has [2utf8] as submodule, we are asking git to update all the submodule so can work on them locally. 

Now, we have to generate `routine.xml`. For the moment being this has to be done manually. It's easy. cd into [batti] then issue the below command.
```bash
$ cd batti
$ ./main.sh
$ ./main.sh -x > ../routine.xml
```
`routine.xml` should be placed in the root of the project.
 
When we are running [batti] for the first time, It will download the latest routine file from [nea][nea] website and extract the contents from it. 

### How to run

#### From command line
```bash

    $ python main.py &
```

#### For Issues
- For feature request and issues please use github issues tracker [new_issue][new_issue]

Currently there is no option for updating to the latest load-shedding routine, one has to manually update routine using 
[batti].

- Go to the batti sub-folder, and issue the following command

```bash

   $ cd batti
   $ ./main.sh -x > routine.xml
```

- Replace the old routine.xml with newly generated routine.xml and restart the unity indicator.

* There is still issue in the preference, when preference is saved, there is duplicate preference in the menu.

### References
[web]:https://github.com/samundra/Nep_Loadshedding_Py3
[rhoit]:https://github.com/rhoit
[batti]:https://github.com/foss-np/batti
[new_issue]:https://github.com/samundra/Nep_Loadshedding_Py3/issues/new
[nea]:http://www.nea.org.np/loadshedding.html
[2utf8]:https://github.com/foss-np/2utf8
