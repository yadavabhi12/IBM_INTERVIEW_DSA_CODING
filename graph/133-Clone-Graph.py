"""
===============================================================================
LeetCode 133 - Clone Graph
===============================================================================

PROBLEM
-------
Given a reference of a node in a connected undirected graph, return a deep
copy (clone) of the graph.

Each node contains:

    val
    neighbors


Example:

        1
       / \
      2---4
       \ /
        3

We need to create completely NEW nodes:

Original Graph              Cloned Graph

   1                           1'
  / \                         /  \
 2---4                       2'---4'
  \ /                         \ /
   3                           3'


Important:

1' is NOT the same object as 1.

We need a DEEP COPY.


===============================================================================
MOST IMPORTANT CONFUSION
===============================================================================

Suppose:

node = original node 1

We create:

clone = Node(1)


But node 1 may have neighbors:

2, 4


So clone 1 must have:

clone 2
clone 4


Therefore while cloning a node,
we also have to clone its neighbors.


But neighbors may point back to nodes we have already cloned.


Example:

1 <----> 2


If we clone 1:

clone 1

then clone 2.

But clone 2 has neighbor 1.


Should we clone 1 AGAIN?

NO.


This is why we need a HASHMAP.


===============================================================================
HASHMAP
===============================================================================

original node  →  cloned node


Example:

original       clone

   1      →      1'
   2      →      2'
   3      →      3'
   4      →      4'


Python:

visited = {
    original_node: cloned_node
}


===============================================================================
WHY DO WE NEED THE MAP?
===============================================================================

There are TWO reasons.


1. Avoid infinite recursion.

Graph:

1 → 2 → 1 → 2 → 1 ...


Without visited/map:

DFS would continue forever.


2. Reuse the SAME cloned object.

If original node 1 is connected to nodes 2 and 3,
and both 2 and 3 point to 1,

both cloned nodes must point to:

SAME 1'


NOT:

2' → 1a
3' → 1b


It must be:

2' ──┐
     ↓
    1'
     ↑
     └── 3'


Therefore:

original node → exactly one clone.


===============================================================================
APPROACH 1 - DFS + HASHMAP ⭐⭐⭐
===============================================================================
"""

class Solution:

    def cloneGraph(self, node):

        if not node:
            return None

        visited = {}


        def dfs(node):

            # ----------------------------------------------------------
            # If already cloned, return the existing clone.
            # ----------------------------------------------------------

            if node in visited:
                return visited[node]


            # ----------------------------------------------------------
            # Create clone
            # ----------------------------------------------------------

            clone = Node(node.val)

            # IMPORTANT:
            # Put clone into map BEFORE cloning neighbors.
            visited[node] = clone


            # ----------------------------------------------------------
            # Clone all neighbors
            # ----------------------------------------------------------

            for neighbor in node.neighbors:

                clone.neighbors.append(
                    dfs(neighbor)
                )


            return clone


        return dfs(node)


"""
===============================================================================
WHY MAP INSERTION MUST HAPPEN BEFORE NEIGHBORS?
===============================================================================

This is VERY important for interviews.


Suppose graph:

1 ↔ 2


Start:

dfs(1)


Create:

1'


Put immediately:

visited[1] = 1'


Now clone neighbor 2:

dfs(2)


Create:

2'


Put:

visited[2] = 2'


Now clone neighbor 1:

dfs(1)


We check:

1 in visited?


YES.


Return:

1'


So recursion stops.


If we didn't put 1 into visited before processing neighbors,
we would get:

1
 ↓
2
 ↓
1
 ↓
2
 ↓
...


INFINITE RECURSION.


===============================================================================
COMPLETE DRY RUN
===============================================================================

Graph:

        1
       / \
      2   4
       \ /
        3


Start:

dfs(1)


--------------------------------------------------

Create clone:

1'


visited:

{
    1 : 1'
}


--------------------------------------------------

Neighbor = 2


dfs(2)


Create:

2'


visited:

{
    1 : 1',
    2 : 2'
}


--------------------------------------------------

Suppose 2's neighbor = 3


dfs(3)


Create:

3'


visited:

{
    1 : 1',
    2 : 2',
    3 : 3'
}


--------------------------------------------------

3's neighbor = 4


dfs(4)


Create:

4'


visited:

{
    1 : 1',
    2 : 2',
    3 : 3',
    4 : 4'
}


--------------------------------------------------

4's neighbor = 1


dfs(1)


But:

1 already exists in visited.


Return:

1'


No new node created.


--------------------------------------------------

Eventually:

1' neighbors:

2'
4'


2' neighbors:

1'
3'


3' neighbors:

2'
4'


4' neighbors:

1'
3'


Graph completely cloned.


===============================================================================
THE RECURSION FLOW
===============================================================================

                dfs(1)
                  |
               create 1'
                  |
             clone neighbors
              /          \
          dfs(2)        dfs(4)
             |              |
           create 2'      create 4'
             |              |
          neighbors       neighbors
             |
          dfs(1)
             |
       already cloned
             |
          return 1'


This:

"already cloned → return existing clone"

is the heart of the problem.


===============================================================================
APPROACH 2 - BFS + HASHMAP ⭐⭐⭐
===============================================================================

We can also solve this iteratively using BFS.


Idea:

1. Create clone of starting node.
2. Put original → clone in map.
3. Push original node into queue.
4. Process every node.
5. For every neighbor:
       if not cloned:
           create clone
           add to queue
6. Connect clone's neighbor.


===============================================================================
CODE
===============================================================================
"""

from collections import deque


class Solution:

    def cloneGraph(self, node):

        if not node:
            return None

        visited = {
            node: Node(node.val)
        }

        queue = deque([node])


        while queue:

            current = queue.popleft()

            for neighbor in current.neighbors:

                # --------------------------------------------------
                # Neighbor not cloned yet
                # --------------------------------------------------

                if neighbor not in visited:

                    visited[neighbor] = Node(neighbor.val)

                    queue.append(neighbor)


                # --------------------------------------------------
                # Connect cloned nodes
                # --------------------------------------------------

                visited[current].neighbors.append(
                    visited[neighbor]
                )


        return visited[node]


"""
===============================================================================
BFS DRY RUN
===============================================================================

Graph: showing connections

1 -- 2
|    |
4 -- 3   


Initially:

visited:

1 → 1'


queue:

[1]


--------------------------------------------------

Pop 1.


Neighbors:

2, 4


Clone them:

2 → 2'
4 → 4'


queue:

[2,4]


Connect:

1' → 2'
1' → 4'


--------------------------------------------------

Pop 2.


Neighbor:

3


Create:

3 → 3'


queue:

[4,3]


Connect:

2' → 3'


--------------------------------------------------

Pop 4.


Neighbor 3 already cloned.


Connect:

4' → 3'


--------------------------------------------------

Pop 3.


Neighbors already cloned.


Connect accordingly.


Done.


===============================================================================
DFS vs BFS
===============================================================================

DFS:

    recursion
       ↓
    HashMap
       ↓
    clone


BFS:

    queue
       ↓
    HashMap
       ↓
    clone


Both are correct.


===============================================================================
TIME COMPLEXITY
===============================================================================

Let:

V = number of vertices
E = number of edges


Every node is processed once.

Every edge is examined once from each endpoint
in an undirected graph.


Therefore:

Time:

O(V + E)


HashMap operations are O(1) average.


===============================================================================
SPACE COMPLEXITY
===============================================================================

HashMap stores every node:

O(V)


DFS recursion:

O(V) worst case


Therefore auxiliary space:

O(V)


BFS queue:

O(V) worst case


Therefore:

DFS:

O(V) auxiliary


BFS:

O(V) auxiliary


Output itself also contains O(V + E) information,
but usually we don't count the returned cloned graph as
auxiliary space.


===============================================================================
WHY CAN'T WE JUST DO DFS WITHOUT HASHMAP?
===============================================================================

Because this is a GRAPH, not a normal TREE.


Tree:

        1
       / \
      2   3


No cycle.


Graph:

    1 ------ 2
    |        |
    |        |
    4 ------ 3


Cycles exist.


DFS without visited:

1 → 2 → 3 → 4 → 1 → 2 → 3 ...


Infinite.


Therefore graph traversal usually requires:

    visited


And for cloning:

    visited/map


===============================================================================
TREE VS GRAPH
===============================================================================

TREE:

Can often use:

    DFS
    BFS

without a visited set
because there is no cycle if traversed carefully.


GRAPH:

Usually need:

    visited


CLONE GRAPH:

Need:

    original → clone


This map acts as BOTH:

    visited information

and:

    clone lookup.


===============================================================================
VERY IMPORTANT INTERVIEW QUESTION
===============================================================================

Interviewer:

"Why do you use a dictionary instead of a set?"


Answer:


"Because I don't just need to know whether a node was visited.
I also need to retrieve the cloned object corresponding to that
original node. Therefore I maintain a mapping from original node
to its clone."


Excellent answer.


===============================================================================
ANOTHER INTERVIEW QUESTION
===============================================================================

"Why create the clone before recursively cloning neighbors?"


Answer:


"Because the graph can contain cycles. I first register the clone
in the hashmap, so if recursion encounters the same original node
again, it can immediately return the already-created clone."


===============================================================================
ANOTHER INTERVIEW QUESTION
===============================================================================

"Why can't you simply copy every node independently?"


Because relationships matter.


Suppose:

1 ↔ 2


If we independently create nodes,
we might accidentally create:

1' → 2a
2' → 1b


But correct deep copy requires:

1' ↔ 2'


The same cloned object must be reused.


===============================================================================
COMMON MISTAKES
===============================================================================

❌ Mistake 1:

Putting node in visited AFTER processing neighbors.


This can cause infinite recursion.


Correct:

clone = Node(node.val)

visited[node] = clone

then process neighbors.


--------------------------------------------------

❌ Mistake 2:

Using only a set.


A set tells:

"Have I visited this node?"


But we need:

"Which clone belongs to this node?"


Therefore use dictionary.


--------------------------------------------------

❌ Mistake 3:

Returning the original node.


Wrong:

return node


We need a completely new graph.


--------------------------------------------------

❌ Mistake 4:

Creating a new clone every time.


Wrong:

if node already exists:

return Node(node.val)


This creates multiple clones of the same original node.


Correct:

return visited[node]


--------------------------------------------------

❌ Mistake 5:

Forgetting null input.


If:

node = None


return:

None


===============================================================================
ONE-LINE MEMORY TRICK
===============================================================================

CLONE GRAPH:


        ORIGINAL
           ↓
        CREATE CLONE
           ↓
        PUT IN MAP
           ↓
      CLONE NEIGHBORS
           ↓
        REUSE MAP


Remember:

        Original → Clone


===============================================================================
PATTERN
===============================================================================

This problem follows:

        GRAPH DFS/BFS
              +
          HASHMAP
              +
         DEEP COPY


Very useful pattern.


===============================================================================
FINAL CODE - INTERVIEW VERSION ⭐
===============================================================================
"""

class Solution:

    def cloneGraph(self, node):

        if not node:
            return None

        clones = {node: Node(node.val)}


        def dfs(curr):

            if curr not in clones:
                clones[curr] = Node(curr.val)


            for neighbor in curr.neighbors:

                if neighbor not in clones:

                    clones[neighbor] = Node(neighbor.val)

                    dfs(neighbor)


                clones[curr].neighbors.append(
                    clones[neighbor]
                )


            return clones[curr]


        return dfs(node)


"""
===============================================================================
RECOMMENDED CLEAN VERSION
===============================================================================

For an interview, I recommend this version because it is simpler:

"""

class Solution:

    def cloneGraph(self, node):

        if not node:
            return None

        visited = {}


        def dfs(node):

            if node in visited:
                return visited[node]


            clone = Node(node.val)

            visited[node] = clone


            for neighbor in node.neighbors:

                clone.neighbors.append(
                    dfs(neighbor)
                )


            return clone


        return dfs(node)


"""
===============================================================================
30-SECOND REVISION
===============================================================================

Question:

Clone a graph.


Think:

        Graph
          ↓
        Cycle?
          ↓
        YES
          ↓
       HashMap
          ↓
Original → Clone


DFS:

if node in map:
    return map[node]

clone = Node(node.val)

map[node] = clone

for neighbor:
    clone.neighbors.append(
        dfs(neighbor)
    )

return clone


Complexity:

Time  = O(V + E)
Space = O(V)


===============================================================================
MOST IMPORTANT LINE
===============================================================================

visited[node] = clone


This line MUST happen:

BEFORE:

for neighbor in node.neighbors


because graphs can contain cycles.


===============================================================================
FINAL INTERVIEW STATEMENT
===============================================================================

"I'll use DFS with a hashmap that maps every original node to its
cloned node. Whenever I encounter a node that has already been
cloned, I return the existing clone. I register the clone before
processing its neighbors to safely handle cycles. Each vertex and
edge is processed once, giving O(V + E) time and O(V) auxiliary
space."


===============================================================================
"""