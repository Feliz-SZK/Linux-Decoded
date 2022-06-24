## **Fix when you can't switch to full Screen in Manjaro or any arch-distro(Vmware guest) even when open-vm-tools is installed**

**Don't try to reinstall vmware tools again as it won't work cause the script has an issue with the init.d directory**

**FIRST OF INSTALL ``open-vm-tools`` if not installed** 

### type in-

```bash
sudo pacman -S open-vm-tools
```
### Now we're to install some non-free display drivers and graphic libraries

***type in-***

```bash
sudo pacman -Su xf86-input-vmmouse xf86-video-vmware mesa gtk2 gtkmm
```
**Now all we gotta do is to edit or create the Xorg's wrapper config** 

```bash
echo needs_root_rights=yes | sudo tee -a /etc/X11/Xwrapper.config
```

**Finally enable and start the** ``vmtoolsd.service``

```zsh
sudo systemctl enable vmtoolsd

sudo systemctl start vmtoolsd
```

**Now, for instance if you've rebooted from the login screen and the resolution is not adapting**
**(Or even after starting the vmtoolsd service nothing happens only then)type in**

```zsh
sudo systemctl restart vmtoolsd
```

### And done, You're in full resolution --Congratulations
