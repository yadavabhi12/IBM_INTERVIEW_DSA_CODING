class Solution:

    def findLadders(self, beginWord, endWord, wordList):

        wordSet = set(wordList)

        if endWord not in wordSet:
            return []

        from collections import defaultdict, deque

        parents = defaultdict(list)

        level = {beginWord: 0}

        q = deque([beginWord])

        found = False

        while q and not found:

            size = len(q)

            for _ in range(size):

                word = q.popleft()

                for i in range(len(word)):

                    for ch in "abcdefghijklmnopqrstuvwxyz":

                        newWord = word[:i] + ch + word[i+1:]

                        if newWord not in wordSet:
                            continue

                        if newWord not in level:

                            level[newWord] = level[word] + 1

                            q.append(newWord)

                            parents[newWord].append(word)

                        elif level[newWord] == level[word] + 1:

                            parents[newWord].append(word)

                        if newWord == endWord:
                            found = True

        ans = []

        path = [endWord]

        def dfs(word):

            if word == beginWord:

                ans.append(path[::-1])

                return

            for p in parents[word]:

                path.append(p)

                dfs(p)

                path.pop()

        if found:
            dfs(endWord)

        return ans





'''"""
===============================================================================
LeetCode 126 - Word Ladder II
===============================================================================

PROBLEM
-------
Given:

beginWord
endWord
wordList

Return ALL SHORTEST transformation sequences from beginWord to endWord.

Rules

1. Only ONE character can be changed at a time.

2. Every transformed word must exist in wordList.

3. Return ALL shortest paths.

If impossible

Return []


===============================================================================
EXAMPLE
===============================================================================

beginWord = "hit"

endWord = "cog"

wordList

["hot","dot","dog","lot","log","cog"]


Output

[
 ["hit","hot","dot","dog","cog"],
 ["hit","hot","lot","log","cog"]
]


===============================================================================
WHY NORMAL DFS FAILS?
===============================================================================

DFS explores deep paths first.

It may find

Long path

before

Shortest path.

Also

It cannot guarantee ALL shortest paths.


Hence

DFS alone is NOT suitable.


===============================================================================
WHY BFS?
===============================================================================

BFS explores

Level by Level.


Level

0

hit


↓

Level

1

hot


↓

Level

2

dot

lot


↓

Level

3

dog

log


↓

Level

4

cog


First time reaching

endWord

means

Shortest distance.


===============================================================================
BUT WHY BFS ALONE IS NOT ENOUGH?
===============================================================================

Question asks

ALL shortest paths.


Normal BFS gives only

Shortest Distance.


Need

All Parents

for reconstruction.


===============================================================================
MAIN IDEA
===============================================================================

Phase 1

BFS

↓

Find shortest distance.

↓

Store every possible parent.

↓

Phase 2

DFS / Backtracking

↓

Generate every shortest path.


===============================================================================
VISUALIZATION
===============================================================================

                 hit
                  |
                hot
              /     \
           dot       lot
            |         |
           dog       log
             \       /
               \   /
                cog


Notice

cog has TWO parents

dog

and

log


Therefore

There are TWO shortest paths.


===============================================================================
DATA STRUCTURES
===============================================================================

Queue

For BFS.


Dictionary

parents[word]

Stores ALL previous words.


Example

parents

{

hot : [hit]

dot : [hot]

lot : [hot]

dog : [dot]

log : [lot]

cog : [dog,log]

}


===============================================================================
PHASE 1
===============================================================================

BFS


Queue

hit


Visit

hot


parents

hot

↓

hit


Visit

dot


parents

dot

↓

hot


Visit

lot


parents

lot

↓

hot


Visit

dog


parents

dog

↓

dot


Visit

log


parents

log

↓

lot


Visit

cog


parents

cog

↓

dog

log


BFS Complete.


===============================================================================
PHASE 2
===============================================================================

Now build paths

BACKWARDS.


Start

cog


Parents

dog

log


dog

↓

dot

↓

hot

↓

hit


Reverse


hit

hot

dot

dog

cog


--------------------------------------


log

↓

lot

↓

hot

↓

hit


Reverse


hit

hot

lot

log

cog


===============================================================================
GRAPH
===============================================================================

hit

↓

hot

↙     ↘

dot     lot

↓         ↓

dog      log

 ↘       ↙

    cog


Every edge

represents

One Letter Change.


===============================================================================
ALGORITHM
===============================================================================

STEP 1

Convert wordList into HashSet.

↓

Fast lookup.

O(1)


----------------------------------------

STEP 2

Run BFS.

↓

Maintain

Queue

Visited

Parents Map

Distance


----------------------------------------

STEP 3

Whenever new word generated

Store

Current Word

as parent.


----------------------------------------

STEP 4

Stop BFS after shortest level reaches endWord.


----------------------------------------

STEP 5

DFS from endWord.

↓

Use parent map.

↓

Generate all shortest paths.


===============================================================================
CODE
===============================================================================

class Solution:

    def findLadders(self, beginWord, endWord, wordList):

        wordSet = set(wordList)

        if endWord not in wordSet:
            return []

        from collections import defaultdict, deque

        parents = defaultdict(list)

        level = {beginWord: 0}

        q = deque([beginWord])

        found = False

        while q and not found:

            size = len(q)

            for _ in range(size):

                word = q.popleft()

                for i in range(len(word)):

                    for ch in "abcdefghijklmnopqrstuvwxyz":

                        newWord = word[:i] + ch + word[i+1:]

                        if newWord not in wordSet:
                            continue

                        if newWord not in level:

                            level[newWord] = level[word] + 1

                            q.append(newWord)

                            parents[newWord].append(word)

                        elif level[newWord] == level[word] + 1:

                            parents[newWord].append(word)

                        if newWord == endWord:
                            found = True

        ans = []

        path = [endWord]

        def dfs(word):

            if word == beginWord:

                ans.append(path[::-1])

                return

            for p in parents[word]:

                path.append(p)

                dfs(p)

                path.pop()

        if found:
            dfs(endWord)

        return ans


===============================================================================
DRY RUN
===============================================================================

Queue

hit


↓

hot


↓

dot

lot


↓

dog

log


↓

cog


Parents


cog

↓

dog

log


DFS


cog

↓

dog

↓

dot

↓

hot

↓

hit


Reverse


hit

hot

dot

dog

cog


Second Path


cog

↓

log

↓

lot

↓

hot

↓

hit


Reverse


hit

hot

lot

log

cog


===============================================================================
TIME COMPLEXITY
===============================================================================

BFS

O(N × L × 26)

N

Number of words

L

Word Length


DFS

Depends on

Number of shortest paths.


===============================================================================
SPACE COMPLEXITY
===============================================================================

Queue

O(N)

Parents

O(N)

Visited

O(N)


Overall

O(N)


===============================================================================
COMMON MISTAKES
===============================================================================

❌ Using only DFS.

Cannot guarantee shortest path.

--------------------------------------

❌ Stopping immediately after finding endWord.

Need to finish CURRENT BFS LEVEL.

Otherwise some shortest parents are lost.

--------------------------------------

❌ Using single parent.

Need multiple parents.

Because multiple shortest paths exist.

--------------------------------------

❌ Marking visited too early.

Can lose another shortest parent from same level.

===============================================================================
INTERVIEW TRICK
===============================================================================

Word Ladder I (127)

Only shortest distance

↓

Pure BFS


Word Ladder II (126)

All shortest paths

↓

BFS

+

Parent Graph

+

DFS Backtracking


===============================================================================
MEMORY TRICK
===============================================================================

Graph

↓

BFS

↓

Parent Map

↓

Backtracking

↓

All Shortest Paths


===============================================================================
PATTERN
===============================================================================

Graph

↓

Shortest Path

↓

BFS

↓

Store Parents

↓

DFS Reconstruction

↓

All Shortest Paths

===============================================================================
"""'''