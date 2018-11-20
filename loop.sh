#!/bin/bash

for i in *
do
tail -1 $i >> lastlines.txt 2>> errormessage.txt
done


