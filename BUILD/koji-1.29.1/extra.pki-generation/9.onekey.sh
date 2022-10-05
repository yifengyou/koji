#!/bin/bash

set -xe

./0.gen-ca.sh
./1.gen-cert-for-everyone.sh
./2.gen-cert-for-browser.sh
