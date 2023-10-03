
#!/bin/bash
echo >Title, Quantity, Price
# Paths
inventory_file="inventory.txt"
current_inventory_file="current_inventory.txt"
inventory_report_file"inventory_report.txt"

# Split
while IFS= read -r line; do
    title=$("$line" | cut -d ',' -f 1)
    quantity=$("$line" | cut -d ',' -f 2)
    price=$("$line" | cut -d ',' -f 3)

    # Check book existence's
    if grep "^$title," current_inventory.txt; then
        # update
	echo $price
        sed -i "s/^$title,.*/$title,$quantity/,$price/" current_inventory.txt
    else
        # Add book to inventory_report.txt
	echo $quantity
        echo "$title,$quantity,$price" >> inventory_report.txt
    fi
done < inventory.txt
echo " ------- "
cat inventory_report.txt
sort inventory_report.txt

