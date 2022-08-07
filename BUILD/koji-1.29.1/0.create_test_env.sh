#!/bin/bash

ln -svf `pwd`/cli/koji /usr/bin/koji
ln -svf `pwd`/cli/koji_cli  /usr/lib/python3.6/site-packages/koji_cli
ls -alh /usr/lib/python3.6/site-packages/koji_cli
ln -svf `pwd`/koji  /usr/lib/python3.6/site-packages/koji
ls -alh /usr/lib/python3.6/site-packages/koji
