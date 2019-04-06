import datetime
import csv
import arrow

# Python with open will auto-close after finished executing
with open('SystemTaskstest.csv') as f:
    reader = csv.reader(f)
    reader = list(reader) # Need to convert to a list to index / slice it
    # writer = csv.writer(csvfile) # To be used to generate a separate csv file; not currently implemented

    # Create a dict of header name -> column number
    headers = {col.strip(): n for n, col in enumerate(reader[0])}
    # print("headers: ", headers) # Used to display the headers and their index.
    
    # For headers_i_want, copy the output from the above print() for the data you want to display
    headers_i_want = ['Task/Step', 'Start date', 'End date', 'Status']
    # not_included = ['ing', 'Child', 'Parent', 'Reconcile', 'devices']
   
    x = 1
    for row in reader[1:]: # Skip the first row because it's the header
        if "ing" not in row[0] and "Child" not in row[0] and "Parent" not in row[0] and "Reconcile" not in row[0] and "devices" not in row[0]: 
        # and "Exporting" not in row[0]"Uploading" not in row[0] and "" :
            print("=" * 50)
            print(x, row[0])
            print("=" * 50)
            x += 1

         # Print system task, start time, end time, and task status from each task      
            ## count = 0

            for h in headers_i_want[1:]:
                print(h, " ", row[headers[h]], end='')                
                if (h == 'Start date'):
                    a = arrow.get(row[headers[h]], 'M/D/YYYY H:mm:ss a')
                if (h == 'End date'):
                    b = arrow.get(row[headers[h]], 'M/D/YYYY H:mm:ss a')
                print()
            delta = (b - a).total_seconds()
            print("This job took: ", datetime.timedelta(seconds = delta))
            print()
            print("-" * 50) 
            print()