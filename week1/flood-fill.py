'''
Problem: Flood Fill
Link: https://leetcode.com/problems/flood-fill/
Language: Python
Written by: Anirudh Makhana
'''

##Important NOTE
'''
DFS (Depth-First Search):

Exploration Strategy: DFS explores as far as possible along a branch before backtracking. It uses a stack (which can be implemented using recursion) to remember which vertex to visit next.
Use Cases: DFS is typically used in scenarios like:
Finding connected components in a grid or graph.
Topological sorting.
Searching for solutions in games or puzzle problems where you might want to explore a decision as far as possible before backtracking (e.g., N-queens problem).
Advantages:
Can be simpler to implement using recursion.
Can provide a natural way to explore all possible decisions in decision-making problems.
BFS (Breadth-First Search):

Exploration Strategy: BFS explores all neighbors at the current depth before moving on to nodes at the next depth level. It uses a queue to remember which vertex to visit next.
Use Cases: BFS is often chosen in scenarios like:
Finding the shortest path in unweighted graphs or grids.
Level order traversal in trees.
Spreading processes like network broadcasting.
Advantages:
Guarantees the shortest path in unweighted graphs.
Can provide level-by-level exploration or processing.
'''

##We need to make use of dfs to solve this problem
##We will create a function to perform dfs
##We will check if the row and column are out of bounds or the color is not the source color
##If they are, we will return
##Else, we will update the color at the row and column
##We will perform dfs on the top, bottom, left and right neighbors

class Solution():
    def dfs(self, image, sr, sc, newColor, rows, cols, source):
        #Base condition:
        #Check if the row and column are out of bounds or the color is not the source color:
        if sr < 0 or sr >= rows or sc < 0 or sc >= cols or image[sr][sc] != source:
            return
        #Update the color at the row and column:
        image[sr][sc] = newColor
        #Perform dfs on the top, bottom, left and right neighbors:
        self.dfs(image, sr - 1, sc, newColor, rows, cols, source)
        self.dfs(image, sr + 1, sc, newColor, rows, cols, source)
        self.dfs(image, sr, sc - 1, newColor, rows, cols, source)
        self.dfs(image, sr, sc + 1, newColor, rows, cols, source)

    def floodFill(self, image, sr, sc, color) -> list[list[int]]:
        #Check if the image is empty:
        if len(image) == 0:
            #If it is, return the image:
            return image
        #Store the number of rows and columns:
        rows = len(image)
        cols = len(image[0])
        #Store the source color:
        source = image[sr][sc]
        #Check if the source color is equal to the new color:
        if source == color:
            #If it is, return the image:
            return image
        #Perform dfs:
        self.dfs(image, sr, sc, color, rows, cols, source)
        #Return the image:
        return image
