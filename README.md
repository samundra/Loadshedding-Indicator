# Nepal Loadshedding Unity Indicator (Py3) [:link:] [web]

Nepal Loadshedding Unity Indicator ported to py3.

Thanks to [rohit][rhoit] for the `routine.xml`. This package makes use of [batti][batti] project.

To generate the latest `routine.xml` [batti] is must.

### How to run

#### From command line
```bash

    $ python main.py &
```

#### For Issues
- For feature request and issues please use github issues tracker [new_issue][new_issue_link]

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
