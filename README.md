# TOC_extra_credit

What was the extra work: 
The pcp_solver.py script solves multiple instances of the Post Correspondence Problem (PCP), where each test case consists of a set of tiles, each with a top and bottom string. The script reads an input file containing one or more test cases, where each test case is a set of top/bottom pairs separated by an empty line or a delimiter (---). For each test case, it uses Breadth-First Search (BFS) to explore all possible sequences of tiles and checks if the concatenated top and bottom strings from any sequence match, indicating a solution. If a solution is found, the script outputs the sequence of tile indices that forms the match; otherwise, it reports "No solution found." The script can handle multiple test cases in a single input file, processing each independently, and outputs the results for all test cases in sequence.


Why did you choose it (i.e. in what area did you feel deficient and how did this work help improve your understanding) You can point to specific homeworks or problem types on exams: 
After doing Problem 3 on HW 10A Individual, I realized that despite having a decent understanding of PCPs, I really had trouble identifying solutions to the puzzles. So, I thought creating a python script that could find multiple solutions to given instances would be helpful not only tomyself but to otheres that had trouble finding solutions to the puzzles by hand. Additionally, this Python script helped me improve my understanding of the Post Correspondence Problem (PCP) by providing a concrete implementation of a Breadth-First Search (BFS) algorithm to solve the problem. By breaking the problem into smaller, manageable steps—such as reading and parsing input, applying BFS to explore tile combinations, and checking for prefix compatibility between top and bottom strings—it gave me a clear view of how PCP can be approached algorithmically. The script visually demonstrated how tile sequences can be tested and combined to form a solution, helping me understand how string matching works in this context. It also allowed me to explore different test cases, including those with no solution, showing the challenges involved in solving PCPs and how constraints like prefix matching affect the search process. Overall, this code provided me with hands-on experience with PCP and helped me appreciate the role of search algorithms in solving complex combinatorial problems.

What files are what:
pcp_solver.py is the python script that contains the BFS to solve the PCPs
pcp_input.py is a sample input with different instances with different outputs to test the code (NOTE: I programmed this to take in a maximum of 10 tiles per instance so the sake of simplicity and efficiencey)
This code prints to stdout 

To run this code:
python3 pcp_solver.py pcp_input.txt 
