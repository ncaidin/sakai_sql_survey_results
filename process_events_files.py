import os
import sys
import csv

path = '/Users/nealcaidin/Documents/tmp/Events'

# create events dictionaries. One for the total across all files for the detail events,
#    and another to rollup the events to their "parent" functionality.
aggregate_detail = {}
rollup_aggregate_detail = {}


for file in os.listdir(path):
    current = os.path.join(path, file)
    if os.path.isfile(current) and ("csv" in current):
        csv_file = open(current,'rU')
        reader = csv.reader(csv_file)
        # reset the total events. We will use this to calculate percentages
        i = 0

        # initialize total number of events that are counted for the current file.
        total_events_in_file = 0

        # reset dictionary for this file
        events_per_file = {}
        rollup_events_per_file = {}

        # catching exceptions helps to clean up stray
        # characters in the data
        try:
            for row in reader:

                i += 1
                # skip the first row, header


                if i > 1 :

                    # get the raw number in row[0]. The first column of this file has the number of "hits" of
                    # event.

                    # clean up event name. Strip whitespace.
                    detail_event_name = row[1].strip()

                    # proportion = float(row[2].replace(",",""))
                    events_per_file[detail_event_name] = float(row[0])
                    total_events_in_file += events_per_file[detail_event_name]

                    # events have names like content.read and content.revise
                    #   by taking the prefix (the part before the period)
                    #   we can summarize all the events of the same type (i.e. "content")
                    rollup_event_name = detail_event_name.split(".")[0]
                    if rollup_events_per_file.has_key(rollup_event_name):
                        rollup_events_per_file[rollup_event_name] += events_per_file[detail_event_name]
                    else:
                        rollup_events_per_file[rollup_event_name] = events_per_file[detail_event_name]


        except csv.Error:
            print current
            print('csv choked on line %s' % (i+1))
            raise
        except ValueError:
            print current
            print('csv choked on line %s' % (i+1))
            raise

        # Now we go through all the events read from that file
        # calculate the relative proportion to the total events in that file
        # to normalize the data, and add that number to an aggregate total across
        # all files.
        for event_name in events_per_file:
            # calculate the proportion (percentage) of the event relative to total of all events in file
            proportion = events_per_file[event_name] / total_events_in_file

            # add into an aggregate count across all files
            if aggregate_detail.has_key(event_name):
                # calculating the percentage of events relative to all events in the file
                aggregate_detail[event_name] += proportion
            else:
                # first time to see this event across files read so far.
                aggregate_detail[event_name] = proportion


            # now for the rollup aggregates. i.e. content.read and content.write events are under "content"
            # first get the aggregate name, which is the first (zero element) of the full name separated by periods.
            rollup_event_name = event_name.split(".")[0]

            if rollup_aggregate_detail.has_key(rollup_event_name):
                rollup_aggregate_detail[rollup_event_name] += proportion
            else:
                rollup_aggregate_detail[rollup_event_name] = proportion


for event_name in aggregate_detail:
    print event_name, "," , aggregate_detail[event_name]

print "------------------------------------"

for event_rollup in rollup_aggregate_detail:
    print event_rollup, ",", rollup_aggregate_detail[event_rollup]



