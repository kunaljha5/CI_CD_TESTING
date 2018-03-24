#!/bin/bash
sudo cp -p /var/lib/jenkins/workspace/git-build/* /var/www/html/
RC=$?
if [[ $RC -eq 0 ]];then
	echo -e "Copy Git Package to apache home path [\tOK\t]"
else
	echo -e "Copy Git Package to apache home path [\tFAILED\t]"
    exit 127;
fi
sudo curl -s http://localhost/index.html
RC=$?
if [[ $RC -eq 0 ]];then
	echo -e "URL WORKING [\tOK\t]"
else
	echo -e "URL WORKING [\tFAILED\t]"
    exit 127;
fi
