import os
import sys
import csv

path = '/Users/nealcaidin/Documents/tmp/Events'

# create an events dictionary
events = {}
events_summary = {}

# keep track of the total events so we can calculate percentages at the end
total_proportions = 0

for file in os.listdir(path):
    current = os.path.join(path, file)
    if os.path.isfile(current) and ("csv" in current):
        csv_file = open(current,'rU')
        reader = csv.reader(csv_file)
        # reset the total events. We will use this to calculate percentages
        i = 0
        # catching exceptions helps to clean up stray
        # characters in the data
        try:
            for row in reader:

                i += 1
                # skip the first row, header
                if i > 1 :
                    # the third column is index [2]
                    # it contains proportion (percent) of event hits
                    #    compared to other events in the file
                    # print("row[1] " + row[1])
                    # print ("row[1] " + row[1])
                    proportion = float(row[2].replace(",",""))
                    total_proportions += proportion

                    # clean up event name. Strip whitespace.
                    event_name = row[1].strip()

                    # events have names like content.read and content.revise
                    #   by taking the prefix (the part before the period)
                    #   we can summarize all the events of the same type
                    event_name_summary = event_name.split(".")[0]

                    # adding up the proportions across all files
                    # for a given event
                    if events.has_key(event_name):
                        events[event_name] += proportion
                    else:
                        events[event_name] = proportion

                    # adding up the proportions across all files
                    # for a given event summary (rollup)
                    if events_summary.has_key(event_name_summary):
                        events_summary[event_name_summary] += proportion
                    else:
                        events_summary[event_name_summary] = proportion


        except csv.Error:
            print current
            print('csv choked on line %s' % (i+1))
            raise
        except ValueError:
            print current
            print('csv choked on line %s' % (i+1))
            raise

for event in events:
    print event, "," , events[event]

print "total", ",",  str(total_proportions)

for event_summary in events_summary:
    print event_summary, ",", events_summary[event_summary]



