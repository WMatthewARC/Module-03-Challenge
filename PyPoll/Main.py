#PyPoll main.py

import os
import csv

filename = os.path.join(os.path.dirname(__file__), "./Resources/election_data.csv")

#data_path=os.path.join('Resources', 'election_data.csv')
#candidates_set = set()


outputfile_PyPoll= "C:/Users/MattM/Documents/GitHub/Module-03-Challenge/PyPoll/analysis"




candidates = {}
sum = 0
maxVotes = 0
winner = ""

def formatPercent(amount):
    return "{:.3f}%".format(amount)

with open(filename, "r") as file:

    reader = csv.DictReader(file)
    for row in reader:
        if not row["Candidate"] in candidates:
            candidates[row["Candidate"]] = 1
        else:
            candidates[row["Candidate"]] += 1
        #print(row["Ballot ID"], row["County"], row["Candidate"])
        sum += 1

    # write header and sum
output = [
    f"Analysis",
    "----------------",
    f"Total Votes: {sum}"
]
for candidate in candidates:
    votes = candidates[candidate]
    maxVotes = max(maxVotes, votes)
    if maxVotes == votes:
        winner = candidate
    percent = (votes/sum)*100
    
    output.append(f"{candidate}: {formatPercent(percent)} ({votes})")

    # write candidate, percent, total
    #print(f"{candidate}: {formatPercent(percent)} ({votes})")
#print(f"Winner {winner}")


print(output)


with open(outputfile_PyPoll, "w") as textfile:
    textfile.write(output)

