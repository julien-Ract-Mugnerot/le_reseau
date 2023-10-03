#Make sure inventory is reset on every use, needs to actualize original at the end thought
cp original_inventory.txt > inventory_txt
#reset inventory_report
rm inventory_report.txt
# Split
while IFS= read -r line; do
    title=$(echo "$line" | cut -d ',' -f 1)
    quantity=$(echo "$line" | cut -d ',' -f 2)
    price=$(echo "$line" | cut -d ',' -f 3)

    # Check book existence's
    if grep "^$title," current_inventory.txt; then
        # update lines
	      # echo $price
        sed -i "s/^$title,.*/$title,$quantity/" current_inventory.txt
    else
        # Add book to inventory_report.txt
	      # echo $quantity
        echo "$title,$quantity,$price" >> inventory_report.txt
    fi
done < inventory.txt
echo " ------- "
# need to check the sort
sort -o inventory_report.txt inventory report.txt
cat inventory_report.txt


# cp inventory_txt > original_inventory.txt
