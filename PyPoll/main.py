# Import modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Store header row (skip while looping through csvreader)
    header = next(csvreader, None)

    # Set starting variables before looping through rows...
    # To hold the total number of votes:
    number_of_votes = 0
    # Lists to hold the names of candidates and number of votes for each candidate:
    candidates = []
    candidate_total_votes = []

    # Loop through rows in CSV file to retrieve candidates and votes
    for row in csvreader:
        # Add to total number of votes
        number_of_votes += 1

        # Retrieve candidate name
        candidate_name = row[2]

        # If candidate is not already included in candidate list...
        if candidate_name not in candidates:
            # Add them to candidate list
            candidates.append(candidate_name)
            # Add a spot in the candidate votes list to hold count
            candidate_total_votes.append(0)
        
        # Tally votes
        # Loop through each person in the candidate list
        for person in candidates:
            # If the candidate for the current row of the csv file matches 
            # the current person in the list
            if candidate_name == person:
                # Retrieve the index of that person in the list so that the correct
                # vote counter can be called
                index = candidates.index(candidate_name)
                # And increase their vote count by 1
                candidate_total_votes[index] += 1
    # End loop through rows

    # Define function to run election results and generate output message
    def election_results(candidate_list, vote_list, total_vote_count):
        
        # Calculate total number of candidates in list
        number_of_candidates = len(candidate_list)

        # Set initial variable to determine number of votes for winning candidate
        winner_votes = 0

        # Empty array to hold strings to print for output message
        output_message = []
        
        # Add strings to output message for header and total votes
        output_message.append("Election Results")
        output_message.append("-------------------------")
        output_message.append(f'Total Votes: {total_vote_count}')
        output_message.append("-------------------------")
        # Loop through each candidate in list...
        for i in range(number_of_candidates):
            candidate_votes = vote_list[i]
            # Calculate % of total votes for each candidate, to 3 decimal places
            percentage = round((candidate_votes / total_vote_count) * 100, 3)
            # Find winning number of votes...
            if candidate_votes > winner_votes:
                winner_votes = candidate_votes
                # And retrieve the winning candidate's name from the list
                winner = candidate_list[i]
            # Generate string for each candidate showing results and add to output message
            output_message.append(f'{candidate_list[i]}: {percentage}% ({vote_list[i]})')
        # End loop through candidates
        # Add strings to output message for winner name
        output_message.append("-------------------------")
        output_message.append(f'Winner: {winner}')
        output_message.append("-------------------------")

        return output_message

    # Print output to terminal
    # Call in variables for results function
    for line in election_results(candidates, candidate_total_votes, number_of_votes):
        # Print each string from the output to a new line
        print(line)

    # Set output file path
    output_path = os.path.join("Analysis","election_results.txt")
    
    # Write results to text file
    with open(output_path, "w") as txtfile:
        # Call in variables for results function
        for line in election_results(candidates, candidate_total_votes, number_of_votes):
            # Print each string from the output to a new line
            txtfile.write(line + "\n")