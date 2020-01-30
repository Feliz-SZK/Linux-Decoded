# fix initrams prompt during boot || Alert /dev/sda* doesn't exist! || parrot-os 4.7 error

## *Note-* After digging for days I've come up with the reason behind this error and this isn't on the internet.
**so what we have to do is to invoke the initramfs.**

### This is a bug in parrot os 4.7 at the time I'm uploading this; but anyone can face this error even it's quite rare. it happens cause the initrd image can not be loaded. 

## boot into a live system and type in:
```bash
sudo fdisk -l
```
**check your linux file system name(in my case it's ``sda5``) and check your hard disk name in my case it's ``sda``**
**and the boot partition(with ``/`` in my case it's``sda1``)**

**type in**
```bash
sudo mount /dev/sda5 /mnt
```
### ***optional***: *if you have a separate boot partition type in``mount /dev/sda1 /mnt/boot`` for bios or* 
### *``mount /dev/sda1 /mnt/boot/efi`` for uefi.*

```bash
sudo mount --bind /dev /mnt/dev
sudo mount --bind /proc /mnt/proc
sudo mount --bind /sys /mnt/sys
sudo chroot /mnt
```
***then check***
```bash
cd /boot
ls
```
***if you find the linux image and the kernel files are inside(vmlinuz**, initrd.img etc.) then you're good to go***
**if they are not inside then scroll-down and continue from the hint of hashes #####.**
```bash
sudo update-initramfs -u 
grub-install /dev/sda
```
***for separate boot partition ``sudo grub-install --boot-directory=/mnt/boot /dev/sda``***
```bash
sudo update-grub
sudo reboot
```
### *remember don't ``umount`` the partitions*


**Now, you're inside system.**

## '##########################################'

**in case above doesn't work then after chroot  type in**
```bash
sudo apt-cache search linux-image
```
**``apt-get install linux-headers** linux-image**`` type in your prefered linux image and header as you can see in the output.**
***then type in:***
```bash
sudo install-grub /dev/sda
sudo update-grub
sudo reboot
```
## And you're done.

