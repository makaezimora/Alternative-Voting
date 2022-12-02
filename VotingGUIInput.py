# import tkinter as tk
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def getInput():
    if request.method == 'POST':
        IRONMANrank = request.form.get['ironVote']
        # request.form.get('input Name')
        print(IRONMANrank)
        SHEHULKrank = request.form.get('hulkVote')
        HAWKGIRLrank = request.form.get('hawkVote')
        BLACKPANTHERrank = request.form.get('pantherVote')
        GREENLANTERNrank = request.form.get('lanternVote')
        STORMrank = request.form.get('stormVote')
        CATWOMANrank = request.form.get('catwomanVote')
        CAPTAINMARVELrank = request.form.get('marvelVote')
        WONDERWOMANrank = request.form.get('wonderVote')
        CAPTAINAMERICArank = request.form.get('americaVote')
        SUPERMANrank = request.form.get('supermanVote')
        BATMANrank = request.form.get('batmanVote')
        global g
        g = ['Voter You',int(BATMANrank),int(SUPERMANrank),int(CAPTAINAMERICArank),int(WONDERWOMANrank),
            int(CAPTAINMARVELrank),int(CATWOMANrank),int(STORMrank),int(GREENLANTERNrank),int(BLACKPANTHERrank),
            int(HAWKGIRLrank),int(SHEHULKrank),int(IRONMANrank)]
        global guess
        guess = request.form.get('dropdown')
        if request.form['submitButton'] == 'BORDA':
            borda()
        elif request.form['submitButton'] == 'PLURALITY':
            plurality()
        elif request.form['submitButton'] == 'APPROVAL':
            approval()
        elif request.form['submitButton'] == 'CONDORCET':
            condorcet()
    if request.method == 'GET':
        return render_template('index.html')
    #     return render_template('index.html', form=form)
        # use this section to send data about winner, the text, imgs, etc from each voting method function

def plurality(g):
    # creates an empty list to store the csv information, essentially a list of lists
    csv = []
    # accessing the csv file and reading it line by line to append them into the csv list
    for l in open("CSV.csv", 'r').readlines():
        # adds each line to the csv and removes any unnecessary trailing newline characters from the end of the string
        csv.append(l.strip("\n"))
        # csv.append(l)
    # create a new string
    # map changes each element in n into a string and list creates a list
    g = g
    g = list(map(str, g))
    # concatenates and separates the string with commas
    g = ','.join(g)
    # replace the last element in the list of contents with a new string
    csv[-1] = g
    # write into the csv file
    with open('CSV.csv', 'w') as f:
        for t in csv:
            f.write(t + '\n')
    # trying to append a new row to the end of csv same formatting as the other votes
    # create an empty dictionary to later populate the dictionary below
    data = {}
    # creates a separated list of headers for the candidates without the word "Response"
    headers = csv[0].split(",")[1:]
    # looping through, filling up the dictionary based off of the csv list
    for i in range(1, len(csv)):
        # tokens are the rows of responses and ranks in the csv sheet, separate each response up by the list's commas
        tokens = csv[i].split(",")
        # indexes the first column that holds each voters individual voterIDs
        voteID = tokens[0]
        # indexes the second column and the rest of them that hold the ranks or "votes"
        votes = tokens[1:]
        # creates an empty dictionary out of the voteID data to directly easily access the votes
        data[voteID] = {}
        # loops through the votes
        for j in range(len(votes)):
            # if there is a rank cast, meaning the rank isn't empty or equal to ''
            if len(votes[j]) > 0:
                # then the votes are assigned and converted into integers (which is needed for voting calculations)
                data[voteID][headers[j]] = int(votes[j])
    # creating a dictionary for each candidate with their assigned values
    candidates = {c: 0 for c in headers}
    # going over each voter id and their candidates
    for voter in data.keys():
        for candidate in data[voter].keys():
            if data[voter][candidate] != 1:
                # ensures that the code will loop through all the ranks and won't stop when the value isn't 1
                continue
            else:
                # incrementing the value of the candidate, in the key, value pair if their ranking is 1
                candidates[candidate] += 1
    # finds the candidate whose second element,x[1](their score) is larger than all of the others' second elements
    itemMaxValue = max(candidates.items(), key=lambda x: x[1])
    # creates an empty list to store all the ties
    listOfTies = list()
    # loops over each key, value pair, meaning each candidate and their score
    for key, value in candidates.items():
        # if their score is equal to the max score
        if value == itemMaxValue[1]:
            # add the candidate's name to the list
            listOfTies.append(key)
    # loop that prints out each candidate, or winner in the list of ties
    CutlistofTies = str(listOfTies)[1:-1]
    for j in listOfTies:
        single = 'With ' + str(itemMaxValue[1]) + ' votes...' + 'the plurality winner is ' + str(j)
        tie = 'With ' + str(itemMaxValue[1]) + ' votes...' + CutlistofTies + ' have tied'
    if len(listOfTies) <= 1:
        request.post(text=single)
        if str(j) == 'IRON MAN':
            WINimage = "Image files/ironman.jpg"
            request.post(electionWinner=WINimage)
        elif str(j) == 'BATMAN':
            WINimage = "Image files/batman.jpg"
            request.post(electionWinner=WINimage)
        elif str(j) == 'SUPERMAN':
            WINimage = "Image files/superman.jpg"
            request.post(electionWinner=WINimage)
        elif str(j) == 'CAPTAIN AMERICA':
            WINimage = "Image files/captain america.jpg"
            request.post(electionWinner=WINimage)
        elif str(j) == 'WONDER WOMAN':
            WINimage = "Image files/wonder woman.png"
            request.post(electionWinner=WINimage)
        elif str(j) == 'CAPTAIN MARVEL':
            WINimage = "Image files/captain marvel.jpg"
            request.post(electionWinner=WINimage)
        elif str(j) == 'CATWOMAN':
            WINimage = "Image files/catwoman.png"
            request.post(electionWinner=WINimage)
        elif str(j) == 'STORM':
            WINimage = "Image files/storm.jpg"
            request.post(electionWinner=WINimage)
        elif str(j) == 'GREEN LANTERN':
            WINimage = "Image files/green lantern.jpg"
            request.post(electionWinner=WINimage)
        elif str(j) == 'BLACK PANTHER':
            WINimage = "Image files/black panther.jpg"
            request.post(electionWinner=WINimage)
        elif str(j) == 'HAWK GIRL':
            WINimage = "Image files/hawkgirl.jpg"
            request.post(electionWinner=WINimage)
        elif str(j) == 'SHE-HULK':
            WINimage = "Image files/she hulk.jpg"
            request.post(electionWinner=WINimage)
        elif str(j) == 'IRON MAN':
            WINimage = "Image files/ironman.jpg"
            request.post(electionWinner=WINimage)
    else:
        request.post(text=tie)
        tiedimage = "Image files/Draw-Logo.png"
        request.post(electionWinner=tiedimage)

    def YesorNo(guess):
        yes = False
        for p in listOfTies:
            if p == guess:
                yes = True
        if yes == True:
            yesnoimg = 'Image files/YesEmoji-Correct.png'
        else:
            yesnoimg = 'Image files/NoEmoji-Incorrect.png'
    YesorNo()

def borda(g):
    # creates an empty list to store the csv information, essentially a list of lists
    csv = []
    # accessing the csv file and reading it line by line to append them into the csv list
    for l in open("CSV.csv", 'r').readlines():
        # adds each line to the csv and removes any unnecessary trailing newline characters from the end of the string
        csv.append(l.strip("\n"))
    # create an empty dictionary to later populate the dictionary below
    g = g
    g = list(map(str, g))
    # concatenates and separates the string with commas
    g = ','.join(g)
    # replace the last element in the list of contents with a new string
    csv[-1] = g
    # write into the csv file
    with open('CSV.csv', 'w') as f:
        for t in csv:
            f.write(t + '\n')
    # trying to append a new row to the end of csv same formatting as the other votes
    data = {}
    # creates a separated list of headers for the candidates without the word "Response"
    headers = csv[0].split(",")[1:]
    # looping through, filling up the dictionary based off of the csv list
    for i in range(1, len(csv)):
        # tokens are the rows of responses and ranks in the csv sheet, separate each response up by the list's commas
        tokens = csv[i].split(",")
        # indexes the first column that holds each voters individual voterIDs
        voteID = tokens[0]
        # indexes the second column and the rest of them that hold the ranks or "votes"
        votes = tokens[1:]
        # creates an empty dictionary out of the voteID data to directly easily access the votes
        data[voteID] = {}
        # loops through the votes
        for j in range(len(votes)):
            # if there is a rank cast, meaning the rank isn't empty or equal to ''
            if len(votes[j]) > 0:
                # then the votes are assigned and converted into integers (which is needed for voting calculations)
                data[voteID][headers[j]] = int(votes[j])
    # creating a dictionary for each candidate with their assigned values
    candidates = {c: 0 for c in headers}
    # the total of the highest and lowest rank (12, 1)
    hiLoTotal = 13
    # iterates through each voter and the candidate values
    for voter in data.keys():
        for candidate in data[voter].keys():
            # outlines the numerical relationship between the rank assigned and the amount of points given
            # gives the candidate the points for each of their ranks
            candidates[candidate] += hiLoTotal - data[voter][candidate]

    # finds the candidate whose second element,x[1](their score) is larger than all of the others' second elements
    itemMaxValue = max(candidates.items(), key=lambda x: x[1])
    # creates an empty list to store all the ties
    listOfTies = list()
    # loops over each key, value pair, meaning each candidate and their score
    for key, value in candidates.items():
        # if their score is equal to the max score
        if value == itemMaxValue[1]:
            # add the candidate's name to the list
            listOfTies.append(key)
    # loop that prints out each candidate, or winner in the list of ties
    CutlistofTies = str(listOfTies)[1:-1]
    for j in listOfTies:
        single = 'With ' + str(itemMaxValue[1]) + ' votes...' + 'the plurality winner is ' + str(j)
        tie = 'With ' + str(itemMaxValue[1]) + ' votes...' + CutlistofTies + ' have tied'
    if len(listOfTies) <= 1:
        request.post(text=single)
        if str(j) == 'IRON MAN':
            WINimage = "Image files/ironman.jpg"
            request.post(electionWinner=WINimage)
        elif str(j) == 'BATMAN':
            WINimage = "Image files/batman.jpg"
            request.post(electionWinner=WINimage)
        elif str(j) == 'SUPERMAN':
            WINimage = "Image files/superman.jpg"
            request.post(electionWinner=WINimage)
        elif str(j) == 'CAPTAIN AMERICA':
            WINimage = "Image files/captain america.jpg"
            request.post(electionWinner=WINimage)
        elif str(j) == 'WONDER WOMAN':
            WINimage = "Image files/wonder woman.png"
            request.post(electionWinner=WINimage)
        elif str(j) == 'CAPTAIN MARVEL':
            WINimage = "Image files/captain marvel.jpg"
            request.post(electionWinner=WINimage)
        elif str(j) == 'CATWOMAN':
            WINimage = "Image files/catwoman.png"
            request.post(electionWinner=WINimage)
        elif str(j) == 'STORM':
            WINimage = "Image files/storm.jpg"
            request.post(electionWinner=WINimage)
        elif str(j) == 'GREEN LANTERN':
            WINimage = "Image files/green lantern.jpg"
            request.post(electionWinner=WINimage)
        elif str(j) == 'BLACK PANTHER':
            WINimage = "Image files/black panther.jpg"
            request.post(electionWinner=WINimage)
        elif str(j) == 'HAWK GIRL':
            WINimage = "Image files/hawkgirl.jpg"
            request.post(electionWinner=WINimage)
        elif str(j) == 'SHE-HULK':
            WINimage = "Image files/she hulk.jpg"
            request.post(electionWinner=WINimage)
        elif str(j) == 'IRON MAN':
            WINimage = "Image files/ironman.jpg"
            request.post(electionWinner=WINimage)
    else:
        request.post(text=tie)
        tiedimage = "Image files/Draw-Logo.png"
        request.post(electionWinner=tiedimage)

    def YesorNo():
        yes = False
        for p in listOfTies:
            if p == guess:
                yes = True
        if yes == True:
            yesnoimg = 'Image files/YesEmoji-Correct.png'
        else:
            yesnoimg = 'Image files/NoEmoji-Incorrect.png'
    YesorNo()

def condorcet(g):
    # creates an empty list to store the csv information, essentially a list of lists
    csv = []
    # accessing the csv file and reading it line by line to append them into the csv list
    for l in open("CSV.csv", 'r').readlines():
        # adds each line to the csv and removes any unnecessary trailing newline characters from the end of the string
        csv.append(l.strip("\n"))
    # create an empty dictionary to later populate the dictionary below
    g = g
    g = list(map(str, g))
    # concatenates and separates the string with commas
    g = ','.join(g)
    # replace the last element in the list of contents with a new string
    csv[-1] = g
    # write into the csv file
    with open('CSV.csv', 'w') as f:
        for t in csv:
            f.write(t + '\n')
    data = {}
    # creates a separated list of headers for the candidates without the word "Response"
    headers = csv[0].split(",")[1:]
    # looping through, filling up the dictionary based off of the csv list
    for i in range(1, len(csv)):
        # tokens are the rows of responses and ranks in the csv sheet, separate each response up by the list's commas
        tokens = csv[i].split(",")
        # indexes the first column that holds each voters individual voterIDs
        voteID = tokens[0]
        # indexes the second column and the rest of them that hold the ranks or "votes"
        votes = tokens[1:]
        # creates an empty dictionary out of the voteID data to directly easily access the votes
        data[voteID] = {}
        # loops through the votes
        for j in range(len(votes)):
            # if there is a rank cast, meaning the rank isn't empty or equal to ''
            if len(votes[j]) > 0:
                # then the votes are assigned and converted into integers (which is needed for voting calculations)
                data[voteID][headers[j]] = int(votes[j])
            # since we need to compare all the values, including the empty ones
            else:
                # we add them to the dataset and assign them with the integer 0
                data[voteID][headers[j]] = 0
    # creating a dictionary for each candidate with their assigned values
    candidates = {c: 0 for c in headers}
    # gives a dictionary of the pair-wise comparisons of the candidates and the wins of each pair
    cad = {}
    # creates a new dictionary for the final scores with each candidate name and a starting score of 0
    final = {x: 0 for x in headers}
    # iterates through each voter in the data
    for voter in data.keys():
        # iterates through each candidate through the data dictionary keys
        for candidate in data[voter].keys():
            # creates a differently referenced, but identical iteration that iterates each candidate with the headers
            for name in headers:
                # compares two different candidates if they haven't been added to the cad dict yet
                if candidate != name and (candidate, name) not in cad:
                    # adds the pair to the cad dictionary and gives them a starting score of 0
                    cad[(candidate, name)] = 0
                if candidate != name and data[voter][candidate] < data[voter][name]:
                    # if the candidate is ranked higher than the name (other candidate), then the first one gets a point
                    # the first one in the pair, the candidate, is the one who the points correspond to
                    cad[(candidate, name)] += 1
    # creates a dictionary for results that aggregate the candidate wins for the pairwise dictionaries
    results = {x: 0 for x in headers}
    # iterates through all of the pairs
    for candidate, name in cad.keys():
        # the first value in the pair corresponds with the score
        # this if and elif statement compare the scores of the pairs and whoever has the greatest score, gets 1 victory
        if candidate != name and cad[(candidate, name)] > cad[(name, candidate)]:
            results[candidate] += 1
        elif candidate != name and cad[(candidate, name)] < cad[(name, candidate)]:
            results[name] += 1
    for key in results:
        # since each pair was compared twice, we divide the results by two to get the correct number of victories
        results[key] = results[key] / 2
    # finds the candidate with the maximum value and assigns that value to a variable for easy printing
    max_key = max(results, key=results.get)
    text = 'The condorcet winner is ' + str(max_key) + ' with....' + str(int(results[max_key])) + ' victories'
    request.post(text=text)
    if str(max_key) == 'IRON MAN':
        WINimage = "Image files/ironman.jpg"
        request.post(electionWinner=WINimage)
    elif str(max_key) == 'BATMAN':
        WINimage = "Image files/batman.jpg"
        request.post(electionWinner=WINimage)
    elif str(max_key) == 'SUPERMAN':
        WINimage = "Image files/superman.jpg"
        request.post(electionWinner=WINimage)
    elif str(max_key) == 'CAPTAIN AMERICA':
        WINimage = "Image files/captain america.jpg"
        request.post(electionWinner=WINimage)
    elif str(max_key) == 'WONDER WOMAN':
        WINimage = "Image files/wonder woman.png"
        request.post(electionWinner=WINimage)
    elif str(max_key) == 'CAPTAIN MARVEL':
        WINimage = "Image files/captain marvel.jpg"
        request.post(electionWinner=WINimage)
    elif str(max_key) == 'CATWOMAN':
        WINimage = "Image files/catwoman.png"
        request.post(electionWinner=WINimage)
    elif str(max_key) == 'STORM':
        WINimage = "Image files/storm.jpg"
        request.post(electionWinner=WINimage)
    elif str(max_key) == 'GREEN LANTERN':
        WINimage = "Image files/green lantern.jpg"
        request.post(electionWinner=WINimage)
    elif str(max_key) == 'BLACK PANTHER':
        WINimage = "Image files/black panther.jpg"
        request.post(electionWinner=WINimage)
    elif str(max_key) == 'HAWK GIRL':
        WINimage = "Image files/hawkgirl.jpg"
        request.post(electionWinner=WINimage)
    elif str(max_key) == 'SHE-HULK':
        WINimage = "Image files/she hulk.jpg"
        request.post(electionWinner=WINimage)
    def YesorNo(guess):
        yes = False
        if str(max_key) == guess:
            yes = True
        if yes == True:
            yesnoimg = 'Image files/YesEmoji-Correct.png'
        else:
            yesnoimg = 'Image files/NoEmoji-Incorrect.png'
    YesorNo()

def approval(g):
    # creates an empty list to store the csv information, essentially a list of lists
    csv = []
    # accessing the csv file and reading it line by line to append them into the csv list
    for l in open("CSV.csv", 'r').readlines():
        # adds each line to the csv and removes any unnecessary trailing newline characters from the end of the string
        csv.append(l.strip("\n"))
    # create an empty dictionary to later populate the dictionary below
    g = g
    g = list(map(str, g))
    # concatenates and separates the string with commas
    g = ','.join(g)
    # replace the last element in the list of contents with a new string
    csv[-1] = g
    # write into the csv file
    with open('CSV.csv', 'w') as f:
        for t in csv:
            f.write(t + '\n')
    data = {}
    # creates a separated list of headers for the candidates without the word "Response"
    headers = csv[0].split(",")[1:]
    # looping through, filling up the dictionary based off of the csv list
    for i in range(1, len(csv)):
        # tokens are the rows of responses and ranks in the csv sheet, separate each response up by the list's commas
        tokens = csv[i].split(",")
        # indexes the first column that holds each voters individual voterIDs
        voteID = tokens[0]
        # indexes the second column and the rest of them that hold the ranks or "votes"
        votes = tokens[1:]
        # creates an empty dictionary out of the voteID data to directly easily access the votes
        data[voteID] = {}
        # loops through the votes
        for j in range(len(votes)):
            # if there is a rank cast, meaning the rank isn't empty or equal to ''
            if len(votes[j]) > 0:
                # then the votes are assigned and converted into integers (which is needed for voting calculations)
                data[voteID][headers[j]] = int(votes[j])
            # since we need to compare all the values, including the empty ones
            else:
                # we add them to the dataset and assign them with the integer 0
                data[voteID][headers[j]] = 0
    # creating a dictionary for each candidate with their assigned values
    candidates = {c: 0 for c in headers}

    for voter in data.keys():
        total, counter = 0, 0
        for candidate in data[voter].keys():
            if data[voter][candidate] != 0:
                # for each row, calculates the total sum of ranks
                total += data[voter][candidate]
                # for each row, counts the number of ranks
                counter += 1
        if counter == 0:
            continue
        else:
            # calculates the average we'll use to assign the top rankers/ point getters
            average = total / counter
        for candidate in data[voter].keys():
            # if the rank is not equal to zero
            if data[voter][candidate] != 0:
                # and if the rank is "top ranked", meaning less than the average, or if the average is equal to 1
                if data[voter][candidate] < average or average == 1:
                    # the candidate gets a point added to their score
                    candidates[candidate] += 1
    # finds the candidate with the maximum value and assigns that value to a variable for easy printing
    max_key = max(candidates, key=candidates.get)
    text = 'The approval winner is ' + str(max_key) + ' with....' + str(int(candidates[max_key])) + ' victories'
    request.post(text=text)
    if str(max_key) == 'IRON MAN':
        WINimage = "Image files/ironman.jpg"
        request.post(electionWinner=WINimage)
    elif str(max_key) == 'BATMAN':
        WINimage = "Image files/batman.jpg"
        request.post(electionWinner=WINimage)
    elif str(max_key) == 'SUPERMAN':
        WINimage = "Image files/superman.jpg"
        request.post(electionWinner=WINimage)
    elif str(max_key) == 'CAPTAIN AMERICA':
        WINimage = "Image files/captain america.jpg"
        request.post(electionWinner=WINimage)
    elif str(max_key) == 'WONDER WOMAN':
        WINimage = "Image files/wonder woman.png"
        request.post(electionWinner=WINimage)
    elif str(max_key) == 'CAPTAIN MARVEL':
        WINimage = "Image files/captain marvel.jpg"
        request.post(electionWinner=WINimage)
    elif str(max_key) == 'CATWOMAN':
        WINimage = "Image files/catwoman.png"
        request.post(electionWinner=WINimage)
    elif str(max_key) == 'STORM':
        WINimage = "Image files/storm.jpg"
        request.post(electionWinner=WINimage)
    elif str(max_key) == 'GREEN LANTERN':
        WINimage = "Image files/green lantern.jpg"
        request.post(electionWinner=WINimage)
    elif str(max_key) == 'BLACK PANTHER':
        WINimage = "Image files/black panther.jpg"
        request.post(electionWinner=WINimage)
    elif str(max_key) == 'HAWK GIRL':
        WINimage = "Image files/hawkgirl.jpg"
        request.post(electionWinner=WINimage)
    elif str(max_key) == 'SHE-HULK':
        WINimage = "Image files/she hulk.jpg"
        request.post(electionWinner=WINimage)
    def YesorNo(guess):
        yes = False
        if str(max_key) == guess:
            yes = True
        if yes == True:
            yesnoimg = 'Image files/YesEmoji-Correct.png'
        else:
            yesnoimg = 'Image files/NoEmoji-Incorrect.png'
    YesorNo()

if __name__ == "__main__":
    app.run()
    getInput()