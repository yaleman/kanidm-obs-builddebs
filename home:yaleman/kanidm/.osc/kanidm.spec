#
# spec file for package kanidm
#
# Copyright (c) 2021 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           kanidm
Version:        1.1.0alpha.4~git39.033b977
Release:        0
Summary:	Kanidm CLI Client
# FIXME: Select a correct license from https://github.com/openSUSE/spec-cleaner#spdx-licenses
License:        Mozilla Public License Version 2.0
URL:            https://github.com/kanidm/kanidm
BuildRequires:  git-buildpackage libudev-devel gzip libopenssl-devel git sqlite3-devel gcc sccache which pam-devel rust cargo 
Source:	        %{name}_%{version}.tar.gz	

%description
Test build package for kanidm cli

%prep
tar zxvf "${RPM_SOURCE_DIR}/rust-1.52.1-x86_64-unknown-linux-gnu.tar.gz" --directory /tmp
mkdir ~/.local
chmod +x /tmp/rust-1.52.1-x86_64-unknown-linux-gnu/install.sh
/tmp/rust-1.52.1-x86_64-unknown-linux-gnu/install.sh --disable-ldconfig --prefix=~/.local/ --without=rust-docs,clippy-preview,rust-analyzer-preview,miri-preview,rustfmt-preview,rls-preview

mkdir -p ~/.cargo/
cat > ~/.cargo/config.toml <<-'EOM'
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
EOM
echo "directory = \"$HOME/rust-vendor/\"" >> ~/.cargo/config.toml

mkdir -p "$HOME/rust-vendor/"
tar -xzf "${RPM_SOURCE_DIR}/vendor.tar.gz" --directory "$HOME/rust-vendor/"
ls -la "$HOME/rust-vendor/"

%setup -q -n %{name}-%{version}

%build
echo "Doing spec build"
PATH=~/.local/bin:$PATH cargo build --bin kanidm --release


%install
#mkdir -p  "${RPM_BUILD_ROOT}/usr/share/licenses/kanidm/"
cp LICENSE.md COPYING #"${RPM_BUILD_ROOT}/usr/share/licenses/kanidm/COPYING"

mkdir -p "${RPM_BUILD_ROOT}/usr/local/bin/"
mv target/release/kanidm "${RPM_BUILD_ROOT}/usr/local/bin/kanidm"
mkdir -p "${RPM_BUILD_ROOT}/usr/local/share/kanidm/"
cp examples/config "${RPM_BUILD_ROOT}/usr/local/share/kanidm/"
touch Changelog
cp README.md README

%post
%postun

%files
#%license COPYING
#%doc ChangeLog README
/usr/local/bin/kanidm
/usr/local/share/kanidm/config

#%changelog

