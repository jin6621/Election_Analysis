#Add our deependencies.
import csv
import os

#Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a pth
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initilize a total vote counter
total_votes = 0

#Candidate options and candidate votes.
candidate_options = []
candidates_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


#Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read the header row.
    headers = next(file_reader)
    
    #Print each row in the CSV file.
    for row in file_reader:

        #2. Add to total vote count.
        total_votes += 1

        #Print the candidate name from each row
        candidate_name = row[2]
        
        #If the candidate does not match any existing candidates...
        if candidate_name not in candidate_options:

            #Add it to the list of candidates
            candidate_options.append(candidate_name)
            
            #Begin tracking that candidate's vote count
            candidates_votes[candidate_name] = 0
            
        #Add a vote to that candidates count
        candidates_votes[candidate_name] += 1

#save the results to our txt file
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)


    #3. Print the total votes
    #print(candidates_votes)


    #Determine the percemtage of votes for each candidate by looping through the counts. 
    #1. Iterate through the candidate list.
    for candidate_name in candidates_votes:
        
        #2. Retrieve vote count of a candidate.
        votes = candidates_votes[candidate_name]
        
        #3. Calculate the percentage of votes
        vote_perentage = (votes/total_votes) * 100

        #4. Print the candidate name and percentage of votes.
        candidate_results = (
            f"{candidate_name}: {vote_perentage:.1f}% ({votes:,})\n")

        # Print each candidate, their vote count, and percentage to the terminal.
        print(candidate_results)

        #Save the candiate results to our text file.
        txt_file.write(candidate_results)

        #Determine winning vote count and candidate
        #1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_perentage > winning_percentage):

            #2. If true then set winning_count = votes and winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_perentage

            #3. Set the winning_candidate euqal to the candidate's name
            winning_candidate = candidate_name
        
    # To do: print out the winning candidate, vote count and percentage to terminal.
    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n"
    )

    print(winning_candidate_summary)
    #Save the winning candidates' name to the text file.
    txt_file.write(winning_candidate_summary)
    