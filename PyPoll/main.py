import csv


with open("./Resources/election_data.csv", newline="") as csvfile:
    with open("./Analysis/results.txt", 'w') as resultfile:
        rows = csv.reader(csvfile)
        castvotes = 0
        votesDict = {}
        winnervotes = 0
        winner = ""
        next(rows)
        for row in rows:
            castvotes+=1
            if row[2] not in votesDict.keys():
                votesDict[row[2]] = 1
            else:
                votesDict[row[2]] += 1
        print("\nElection Results\n----------------------------")
        resultfile.write("\nElection Results\n----------------------------\n")
        print(f"Total Votes: {castvotes}\n----------------------------")
        resultfile.write(f"Total Votes: {castvotes}\n----------------------------\n")
        for candidate in votesDict.keys():
            print("{}:  {:.3f}% ({})".format(candidate,float(votesDict[candidate])/castvotes*100,votesDict[candidate]))
            resultfile.write("{}:  {:.3f}% ({})\n".format(candidate,float(votesDict[candidate])/castvotes*100,votesDict[candidate]))
            if votesDict[candidate] > winnervotes:
                winnervotes = votesDict[candidate]
                winner = candidate
        print(f"----------------------------\nWinner: {winner}\n----------------------------")
        resultfile.write(f"----------------------------\nWinner: {winner}\n----------------------------\n")
