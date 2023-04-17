import os
import csv 

#read in csv
csvpath = os.path.join('PyPoll','Resources', 'election_data.csv')
#make variables
total_votes = []
stockham = 0
degette = 0
doane = 0

#open file
with open(csvpath,encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #ignore headers
    csv_header = next(csvreader)
    for row in csvreader:
        #get number of votes
        total_votes.append(row[0])
        #count votes for all candidate
        if row[2] == "Charles Casper Stockham":
            stockham +=1
        elif row[2] == "Diana DeGette":
            degette +=1
        elif row[2] == "Raymon Anthony Doane": 
            doane +=1

#make dictionary and list with candidates
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
candidate_votes = [stockham, degette, doane]
#use the zip function to join candidates with their votes and then obtain the winner
votes_dict = dict(zip(candidates, candidate_votes))
winner = max(votes_dict, key=votes_dict.get)

#create a variable with length of total votes
total_vote_count = len(total_votes)
#caculate percentages for each candidate
degette_percentage = (degette/total_vote_count) * 100
stockham_percentage = (stockham/total_vote_count) * 100
doane_percentage = (doane/total_vote_count) * 100

#print in terminal
print("Election Results")
print("________________")
print(f"Total Votes : {len(total_votes)}" )
print("________________")
#print percentages of votes for each candidatei and number of votes.
print(f"Charles Casper Stockham: {stockham_percentage:.3f}% ({stockham})")
print(f"Diana Degette: {degette_percentage:.3f}% ({degette})")
print(f"Raymon Anthony Doane: {doane_percentage:.3f}% ({doane})")
print("________________")
print(f"Winner: {winner}")


#export results in a text file
analysis = os.path.join('PyPoll',"Resources", "Results.txt")
with open(analysis,"w") as file:

    file.write("Election Results")
    file.write("\n")
    file.write("________________")
    file.write("\n")
    file.write(f"Total Votes : {len(total_votes)}" )
    file.write("\n")
    file.write("________________")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {stockham_percentage:.3f}% ({stockham})")
    file.write("\n")
    file.write(f"Diana Degette: {degette_percentage:.3f}% ({degette})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {doane_percentage:.3f}% ({doane})")
    file.write("\n")
    file.write("________________")
    file.write("\n")
    file.write(f"Winner: {winner}")
