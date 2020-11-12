### Well, this kind of unmet dependency occures mostly when you mess around with the sources list.

***now, if you're running a stable release of distro and used the unstable sources to install somethin, please add that too. else, some other dependency may occur too.***

#### First things first,

****install ``gcc-8-base`` by typing ``sudo apt install gcc-8-base`` if already installed****

##### install ``gcc-9-base`` type-in,  ``sudo apt install gcc-9-base``

***This will fix it.***

at end of the installation if you see something like ``couldn't configure libc6:amd64`` then just reinstall ``libc6``

by typing, ``apt reinstall libc6``
