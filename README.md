# Headless-Codeforces

Headless-Codeforces is a simple code that can gather information from the coding website https://codeforces.com without having to open the browser. All that is required is an
internet connection.

In the file headless-codeforces.py, there is a class CodeForces containing the methods getTopRated(), getTodaysProblems(), getLatestContest() and close().

getTopRated() extracts the list of top 10 registered individuals with the highest rating in Codeforces and saves/creates the list in a csv file called 'top_rated.csv'.

getTodaysProblems() retrieves the list of current problems posted on the problemset page of Codeforces and stores them in a file called 'todays_problem_set.csv'. It also contains
the id number and the difficulty level of each of the problems (if specified in the website).

getLatestContest() gives information on the nearest upcoming contest, its duration and begin date. It stores this information on 'upcoming_contest.txt'.

close() simply closes the headless browser. It's recommended to close the browser after retrieving information from https://codeforces.com.

All this has been implemented using selenium and csv modules in python.
