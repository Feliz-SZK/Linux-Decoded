## After a lot of research and personal experiences I've come with the perfect fix, You'll not gonna find it anywhere.
## for indentation I've chosen to use the python extension.

....... So if you blew up your grub you'll see something like this when boot.......

grub>

....... let's fix it.......

....... Now type in .......

grub>ls 

....... if your boot system is uefi(considering you've chosen all files in one partition while installation otherwise a lot of them) 
         you'll see.......

grub>(hd0) (hd0,gpt5) (hd0,gpt1)

....... or if your boot scheme is bios you'll see .......

grub> (hd0) (hd0,msdos5) (hd0,msdos1)

....... so now we're gonna have to load the kernel and the initrd image, usually the kernel files lies in the boot folder inside 
 of the root folder in my case it's (hd0,msdos5). So if you're kernel files are inside the root or the linux partition,
 it's good else stay with me.......

....... So, let's start by checking(partitions can also be denoted by hd0,X   --X is your partion no let's say 
for(hd0,msdos5) you could write hd0,5) .......more details at the end of the tutorial.......

grub>ls (hd0,5)/

grub>lost+found/ bin/ boot/ cdrom/ dev/ etc/ home/  lib/
lib64/ media/ mnt/ opt/ proc/ root/ run/ sbin/ 
srv/ sys/ tmp/ usr/ var/ vmlinuz vmlinuz.old 
initrd.img initrd.img.old"""""""  (let's see inside boot)

....... type in .......

grub>ls/(hd0,5)/boot/

grub>  grub/ system.map... vmlinuz-4.19.37-parrot1-amd64... initrd.img.....     and so on  .....(if it's there then its ok other wise 
you've to look inside(ls) the other directries. In my case the kernel files are inside (hd0,1) .......

....... Now let's discuss the normal scenario in which the kernel files are inside boot .......
....... if your kernel files are in other partition scroll a little down and continue from the hint of stars .......

....... type in(Optional) .......

grub>set pager=1

....... Now select your root partition or your linux installation partition .......

grub>set root=(hd0,5)

....... Now it's time to load kernel which is inside boot directory. so the kernel file name starts 
with vmlinuz i'm writing mine make sure you write yours .......

grub>linux /boot/vmlinuz-4.19.37-parrot1-amd64 root=/dev/sda5

....... root part is optional but sometimes pc gets a kernel panic so it's better adding it .......

....... now its time to load the initrd image check the name with initrd.img and write it without mistake. I'm writing mine .......

grub> initrd /boot/initrd.img-4.19.37-parrot1-amd64

....... done now you can boot .......

grub>boot

*********************
*********************
*********************
*********************

.......Now if your kernel files are in other partition instead of linux partition/boot then you've to set that partition
as root temporarily. other wise you can't load the kernel by just mentioning it's directory. Stay with me.......

.......In my case my linux partition is (hd0,5) and my boot partition is (hd0,1) and my kernel files were inside 
the (hd0,1) partition . So let's fix it.......

grub>set pager=1  (optional)
grub>set root=(hd0,1)

.......Now it's time to load kernel which is inside it. so the kernel file name starts 
with vmlinuz i'm writing mine make sure you write yours.......

grub>linux /vmlinuz-4.19.37-parrot1-amd64 root=/dev/sda1

.......root part is optional but sometimes pc gets a kernel panic so it's better adding it.......

.......now its time to load the initrd image check the name with initrd.img and write it without mistake.
        I'm writing mine.......

grub> initrd /initrd.img-4.19.37-parrot1-amd64

.......now let's change the root directory....... 

grub>set root=(hd0,5)

....... you're done now let's boot .......

grub>boot

**** Important**** after the system boots follow this tho fix it permanently. fire up terminal and type .......

root~ sudo update-grub

root~ sudo fdisk -l

....... check the name of your drive ......

....... finally type in .......

root~ sudo grub-install /dev/sda

**** Congrats you've fixed it.......

....... Finally and most important never ever give up.......


GRUB-Identifier	  Hard Drive	    Partition	        Linux-Identifier

(hd0)	            First		                                /dev/sda

(hd0,gpt1)           First	               First	              /dev/sda1

(hd0,gpt2)           First	               Second	             /dev/sda2

(hd1)	            Second		                      /dev/sdb

(hd1,gpt2)           Second	     Second	             /dev/sdb2

(hd1,gpt5)           Second	     Fifth	             /dev/sdb5
 
