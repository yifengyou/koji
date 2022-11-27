#!/bin/bash
# we need some sanity here, plus some tests rather than 
# blindly hitting rpmbuild and cp -a

rpmbuild --define "%_topdir `pwd`" -bp --nodeps SPECS/*.spec
bpn=$( ls BUILD )
cp -a BUILD/${bpn} BUILD/${bpn}__orig
