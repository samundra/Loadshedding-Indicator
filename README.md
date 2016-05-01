# Nepal Loadshedding Unity Indicator (Py3) [:link:] [web]

Nepal Loadshedding Unity Indicator ported to py3.

Thanks to [rohit][rhoit] for the `routine.xml`. This package makes use of [batti][batti] project.

To generate the latest `routine.xml` [batti] is must.

### Screenshots
**Menu of Unity Loadshedding indicator**<br/>
![Menu of Unity Loadshedding indicator](http://i76.photobucket.com/albums/j5/alexshr/NepalLoadsheddingIndicator_zpsf696cd02.png)

**Date Converter (WIP)**<br/>
![Date Converter](http://i76.photobucket.com/albums/j5/alexshr/convertwindow_zpsfc39b116.png)

**Preference for Loadshedding**<br/>
![Preference window](http://i76.photobucket.com/albums/j5/alexshr/preferencewindow_zpsfb94dfd0.png)
- Add multiple group to the menu list

### How to clone this project?
```bash
$ git clone https://github.com/samundra/Nep_Loadshedding_Py3.git --recursive
```
Since, [batti] is used as submodule, and [batti] has [2utf8] as submodule, we are asking git to update all the submodule so can work on them locally. Now, we have to generate `routine.xml`. For the moment being this has to be done manually. It's easy. cd into [batti] then issue the below command.

_Note: Always refer to [batti] documentation to have the latest information. There might be cases when instruction provided here may not work exactly and you might need to tweak here and there_

#### Use batti to generate routine.xml
Starting with v1.6 of batti, we can directly run `sudo make install` in the root of [batti] and it will install itself. Once [batti] has been installed we can run it directly from anywhere in the commandline. Please refer to it's documentation on installations. Once batti has been installed please use below commands to generate the `routine.xml` file.

- Get to the folder where Nepal Loadshedding has been cloned. CD into the folder and use below command.

```bash
$ batti -x > routine.xml
```
**Note:** `routine.xml` should be placed in the root of the project.
 
When we are running [batti] for the first time, It will download the latest routine file from [nea][nea] website and extract the contents from it. 

### How to run unity indicator

#### From command line
```bash
    $ python main.py &
```

#### For Issues
- For feature request and issues please use github issues tracker [Create Issue][create_new_issue]


### Method 1- Generate routine.xml (recommended)

Currently there is no option to update to latest load-shedding routine, it has to be done manually. To update `routine.xml` using 
[batti]. Simply get to the Nepal Loadshedding installation directory and regenerate routine.xml file.

#### Method 2 - Alternative method 
The latest updated code in batti now makes it easy to generate routine.xml. Batti now can be invoked from anywhere in the commandline. So, now we can use the below provided commands to generate the `routine.xml` file.

```bash
   $ batti -x > routine.xml
```
- Replace the old `routine.xml` with newly generated `routine.xml` and restart the unity indicator.

* There is still issue in the preference, when preference is saved, there is duplicate loadshedding routines in the menu.

[web]:https://github.com/samundra/Nep_Loadshedding_Py3
[rhoit]:https://github.com/rhoit
[batti]:https://github.com/foss-np/batti
[create_new_issue]:https://github.com/samundra/Nep_Loadshedding_Py3/issues/new
[nea]:http://www.nea.org.np/loadshedding.html
[2utf8]:https://github.com/foss-np/2utf8
