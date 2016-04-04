#!/bin/sh

path='/home/vagrant/projects/PNotes'

function add_copyright {
    ls -f $1 | while read -r file
    do
        if [ -d "$file" ]; then
            add_copyright $file
        else
            cat $file | python copyright.py --clean | python copyright.py > $file
        fi
    done
}

add_copyright $path