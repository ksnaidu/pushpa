#!/bin/bash

### -gt  --> greater than
### -lt --> lessthan
### -eq --> equal
## -ne --> not equal

NUMBER=$20
if [ $NUMBER -lt 10 ]
then
  echo "Given number $NUMBER is less than 10"
else
  echo "Given number $NUMBER is not less than 10"
fi
