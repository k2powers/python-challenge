import os
import csv
#  The total number of months included in the dataset
numMonths = 0
# net of profit or loss for all months
netPL = 0
# average of net change
avgPL = 0
greatestInc = 0
greatestIncName = "start"
greatestDec = 0
greatestDecName = "start"
csvpath = os.path.join( 'Resources', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # check if there is a header (sniffer) and if so, skip it
    if csv.Sniffer().has_header(open(csvpath).read(1024)):
           csv_header = next(csvfile)
# go through line by line
    for row in csvreader:
#  Update the value for total number of months included in the dataset
        numMonths = numMonths + 1
#   * The total net amount of "Profit/Losses" over the entire period
        netPL = netPL + int(row[1])
#   * The greatest increase in profits (date and amount) over the entire period
        if int(row[1]) > int(greatestInc):
                greatestIncName = row[0]
                greatestInc = int(row[1])
#   * The greatest decrease in losses (date and amount) over the entire period
        if int(row[1]) < int(greatestDec):
                greatestDecName = row[0]
                greatestDec = int(row[1])
# * As an example, your analysis should look similar to the one below:
avgPL = int(round(netPL/numMonths,0))
print("Financial Analysis")
print("----------------------------------")
print("Total Months: ", numMonths)
print("Total:", '${:,.0f}'.format(netPL))
print("Average Change:", '${:,.0f}'.format(avgPL))
print("Greatest Increase in Profits: " + greatestIncName + " (" +'${:,.0f}'.format(greatestInc) + ")")
print("Greatest Decrease in Profits: " + greatestDecName + " (" +'${:,.0f}'.format(greatestDec) + ")")

# Specify the file to write to
# output_path = os.path.join("new.csv")

# Open and write to the file using "write" mode. Specify the variable to hold the contents
with open("pybank_results.csv",'x',newline='') as pybankcsv:
        pybankwriter = csv.writer(pybankcsv,delimiter=',')
        pybankwriter.writerow(["Financial Analysis"])
        pybankwriter.writerow(["----------------------------------"])
        pybankwriter.writerow(["Total Months: ","Total:","Average Change:","Greatest Increase in Profits Month:",
        "Greatest Increase in Profits Amount:","Greatest Decrease in Profits Month:","Greatest Decrease in Profits Amount:"])
        pybankwriter.writerow([numMonths,'${:,.0f}'.format(netPL),'${:,.0f}'.format(avgPL),
        greatestIncName, '${:,.0f}'.format(greatestInc),greatestDecName,'${:,.0f}'.format(greatestDec)])
