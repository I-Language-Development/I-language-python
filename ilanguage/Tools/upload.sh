#!/bin/sh

pip3 install twine
python3 -m twine upload dist/* --username=__token__