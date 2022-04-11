rm articlesDates.txt
touch articlesDates.txt

for i in {0..844}
do
   echo "Processing $i.txt"
   grep -i "[0-9]/" ./articles/$i.txt >> articlesDates.txt
done
