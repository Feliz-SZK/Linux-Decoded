## While upgrading your distro or more specifically while installing a new linux-image if you encontered

```bash
pigz: abort: write error on <stdout> (No space left on device)
E: mkinitramfs failure cpio 141 pigz 28
update-initramfs: failed for /boot/initrd.img-5.2.0-2parrot1-amd64 with 1.
dpkg: error processing package initramfs-tools (--configure):
 installed initramfs-tools package post-installation script subprocess returned error exit status 1
Errors were encountered while processing:
 initramfs-tools
Scanning application launchers
Updating active launchers
Done
E: Sub-process /usr/bin/dpkg returned an error code (1)
```
## It happens because there is no space left  in your boot partition

## Let's Fix it, shall we!

*So what are we gonna do is to purge one of the old kernels.*
*Type in*
```
sudo uname -r
```
**check the name of the kernel you're currently booted in**

**Now type in**
```
dpkg -l | tail -n +6 | grep -E 'linux-image-[0-9]+' | grep -Fv $(uname -r)
```
### You'll se something like 

```bash
ii  linux-image-4.19.0-6parrot3-amd64            4.19.37-6parrot3              amd64        Linux 4.19 for 64-bit PCs
rc  linux-image-4.19.37-parrot1-amd64            4.19.37-5parrot1              amd64        Linux 4.19.37 for 64-bit PCs
ii  linux-image-5.2.0-2parrot1-amd64             5.2.7-2parrot1                amd64        Linux 5.2 for 64-bit PCs
```
***so, we can delete the ones with the ``ii`` flag. don't delete the one with ``rc``.***
**here in my case linux-image 5.2 is the one i'm having problem to install,**
**So, we're not gonna delete the one which we're trying to install.**

***Let's just face it***

- ``rc``: means it has already been removed.
- ``ii``: means installed, eligible for removal.
- ``iU``: DON’T REMOVE. It means not installed, but queued for install in apt
    
### Now, type in
```bash
sudo dpkg --purge image-name
```
**ex-** ``sudo dpkg --purge linux-image-4.19.0-6parrot3-amd64``

***Done! now, type in***
```bash
sudo dpkg --configure -a
```
***Or type in***
```bash
sudo apt-get -f install
```
***Finally, type in***
```bash
sudo reboot
```
> You're done, Everything's fine now.
