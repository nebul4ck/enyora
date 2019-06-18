#!/bin/bash

set -u -e -o pipefail

help() {
	echo "Usage: ./make_package.sh python_version make_mode repository"
	echo "python_version: [2.7|3.6|3.7] jenkins|local buanaclient"
	exit 1
}

# check whether user had supplied -h or --help . If yes display usage
if [[ ($# == "--help") || ($# == "-h") ]]; then
	help
else
	if [ $# -ne 3 ]; then
		help
	else
		# Check python version
		if [[ ($1 == "2.7") || ($1 == "3.5") ]]; then
			PYTHON_VERSION=$1
			SET_MODE=$2
			REPO=$3
			SATINIZE_REPO=$(echo ${REPO} | tr - _)

			# PATHS
			JENKINS_BASE="/var/lib/jenkins/workspace"
			BASE="./${SATINIZE_REPO}_env"

			if [ $SET_MODE == "jenkins" ]; then
				BASE="${JENKINS_BASE}/${SATINIZE_REPO}"
			fi
		else
			help
		fi
	fi
fi

# Sync source code with package folder
echo "Sync source code with package folder..."
rsync -av --delete -r --exclude '*pyc' ${BASE}/src/${SATINIZE_REPO}/* \
	./${SATINIZE_REPO}/usr/lib/python${PYTHON_VERSION}/dist-packages/${SATINIZE_REPO}/

# Copy configuration file
echo "Copy configuration file..."
cp ${BASE}/src/${SATINIZE_REPO}.conf-prod \
	./${SATINIZE_REPO}/etc/${SATINIZE_REPO}/${SATINIZE_REPO}.conf && \
	echo "OK - ${SATINIZE_REPO}.conf-prod file sent"

# Copy executable file to system folder
echo "Copy executable file to system folder..."
cp ${BASE}/src/${SATINIZE_REPO}.py \
	./${SATINIZE_REPO}/usr/bin/${SATINIZE_REPO} && \
	echo "OK - ${SATINIZE_REPO}.py main prog file sent"

# Add executable permissions to executable file
echo "Add executable permissions to executable file..."
chmod +x ./${SATINIZE_REPO}/usr/bin/${SATINIZE_REPO} && \
	echo "OK - attr changed!"

# Make DEBIAN package
VERSION=$(grep Version: VERSION | awk '{printf $2}')
echo "Building DEBIAN pkg..."
dpkg -b ./${SATINIZE_REPO} ${SATINIZE_REPO}-${VERSION}.deb && \
	echo "OK - Built package"

exit 0