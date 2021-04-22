#!/bin/bash -l

conda activate cylc8


pandoc -t revealjs -s README.md -o slides.html
