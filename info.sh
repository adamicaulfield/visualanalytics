name="$1"

echo "--------- Unique Recipients ---------"
awk -F, -v n=$name '$1 == n' sendrecv.csv > msgs.txt
awk -F, '{print "(" $3 ")\t" $2}' msgs.txt
rm msgs.txt

echo "Date"