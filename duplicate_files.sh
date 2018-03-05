#!/bin/bash
dirname=$1
find $dirname -type f -not -name "*Track*" | 
while read vo
do
  echo `basename "$vo"`
done | awk '{arr[$0]++; next} END{for (i in arr){if(arr[i]>1){print i}}}' |
while read v1
do
  find $1 -type f -name "$v1"
  echo '-------------------'
done

