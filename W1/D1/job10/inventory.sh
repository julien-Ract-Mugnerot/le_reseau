txt=$(<inventory.txt)
echo "$txt"
current_txt=$(<current_inventory.txt)
echo $current_txt


cat inventory.txt> inventory
cat current_inventory.txt> current_inventory

echo inventory

echo "-----------------------------"

diff -s inventory current_inventory> inventory_report.txt

seq --separator="---" inventory_report.txt>check.txt
