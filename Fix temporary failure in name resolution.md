# Fixing Temporary failure in name Resolution in linux


# Step1:

## Check ``` /etc/resolv.conf``` file is either empty or lacking permissons

if it's empty the add 
```bash
sudo nano /etc/resolv.conf
```
Then Add: 
```
nameserver (your default gateway ip)
```
# save and restar network manager by typing `service network-manager-restart`

## If your /etc/resolv.conf is lacking permissons then type in `chmod o+r /etc/resolv.conf` or delete that file and create a new one.

## still isuues follow step2

# Step2:

## if your NetworkManager.service is masked.

## to check type in 

```bash
systemctl list-unit-files |grep Network
```
## if it's masked then trying to unmask will eventually remove the service from the `/etc/systemd/system directory.
So, It's better not to unamsk it. else installing `network-manager` will fix it.

## first we gotta access the internet from cmd.line. Type in.
```bash
dhclient Your-Interface-Name
```
`dhclient eth0` for example. if you're using wifi then follow 
**[connect wifi from terminal](https://askubuntu.com/questions/294257/connect-to-wifi-network-through-ubuntu-terminal/294320#294320)**
then type in `dhclient wlan0`

## then install network manager and restart the service

```
sudo apt install network-manager

service restart network-manager
```
To install gui, `sudo apt install network-manager-gnome`. To open it type in
`nm-connection-editor` from terminal.
## and you're done. issue is fixed.


