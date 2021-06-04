# adding kanidm apt repo to ubuntu 21.04

add this to /etc/apt/sources.list.d/kanidm.list

```shell
deb https://download.opensuse.org/repositories/home:/yaleman/xUbuntu_21.04 ./
```

add the signing key and update apt

```
curl -fsSL https://download.opensuse.org/repositories/home:/yaleman/xUbuntu_21.04/Release.gpg | \
gpg --dearmor | \
sudo tee /usr/share/keyrings/kanidm.gpg > /dev/null
sudo apt-get update
```

Because reasons, it won't show up in apt-cache search.

```
$ apt-cache search kanidm
$
```

apt-cache show will find it though

```
yaleman@raspberrypief91:~$ apt-cache show kanidm
Package: kanidm
Version: 1.1.0alpha.4-1
Architecture: arm64
Essential: no
Maintainer: James Hodgkinson <james@terminaloutcomes.com>
Installed-Size: 6264
Filename: ./arm64/kanidm_1.1.0alpha.4-1_arm64.deb
Size: 1523200
MD5sum: 24163f33f3b28f3b32d208210dedfba0
SHA1: af20da201d9563e529133801028ae578d840d78e
SHA256: 39562093195602fc8a44b92cede1da4da76d17cf9b2882bac720c5e9bbcde931
Section: web
Priority: optional

```

