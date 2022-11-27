Welcome to git.centos.org

This git repo contains the following scripts that make interfacing with git.c.o, reimzul and nazar as easy as possible.

Tools:

 * get_sources.sh: when run from inside a package git checkout, will download the relevant non-text sources from the lookaside cache and drop them into the SOURCES/ dir; note: it will generate 0 byte files in place, rather than download them.

 * into_srpm.sh:  reconstructs the srpm from a given commit

 * centos.git.repolist.py:  This package gets list of repos from the pagure API, used to grab CentOS sources.  Requires the package 'python-requests' which is in the EPEL repo for CentOS-6.  

 * return_disttag.sh:  Extracts what appears to be the value of %{dist} from the commit message. <b>NOTE</b>: Requires the package <b>scl-utils-build</b> to be installed to use.

 * rpm-tree-prep.sh:  A very simple script that prepares a git tree for patching. (runs rpmbuild -bp on the tree)

 * show\_possible\_srpms.sh:  when run from inside a package git checkout, shows the list of possible SRPMs available to be built.

========================

Unless otherwise noted inside the code of an individual script, all scripts in this repository are licensed with the [GPL Version 2.0](http://opensource.org/licenses/GPL-2.0 "GPL Version 2.0") by default.  Community members who initially contribute a script can also choose any [OSI Approved License](http://opensource.org/licenses/alphabetical "Approved OSI Licenses") for their scripts if they would rather have something other than the default.  
