import os
import sys
import csv

path = '/Users/nealcaidin/Documents/tmp/Tools'

# create an events dictionary
events = {}
events_summary = {}

# keep track of the total events so we can calculate percentages at the end
sum_proportions = 0

for file in os.listdir(path):
    current = os.path.join(path, file)
    if os.path.isfile(current) and ("csv" in current):
        csv_file = open(current,'rU')
        reader = csv.reader(csv_file)
        # reset the total events. We will use this to calculate percentages
        i = 0
        # catching exceptions helps identify data issues
        # which need cleaning up
        try:
            for row in reader:

                i += 1
                # skip first row - header
                if i > 1 :
                    # some string literals representing numbers
                    # had commas in them. Needed to remove commas
                    # convert to number, which is a proportion
                    proportion = float(row[3].replace(",",""))
                    sum_proportions += proportion

                    # strip out extra whitespace
                    event_name = row[0].strip()


                    # add up the proportions for all the events across files
                    if events.has_key(event_name):
                        events[event_name] += proportion
                    else:
                        events[event_name] = proportion

        except csv.Error:
            print current
            print('csv choked on line %s' % (i+1))
            raise
        except ValueError:
            print current
            print('csv choked on line %s' % (i+1))
            raise
        except IndexError:
            print current
            print('csv choked on line %s' % (i+1))
            raise

for event in events:
    print event, "," , events[event]

print "total", ",",  str(sum_proportions)




