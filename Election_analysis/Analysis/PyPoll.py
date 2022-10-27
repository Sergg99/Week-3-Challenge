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
    # This is a blank row, to give more space between code paragraphs once its ran
print("--------------------------------------------------")
print("The time right now is", now)
print("--------------------------------------------------")
# This is a blank row, to give more space between code paragraphs once its ran

print("\n")


#add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path.
        #VS preferes direct path for some reason... Tutor told me to run it with path. 
    #file_to_load = os.path.join("Resources", "election_results.csv")
#file_to_load = 'C:/Users/checo/Desktop/Data_Analysis_Bootcamp/Module_3_Python/Election_analysis/Analysis/election_results.csv'
    #file_to_save = os.path.join("Resources", "election_results.csv")
#file_to_save = 'C:/Users/checo/Desktop/Data_Analysis_Bootcamp/Module_3_Python/Election_analysis/Analysis\election_results.txt'

# Add a variable to load a file from a path.
file_to_load = os.path.join("..", "Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("..", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}
# Track the winning candidate, cote count, and percentage. 
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
# Read the file object with the reader functrion.
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to the candidate's count.
        candidate_votes[candidate_name] += 1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)
    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list. 
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # TO DO: Print out each candidate's name, vote count, and percentage of 
        # Votes to the terminal. 
        # Print the candidate name and percentages of votes.
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Determine winning vote count and candidate
        # Determine if the votes are greater than the winning count. 
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's results to the text file. 
    txt_file.write(winning_candidate_summary)
