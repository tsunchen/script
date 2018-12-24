#!/bin/bash

DKR=ci
DOCKERREPO=org.chao.os:25321/firstest

set -e
#IP=`ifconfig eth0 | grep inet | awk '{print $2}' | tr -d "addr:"`

#docker tag yourreg/askworld:1.0  $IP/theHarbor/askworld:1.0
#docker tag yourreg/askworld:2.0  $IP/theHarbor/askworld:2.0
docker tag  dkr_${DKR}  ${DOCKERREOP}/${DKR}
echo "----> docker images tag Rename the image to complete."

echo "----> start uploading images to the $IP registry server"
docker push  ${DOCKERREOP}/${DKR}
#docker push $IP/theHarbor/askworld:1.0
#docker push $IP/theHarbor/askworld:2.0

echo "----> the image(s) upload to complete"


#org.chao.os:25321/firstest/
