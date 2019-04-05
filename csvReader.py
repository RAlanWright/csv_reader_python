import csv

# Python with open will auto-close after finished executing
with open('SystemTasks.csv') as f:
    reader = csv.reader(f)
    reader = list(reader) # Need to convert to a list to index / slice it
    # writer = csv.writer(csvfile) # To be used to generate a separate csv file; not currently implemented

    # Create a dict of header name -> column number
    headers = {col.strip(): n for n, col in enumerate(reader[0])}
    # print("headers: ", headers) # Used to display the headers and their index.
    # Copy these "headers" into headers_i_want below from your first run. Issue copying the emoji from excel into the editor...

    # For headers_i_want, copy the output from the above print() for the data you want to display
    headers_i_want = ['Task/Step', 'Start date', 'End date', 'Status']
    for row in reader[1:]: # Skip the first row because it's the header
        print(row[0])
        if (row is not None and row != "Importing" and row != "Export" and row != "Parent" and row != "Gathering " and row != "Uploading"): # Grab students from your section; Change this for your section
            for h in headers_i_want:
                print(h, " ", row[headers[h]], end='')
                print()
            print("-" * 40) # Separate each student
            print()