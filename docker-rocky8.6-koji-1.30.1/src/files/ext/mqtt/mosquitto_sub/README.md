git.centos.org has shifted to using [pagure](https://pagure.io/ "Pagure") to host sources. Here is how to get [Sources](https://wiki.centos.org/Sources "Sources") now from git.centos.org.

There is an example of how to use mosquitto\_sub on that page, but I find the *-v* option then requires using only the second column in the log, so I like to take it out.  Here is what I would use:

`mosquitto_sub --cafile ~/.centos-server-ca.cert --cert ~/.centos.cert --key ~/.centos.cert -h mqtt.git.centos.org -p 8883 --id` _<uniq-id>_` --disable-clean-session --keepalive -t git.centos.org/# >> `_<filepath>_`/mosquitto_sub.log.txt`

Once you have the default log going, you can parse the log as json .. I like to use [jq](https://stedolan.github.io/jq/ "jq").  Here is an example *jq* query that will create an output that looks like this for _branches_ that begin with _c7_ in the log.

`cat mosquitto_sub.log.txt  | jq -j ' . | select(.branch | startswith("c7")) | .repo.name," ",.repo.date_modified," ",.end_commit," ",.branch,"\n"' 2>/dev/null| sed -e 's,",,g'`

The output will be similar to this if an rpm update is found:

`mod_auth_mellon 1553623560 8b0a0c922f1f1b030200998f3bd069f771b4b4a5 c7`

The information is the RPM Name, Date Modfied, Git Commit ID, and Branch for the commit. 

