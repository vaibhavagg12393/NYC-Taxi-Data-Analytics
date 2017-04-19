#!/bin/bash -xe
# Run this script as a bootstrap action in EMR. This will install all the
# python packages that are required by the map-reduce scripts
sudo yum install geos geos-devel

cd /usr/share
sudo wget http://download.osgeo.org/geos/geos-3.3.9.tar.bz2  # Note this changes
sudo tar -xvjf geos-3.3.9.tar.bz2
cd geos-3.3.9
sudo ./configure --enable-php && sudo make clean && sudo make
sudo make install
sudo ldconfig
sudo nano /etc/ld.so.conf
/usr/local/lib
sudo /sbin/ldconfig

wget http://download.osgeo.org/libspatialindex/spatialindex-src-1.7.0.tar.gz
tar -xvf spatialindex-src-1.7.0.tar.gz
cd spatialindex-src-1.7.0
./configure
make
sudo make install

sudo pip install rtree

sudo pip install shapely
