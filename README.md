# Setup

**Don't install the browser yet!**

Install python modules

**Ubuntu**
```bash
sudo apt install -y python3-pip
sudo pip install adblock
```

**Windows**
Download and install [python 3](https://www.python.org/downloads/)

Then run in CMD
```cmd
pip install adblock
```

Clone into your config folder.

**Linux**
```bash
git clone git@github.com:JosefUtbult/Qutebrowser-Setup.git ~/.config/qutebrowser/ --recurse-submodules
```

Now, install Quitebrowser

**Ubuntu**
```bash
sudo apt install -y qutebrowser
```

**Windows (WSL)**
In Windows, you will need to install Qutebrowser, remove the config folder and clone the config

Download from [qutebrowser.org](https://qutebrowser.org/doc/install.html)


Remember to change your username.
```bash
sudo rm -rf '/mnt/c/Users/<Your Username>/Application Data/qutebrowser'
git clone git@github.com:JosefUtbult/Qutebrowser-Setup.git ~/qutebrowser --recurse-submodules                                                             mkdir '/mnt/c/Users/jutb/Application Data/qutebrowser'
mv ~/qutebrowser '/mnt/c/Users/jutb/Application Data/qutebrowser/config'
```
