# Fixing Temporary failure in name Resolution in Linux(Debian or Ubuntu based)


# Step1:

### Check if ``` /etc/resolv.conf``` file is empty or lacking permissions

if it's empty: create the file, 
```bash
sudo nano /etc/resolv.conf
```
Then add, 
``` bash
nameserver (your default gateway ip)
```

***If you don't know what your default gateway is type in,***

```bash
ip r | grep default
```

**Or, simply add ```nameserver 8.8.8.8``` and save the file**

### Restart network manager,


```service network-manager restart``` for old **distros**

```sudo service NetworkManager restart``` for new **distros**

### If your /etc/resolv.conf is lacking permissions, type in `chmod o+r /etc/resolv.conf` or delete that file and create a new one.

## Still having issues follow step2

# Step2:

## Check if your NetworkManager.service is masked.

**For new distros,**
```bash
systemctl list-unit-files | grep NetworkManager.service
```

**For old distros,**
```bash
systemctl list-unit-files | grep network-manager.service
```

**look for ```masked``` within the output**

#### if NetworkManager.service is masked then unmasking it will eventually remove the service from the ``/etc/systemd/system`` directory.
**So, It's better not to unmask it. else installing the ``network-manager`` package will fix it.**

### First we gotta enable the internet access from terminal. Type in.
```bash
dhclient Your-Interface-Name
```
**`dhclient eth0` for example. If you only have WIFI as a resource and don't have the GUI thing set up, follow**
**[connect wifi from terminal](https://askubuntu.com/questions/294257/connect-to-wifi-network-through-ubuntu-terminal/294320#294320)**
then type in `dhclient wlan0`

## Finally, install the ```network manager``` package and restart the service

For new **distros**,

```bash
sudo apt install network-manager
sudo service NetworkManager restart
sudo service NetworkManager status
```

For old **distros,**

```bash
sudo apt install network-manager
sudo service network-manager restart
sudo service network-manager status
```

To install the GUI, `sudo apt install network-manager-gnome`. To open it type in
`nm-connection-editor` from terminal.

## And, this should fix your issue :)


