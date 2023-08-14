So you upgraded your Python. "Now I can deploy my project," you thought. You got all the packages in place, including Certbot for SSL. Ready to generate the certs, you typed `sudo certbot -h`. And then...

```bash

pkg_resources.DistributionNotFound: The 'certbot==0.40.0' distribution was not found and is required by the application 

```

**or**


```bash

from acme.magic_typing import Union  # pylint: disable=unused-import, no-name-in-module
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'acme.magic_typing'

```

**could be**

```bash

ModuleNotFoundError: No module named '_cffi_backend'

```

You see `acme` and `cffi`? Already sitting there in pip. You tried giving certbot, certbot-apache, and certbot-nginx another go with `apt`, but damn, the same wall. Out of sheer frustration, you even threw in the pip packages. Still, no dice.

### The solution

First, uninstall everything,

let's start with the pip packages

```bash
sudo pip3 uninstall certbot certbot-nginx certbot-apache acme
pip3 uninstall certbot certbot-nginx acme
````

Remove both the `sudo` and `user` packages.

Then the package manager ones

```bash
sudo apt uninstall python3-certbot-nginx python3-certbot-apache python3-acme python3-certbot certbot
```

now, make sure certbot is completely removed from the path.

typing `certbot` in the terminal should give `command not found: certbot`

Alright, now we'll install certbot from snap

In the terminal type in,

```bash
sudo snap install certbot --classic
````

Wait for the process to complete,

then type in,

```bash
sudo certbot -h
```

And you should see the help section without any errors :)

Also, if snap is not installed in your system then just do,

```bash
sudo apt update
sudo apt install snapd
```

And run,

```bash
sudo snap install certbot --classic
```

## Why it happens

When we upgrade the system python, most of the times the preinstalled binding binaries don't point to the new python image. So certbot fails to wrap up the helper packages.

Reinstalling and fixing everything altogether can lead you into a rabbit hole, So it's better to just install it from snap for now. Later the more you use the system you'll come accross a couple of more errors like [No module named 'apt_pkg'](The%20%27certbot%3D%3D0.40.0%27%20distribution%20was%20not%20found%20and%20is%20required%20by%20the%20application.md)


Fixing it and some little ones will get you on a clean state.

*Caution:* If you have the snap package running, do not install the pip or apt-bindings for Certbot again.

This is because, in a typical system PATH chain, as shown below:

```bash
    /usr/lib/python3/dist-packages ❯ echo $PATH$
/home/kali/.cargo/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/games:/usr/games:/home/kali/.fzf/bin:/home/kali/.local/bin:/usr/lib/go/bin:/home/kali/go/bin:/snap/bin:/opt/waterfox$
```
The snap directory appears at the end of the list. Therefore, if you install Certbot again using pip or apt, the system will first look in /usr/bin or /usr/local/bin. It will find Certbot there, leading to the recurrence of those errors.