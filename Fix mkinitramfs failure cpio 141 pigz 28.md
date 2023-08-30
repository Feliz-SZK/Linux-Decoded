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

## Let's Fix it!

What we'll do is purge some old kernels.

**In your terminal, type in**
```
sudo uname -r
```
check the name of the kernel you're currently booted in

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

***The status breakdown***

- ``rc``: The package is already removed but some config files are still there.
- ``ii``: means installed, eligible for removal.
- ``iU``: DON’T REMOVE. It means not installed, but queued for install in apt


We can delete the ones with the ``ii`` flag. Remember never delete the ``iU``ones.
Here in my case I'm having trouble installing **linux-image 5.2**;
We'll not delete it cause we'd need it later. We'll delete the other old image(**linux-image-4.19.0-6parrot3-amd64**). You can get rid of all the linux images with the `rc` status but before doing it make sure you don't have any custom configs sitting in for that kernel.

### Let's delete the old linux image
```bash
sudo dpkg --purge image-name
```
**ex-** ``sudo dpkg --purge linux-image-4.19.0-6parrot3-amd64``

You can remove all the old kernel images with an `ii` status if you need to. But keep a few around just in case. If the latest one acts up, you'll have an old reliable one to fall back on. Better safe than sorry, especially if you're not hurting for storage space!

***Done! now, let's resume the new linux-image install***
```bash
sudo dpkg --configure -a
```
***Or type in***
```bash
sudo apt-get -f install
```
***Finally, reboot***
```bash
sudo reboot now
```
> You're done, Everything should be okay now :)
