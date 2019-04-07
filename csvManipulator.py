""" 
This program will open a csv file, grab specific fields,
render the data in the terminal, and write a new csv file.
"""

import datetime
import csv
import arrow

# Python with open will auto-close after finished executing
with open('SystemTaskstest.csv', 'r') as f:
    with open('report.csv', 'w', newline='') as g:
        writer = csv.writer(g, delimiter=' ', quotechar='"')
        reader = csv.reader(f)
        reader = list(reader) # Need to convert to a list to index / slice it
       
        # Create a dict of header name -> column number
        headers = {col.strip(): n for n, col in enumerate(reader[0])}
        # print("headers: ", headers) # Used to display the headers and their index.
        
        # For headers_i_want, copy the output from the above print() for the data you want to display
        headers_i_want = ['Task/Step', 'Start date', 'End date', 'Status']
        
        # Headers for writing
        fieldnames = ['Task/Step', 'Start Date', 'End Date', 'Status', 'Duration']
        writer = csv.DictWriter(g, fieldnames=fieldnames)
        writer.writeheader()
        
        x = 1
        for row in reader[1:]: # Skip the first row because it's the header
            if "ing" not in row[0] and "Child" not in row[0] and "Parent" not in row[0] and "Reconcile" not in row[0] and "devices" not in row[0]: 
                print("=" * 50)
                print(x, row[0])
                print("=" * 50)
                x += 1

            # Print system task, start time, end time, and task status from each task      
                for h in headers_i_want[1:]:
                    print(h, " ", row[headers[h]], end='')                
                    if (h == 'Start date'):
                        a = arrow.get(row[headers[h]], 'M/D/YYYY H:mm:ss a')
                    if (h == 'End date'):
                        b = arrow.get(row[headers[h]], 'M/D/YYYY H:mm:ss a')
                    print()
                    
                delta = (b - a).total_seconds()
                writer.writerow({'Task/Step':row[0], 'Start Date': row[2], 'End Date': row[3], 'Status': row[4], 'Duration': datetime.timedelta(seconds = delta)})
                print("This job took: ", datetime.timedelta(seconds = delta))
                print()
                print("-" * 50) 
                print()
            


            