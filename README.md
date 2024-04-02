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

**Windows (WSL)**

Remember to change your username.
```bash
git clone git@github.com:JosefUtbult/Qutebrowser-Setup.git ~/qutebrowser --recurse-submodules
mkdir /mnt/c/Users/<Your Username>/Application\ Data\qutebrowser
mv ~/qutebrowser /mnt/c/Users/<Your Username>/Application\ Data\qutebrowser\config
```

Now, install Quitebrowser

**Ubuntu**
```bash
sudo apt install -y qutebrowser
```

**Windows**

Download from [qutebrowser.org](https://qutebrowser.org/doc/install.html)
