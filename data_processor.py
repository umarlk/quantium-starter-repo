import csv
import os

DATA_DIR = "./data"
OUTPUT_FILE = "./output.csv"

with open(OUTPUT_FILE, "w") as outfile:
    
    writer = csv.writer(outfile)
    writer.writerow(["sales", "date", "region"])


    for filename in os.listdir(DATA_DIR):

        with open(f"{DATA_DIR}/{filename}") as input_file:
            
            reader = csv.reader(input_file)
            row_index = 0

            for input_row in reader:
                if row_index > 0:
                    product = input_row[0]
                    old_price = input_row[1]
                    quantity = input_row[2]
                    date = input_row[3]
                    region = input_row[4]

                    if product == "pink morsel":
                        price = float(old_price[1:]) 
                        sale = price * int(quantity)

                        writer.writerow([sale, date, region])
                row_index += 1
                        


        