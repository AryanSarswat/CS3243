#!/bin/bash
function func {
count=1
echo Called with $# parameters.
echo -e \$1 is $1
echo -e \$2 is $2
echo -e \$@ is $@
echo -e \$$ is $$

for i in $@; do
echo Parameter $count is $i
let count=count+1
done
return 55;
9
}
func hello world 13.5
echo $?
