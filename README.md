# Alternative-Voting
By studying the computational aspects of different voting methods, I made a teaching tool that allows the user to learn about how their vote may affect a mock election through various ballot counting methods. To keep it fun, the candidates are Superheros like Iron Man or Black Panther.

In 2020 I was assigned this course project about modeling alternative voting methods with a given dataset. I'm taking the algorithm that I created in class, creating a simpler dataset, and translating it into an interesting interactive web app.

## Key Features

- Run an implementation of the chosen voting system and select a winner or declare a draw

- Inform the user of the results, including total votes and winner 

- Clickable button to run the specific voting method

- User can edit the dataset by inputing their vote for each superhero

- Fun animation of "The Flash" racing across the bottom screen

- User can predict the winner by chosing a hero from the dropdown and will be told if they are correct or incorrect

## Demo

I made a `tkinter` GUI version of this before trying to convert it to a Flask web app that could be hosted online.

###### Watch the demo video below :movie_camera:
[<img src="https://img.youtube.com/vi/uj06sldniCQ/maxresdefault.jpg" width="300">](https://youtu.be/uj06sldniCQ?t=204)

## Screenshots

![Website Screenshot](https://github.com/makaezimora/Alternative-Voting/blob/main/Website-Screenshot.png?raw=true)

## Roadmap

- Fix the "Internal Server" error when deploying with Flask

## About the Voting Methods

### Plurality Method: The candidate with the most first-place votes wins the election.
The simplest, and most familiar, is the Plurality Method. This is the conventional one person, one vote method we use today in most elections. In this case, the winner is the candidate that gets the most votes. 

How I implemented it: I gave a vote to only the top-ranked superhero in each survey entry (the one with a ranking of 1) and added up the totals.

### Borda Count Method: Each place on a preference ballot is assigned points. The candidate with the most points wins.

This method was developed by 18th century mathematician Jean-Charles de Borda and is used today to decide the MLB MVP of the year and the ranking of the NCAA college teams. In this method, the voter ranks each candidate numerically and the winner is decided by adding points given to each candidate according to their ranking. Last place receives one point, next to last place receives two points, and so on. Thus, if there are N candidates, then first-place receives N points. Now, multiply the point value for each place by the number of voters at the top of the column to find the points each candidate wins in a column. Lastly, total up all the points for each candidate. 

How I implemented it: You need to give points to each candidate in reverse proportion to their ranking based on the total number of options. This means a ranking of 1 gives that candidate 12 points. A ranking of 2 gives 11 points and so on. If a candidate is not ranked, they get zero points. The superhero with the most points wins.

### Condorcet Method: The candidate who would beat every other candidate in a head-to-head majority vote is the winner. 

This method was developed by the Marquis of Condorcet, Marie Jean Antoine Nicolas de Caritat. Condorcet was an 18th century French philosopher and mathematician and a rival of Borda. Today, Condorcet voting is used by the Wikimedia foundation and the Linux community for most internal elections. In Condorcet voting, the winner is decided by determining the candidate that would beat every other candidate in a hypothetical head-to-head match.

How I implemented it: You will need to use the rankings given in the survey to determine the winner by considering every possible pair of superheroes. For example, if Batman is paired against Superman you would have to count both the number of people who have ranked Batman better (that is, with a lower number) than Superman, and the number who have ranked Superman better than Batman. If Batman is preferred by more people then he is the winner of that pairing. You must repeat this procedure for every possible pairing. The superhero with the most victories is the winner. If there is no clear winner, the Condorcet method ends up in a draw.

### Approval Method: The voters decide whether they approve or disapprove of candidates in an election. The candidate with the most approval votes is the winner.

This method was developed by Cornell University mathematician Robert J. Weber in the 1970s. Today it is relatively uncommon outside of professional organizations, but the United Nations uses it to elect its Secretary General. In approval voting, voters simply give a binary vote (approve or disapprove, thumbs up or down, like or dislike) for as many candidates as they want. The winner is whichever candidate gets the most positive votes. 

How I implemented it: You must find the average ranking for each survey entry. Any ranking below the average would count as an approval and anything above would be a disapproval. For example, if a survey entry ranks four superheroes (rankings would be 1-4, and the average would be 2.5) the rankings 1 and 2 would be approvals while 3 and 4 would be disapproval. If you have an entry with five superheroes ranked (1-5, average 3) rankings 1 and 2 would be approvals, while rankings 4 and 5 would be disapproval.  Ranking 3 would not count at all.  After doing this operation for every survey entry, you count the total number of approvals, and the candidate with the highest number wins.

To go more into depth about voting paradoxes, how to compare voting methods, general voting theory, and other voting methods that weren’t covered, read up on these 
Sources: https://plato.stanford.edu/entries/voting-methods/#toc
https://www.princeton.edu/~cuff/voting/theory.html
https://www.coconino.edu/resources/files/pdfs/academics/arts-and-sciences/MAT142/Chapter_7_VotingSystems.pdf 
