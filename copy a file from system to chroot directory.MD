## First check where the chroot directory is mounted(let's assume /mnt)

**after chrooting inside mnt(chroot /mnt)**

**open another terminal and type in **

```bash
sudo cp /etc/resolv.conf /mnt/etc
```
**I've booted into a live cd, mounted the root partition on /mnt and chrooted.So, I'm copying resolv.conf from the systems etc directoy
to the chrooted etc.**
