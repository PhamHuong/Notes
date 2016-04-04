#!/usr/bin/env python

""" Git Copyright 2016 Script
Src from: http://www.mass-communicating.com/code/2013/11/08/python-versions.html
Will transform stdin to expand some keywords with git author_year, committed_year information.
Specify --clean to remove this information before commit.
Setup:
1. Copy copyright.py into your git repository
2. Run:
 git config filter.copyright.smudge 'python copyright.py'
 git config filter.copyright.clean  'python copyright.py'
 echo 'Dockerfile filter=copyright' >> .gitattributes
 echo '*.md filter=copyright' >> .gitattributes
 echo '*.py filter=copyright' >> .gitattributes
 echo 'copyright.py export-ignore' >> .gitattributes
 ...
 git add copyright.py
3. add this contents to file that you want to show the copyright year dynamic:
 Copyright
4. Installing Hooks
Now, I might forget updating the version 6f5b4c8
 file every time I change something. The way to do this in git is to add hooks.
I added two hooks to do this, a post-checkout hook and a post-commit hook.
I used the same file (the files will be run in the root directory of the repository):

#!/bin/sh

path='<absolute path to your project>'

add_copyright()
{
    ls $1 | while read -r file
    do
        if [ -d "$1/$file" ]; then
            add_copyright "$1/$file"
        else
            cat "$1/$file" | python copyright.py > temp; mv temp "$1/$file"
        fi
    done
}

add_copyright $path

"""

import sys
import subprocess
import re
from dateutil import parser


def main():
    # initialise empty here. Otherwise: forkbomb through the git calls.
    subst_list = {
        "Copyright" : "",
    }

    for line in sys.stdin:
        au_date = subprocess.Popen(('git', 'log', '--pretty=format:"%ad"', '--reverse'), stdout=subprocess.PIPE)
        author_date = subprocess.check_output(['head', '-1'], stdin=au_date.stdout)
        au_date.wait()
        author_year = parser.parse(author_date.replace('"', '')).year
        committed_date = subprocess.check_output(['git', 'log', '--pretty=format:"%cd"', '-1'])
        committed_year = parser.parse(committed_date.replace('"', '')).year

        if committed_year == author_year:
            copyright_year = '"{}"'.format(committed_year)
        else:
            copyright_year = '"{}-{}"'.format(author_year, committed_year)

        subst_list = {
            # '--dirty' could be added to the following, too, but is not supported everywhere
            "Copyright" : copyright_year
        }
        for k, v in subst_list.iteritems():
            v = re.sub(r'[\t"\']', "", v)
            rexp = "%s\s*[\s0-9\-'\"]+" % k
            line = re.sub(rexp, "%s %s " % (k, v), line)
        sys.stdout.write(line)


if __name__ == "__main__":
    main()