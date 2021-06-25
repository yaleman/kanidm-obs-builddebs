# kanidm packaging for .deb based osen

This is tested to run in the openSUSE Open Build System.

It's in two places:

- https://build.opensuse.org/package/show/home:yaleman/kanidm
- https://github.com/yaleman/kanidm-obs-builddebs

Github's so I can keep a copy of it in a place I can sign and have MFA control over...


# blah notes 2021-06-25

set  `DEBTRANSFORM-TAR-FILES: debian-files.tar.gz` in `kanidm_1.1.0alpha.4.dsc` and this happened:

``` shell
[  194s] Hardlinking //usr/src/packages/SOURCES/debian-files.tar.gz to //usr/src/packages/SOURCES.DEB/kanidm_1.1.0alpha.4~git39.033b977.orig.tar.gz
```


Changed it to `kanidm.tar.gz` and set `Source: kanidm` in `debian.control` and ... it got further...