# CS4102 Fall 2019 -- Homework 10A 
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 4 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the comment
# at the top of your java or python file. Do not seek published or online
# solutions for any assignments. If you use any published or online resources
# (which may not include solutions) when completing this assignment, be sure
# to cite them. Do not submit a solution that you are unable to explain orally
# to a member of the course staff. Please remember that you are not allowed to
# share any written notes or documents (these include but are not limited to
# Overleaf documents, LaTeX source code, homework PDFs, group discussion
# notes, etc.). Any solutions that share similar text/code will be considered
# in breach of this policy. Please refer to the syllabus for a complete
# description of the collaboration policy.
#################################
# Your Computing ID: cnw2bx
# Collaborators: 
# Sources: Introduction to Algorithms, Cormen
#################################

class Millionaire:
    def __init__(self):
        return

    # This method should take in a list of the prize values (non-negative
    # integers) for each door and return the maximum amount of prize money you
    # can win by selecting a subset of doors, subject to the restriction that
    # you cannot select any adjacent pair of doors.
    #
    # @return the maximum amount of prize money
    def compute(self, doors):
        n = len(doors)

        if len(doors) == 0:
            return 0

        elif len(doors) == 1:
            return doors[0]

        else:
            return max(self.compute(doors[0:n-1]), self.compute(doors[0:n-2]) + doors[n-1])
