#!/bin/bash


DOCARGOVENDOR=0

if [ "$(dirname $0)" != "." ]; then
	echo "You should be running this from the same dir as the script"
	exit 1
fi

ORIGDIR="$(pwd)"

RAWVERSION="$(grep -E '^Version' kanidm.spec | awk '{print $NF}')"
if [ -z "${RAWVERSION}" ]; then
	echo "Version id fail, got null, bailing"
	exit 1
fi

VERSION="kanidm-${RAWVERSION}"

echo "Kanidm version: '${VERSION}'"
echo "Cloning repo"
git clone --depth 1 https://github.com/kanidm/kanidm "${VERSION}" || exit 1
rm -rf "${VERSION}/.git"

echo "Making deb things"
mkdir -p "${VERSION}/debian" || exit 1 
echo "Copying deb control in"
cp debian.control "${VERSION}/debian/control"
echo "Writing changelog"
cat > "${VERSION}/debian/changelog" <<-'EOM'
kanidm (RAWVERSION) unstable; urgency=low

  [ James Hodgkinson ]
  * I totally admit this is just filler text to convince the debian packaging system to work.

EOM

echo "Writing end of changelog"
echo " -- James Hodgkinson <james@terminaloutcomes.com>  $(date -R)" >> "${VERSION}/debian/changelog"
echo "Including version in changelog"
sed -i'' -e "s/RAWVERSION/${RAWVERSION}/" "${VERSION}/debian/changelog"
echo "Making source package"
cd "${VERSION}"
dpkg-source -b .
cd ..

#echo "DEBTRANSFORM-FILES-TAR: kanidm_${RAWVERSION}.tar.gz" >> "kanidm_${RAWVERSION}.dsc"

echo "Done with deb things"
if [ "${DOCARGOVENDOR}" -eq 1 ]; then
	echo "Vendoring cargo deps"
	cd "${VERSION}"
	cargo vendor -q

	tar cf "${ORIGDIR}/vendor.tar" --directory vendor/ './'

	cd "${ORIGDIR}"
	if [ -f "vendor.tar.gz" ]; then
		rm -f "vendor.tar.gz"
	fi
	gzip -9 "vendor.tar"
fi
#rm -rf "${VERSION}"
