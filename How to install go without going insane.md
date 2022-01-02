Well, if you're tired of installing go manually, the installers polluting your ``PATH`` or ``GOROOT`` is always tripping. Then this is for ya.

To, start of we'll be installing ``GO`` directly from the repo.

If you're using ubuntu or any debian based distro, do.

```shell
sudo apt install golang -y
```

Now, ``GOLANG`` and ``GOROOT`` is already set by the binary, but the thing is, by default ``GOROOT`` will point to the ``go`` binary iteself, which will cause the error;

```shell
go: cannot find GOROOT directory: /usr/bin/go
```
or,

```shell
go: cannot find GOROOT directory: /usr/local/go
```
Now, to fix this we gotta point the ``GOROOT`` to the directory where all the other librariers, objects accociated with the ``go`` binary are present.

And, you'll find that in,
```shell
/usr/lib/go
```

So, to sum it up everything. Add this inside your ``.bashrc`` if you're using ``bash`` or ``.zshrc`` if your shell is ``zsh`` and you're good to go.

```shell
export GOROOT=/usr/lib/go
export GOPATH=$HOME/go
export PATH=$PATH:$GOROOT/bin:$GOPATH/bin
```

If you've ``GOPATH`` set then just ignore that line or you can add whatever the name prefer.

After that do,
```shell
source ~/.bashrc
```
or,
```shell
source ~/.zshrc
```
Then restart your shell(**Important**) by opening a new terminal.

Type in,
```shell
go version
```
You should see something like this,

```shell
go version go1.17.5 linux/amd64
```

Now, to uninstall ``go``, 

take backup of all your scripts and projects first.

Then do, 

```shell
sudo rm -rf $GOROOT

sudo rm -rf $GOPATH

sudo apt purge golang
```
Finally comment out all the schemas in ``.bashrc`` or in ``.zshrc``

again do, ``source ~/.bashrc`` or ``source ~/.zshrc`` based on your shell and you're clean.

I hope this helps. :)
