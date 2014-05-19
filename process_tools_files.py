import os
import sys
import csv

path = '/Users/nealcaidin/Documents/tmp/Tools'

# create a dictionary to hold the sum of all percentages of tool use across file
#  (both by sites and by participants using a Python tuple construct)
aggregate_tools_percentages = {}


for file in os.listdir(path):
    current = os.path.join(path, file)
    if os.path.isfile(current) and ("csv" in current):
        csv_file = open(current,'rU')
        reader = csv.reader(csv_file)
        # reset the total events. We will use this to calculate percentages
        i = 0

        # initialize total number of tool placements that are counted for the current file, both based on
        # number of sites and based on the number of participants in the sites.
        total_by_sites_in_file = 0
        total_by_participants_in_file = 0

        #reset dictionary which will contain the data for each tool
        tools_per_file = {}

        # catching exceptions helps identify data issues
        # which need cleaning up
        try:
            for row in reader:

                i += 1
                # skip first row - header
                if i > 1 :

                    # clean up any excess white space in the tool_name
                    tool_name = row[0].strip()

                    tool_num_sites = float(row[1])
                    tool_num_participants = float(row[2])

                    # add to totals so we can figure out proportion (percentages) later
                    total_by_sites_in_file += tool_num_sites
                    total_by_participants_in_file += tool_num_participants

                    # save data for each tool from the file
                    tools_per_file[tool_name] = (tool_num_sites, tool_num_participants)


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

        # now we can calculate the relative proportion (percentage) of tool use both
        # with respect to sites and with respect to number of participants, for each tool
        for one_tool in tools_per_file:
            # calculate the proportions (percentages)
            tools_site_percentage = tools_per_file[one_tool][0] / total_by_sites_in_file
            tools_participants_percentage = tools_per_file[one_tool][1] / total_by_participants_in_file

            if aggregate_tools_percentages.has_key(one_tool):
                aggregate_tools_percentages[one_tool][0] += tools_site_percentage
                aggregate_tools_percentages[one_tool][1] += tools_participants_percentage
            else:
                aggregate_tools_percentages[one_tool] = [tools_site_percentage, tools_participants_percentage]
            

for a_tool in aggregate_tools_percentages:
    # zero index is by sites, and one index is by participants
    print a_tool, "," , aggregate_tools_percentages[a_tool][0], ",", aggregate_tools_percentages[a_tool][1]





