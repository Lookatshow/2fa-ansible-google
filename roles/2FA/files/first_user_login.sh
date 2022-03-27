#!/bin/bash

user=$(whoami)
len=$(last $user | wc -l)

# 3 - 3я строка появляется при первом входе юзера, скрипт нужно расположить в ~/bash_login
if [ $len == 3 ]; then
        echo "yes"
else
        echo "no"
fi
