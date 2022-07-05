#PyPoll main.py

import os
import csv

GrabData = os.path.join(os.path.dirname(__file__), "./Resources/election_data.csv")
#GrabData = os.path.join("Resources","election_data.csv")
#GrabData = "C:/Users/MattM/Desktop/GaTech Boot Camp/assignments/Lesson 3/Python-challenge/PyPoll/Resources/election_data.csv"

#data_path=os.path.join('Resources', 'election_data.csv')
Outputfile_PyPoll = "C:/Users/MattM/Documents/GitHub/Module-03-Challenge/PyPoll/analysis/OutputFile_PyPoll.txt"

candidates = {}
sum = 0
maxVotes = 0
winner = ""

def formatPercent(amount):
    return "{:.3f}%".format(amount)

with open(GrabData, "r") as file:

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
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {sum}\n"
    "-------------------------\n"
]


for candidate in candidates:
    votes = candidates[candidate]
    maxVotes = max(maxVotes, votes)
    if maxVotes == votes:
        winner = candidate
    percent = (votes/sum)*100
    
    output.append(
        f"{candidate}: {formatPercent(percent)} ({votes})\n"
    
        )

output.append("-------------------------\n")
output.append(f"Winner: {winner}\n")
output.append("-------------------------\n")


print(output)

#Exporting output to a text file.
with open(Outputfile_PyPoll, "w") as textfile:
    textfile.write("".join(output))