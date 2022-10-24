#Path to CSV 
#Resources\election_results.csv

#Pesudocode
#1 Open the data file.
#2 Write down the names of all the candidates.
#3 Add a vote count for each candidate.
#4 Get the total votes for each candidate.
#5 Get the total votes cast for the election.

#To run a python file: python file_name.py

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime to get the present time. 
now = dt.datetime.now()
# Print the present time.
print("The time right now is", now)

#add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path.
        #VS preferes direct path for some reason...
#file_to_load = os.path.join("Resources", "election_results.csv")
file_to_load = 'C:/Users/checo/Desktop/Data_Analysis_Bootcamp/Module_3_Python/Election_analysis/Analysis/election_results.csv'
#file_to_save = os.path.join("Resources", "election_results.csv")
file_to_save = 'C:/Users/checo/Desktop/Data_Analysis_Bootcamp/Module_3_Python/Election_analysis/Analysis\election_results.txt'

# Open the election results and read the file.
with open(file_to_load) as election_data:

# Read the file object with the reader functrion.
    file_reader = csv.reader(election_data)

# Read and print the header row.
    headers = next(file_reader)
    print(headers)
    







