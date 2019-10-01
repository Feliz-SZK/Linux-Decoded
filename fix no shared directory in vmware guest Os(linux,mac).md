### Fix when you can't access the shared directory or if there is no /hgfs dir in /mnt in Vmware guest os(Linux or mac)

***First install ``open-vm-tools,`` ``fuse`` and ``open-vm-tools-desktop``***
```bash
sudo apt install open-vm-tools fuse open-vm-tools-desktop
```
***now if you don't have a /hgfs dir /mnt type these commands below if not then leave it and start from the hint of ascii's**

``sudo mkdir /mnt/hgfs``


```ascii
 __ __  _____  _____  _____ 
/  |  \/   __\/  _  \/   __\
|  _  ||   __||  _  <|   __|
\__|__/\_____/\__|\_/\_____/
 
``` 
**Now type in**

```bash
sudo mount -t fuse.vmhgfs-fuse .host:/ /mnt/hgfs -o allow_other
```

***or type in***

```
sudo /usr/bin/vmhgfs-fuse .host:/ /mnt/hgfs -o subtype=vmhgfs-fuse,allow_other
```
**now you can access the shared folder**

***Finally Create a symlink of the shared dir to Desktop***

``ln -s /mnt/hgfs/shared-directory ~/Desktop/Name-of-the-folder``

### So, this it, but if you reboot and it's gone the add any of the command at startup and everything's good to go.

***Or edit the /etc/fstab and add***
``bash
vmhgfs-fuse      /mnt/hgfs      fuse      defaults,allow_other      0      0
``
