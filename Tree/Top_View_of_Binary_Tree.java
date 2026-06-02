package Tree;
import java.util.*;

// Tree Node class
class TreeNode {

    int val;
    TreeNode left, right;

    TreeNode(int val) {
        this.val = val;
    }
}

// Pair class
// Stores node + horizontal distance
class Pair {

    TreeNode node;
    int hd;

    Pair(TreeNode node, int hd) {
        this.node = node;
        this.hd = hd;
    }
}

public class Top_View_of_Binary_Tree {

    public static List<Integer> topView(TreeNode root) {

        // Final answer list
        List<Integer> result = new ArrayList<>();

        // If tree is empty
        if (root == null)
            return result;

        // TreeMap:
        // key   = horizontal distance
        // value = first node seen
        TreeMap<Integer, Integer> map = new TreeMap<>();

        // Queue for BFS traversal
        Queue<Pair> queue = new LinkedList<>();

        // Root node HD = 0
        queue.offer(new Pair(root, 0));

        // BFS starts
        while (!queue.isEmpty()) {

            Pair current = queue.poll();

            TreeNode node = current.node;
            int hd = current.hd;

            // IMPORTANT:
            // Insert ONLY FIRST node for every HD
            // because top view wants top-most node
            if (!map.containsKey(hd)) {
                map.put(hd, node.val);
            }

            // Go left
            // HD decreases by 1
            if (node.left != null) {
                queue.offer(new Pair(node.left, hd - 1));
            }

            // Go right
            // HD increases by 1
            if (node.right != null) {
                queue.offer(new Pair(node.right, hd + 1));
            }
        }

        // Store answer from left to right
        for (int value : map.values()) {
            result.add(value);
        }

        return result;
    }

    public static void main(String[] args) {

        // Create tree

        TreeNode root = new TreeNode(1);

        root.left = new TreeNode(2);
        root.right = new TreeNode(3);

        root.left.right = new TreeNode(4);

        root.right.left = new TreeNode(5);
        root.right.right = new TreeNode(6);

        // Print answer
        System.out.println(topView(root));
    }
}








// # Example Tree:

// #           1
// #         /   \
// #        2     3
// #         \   / \
// #          4 5   6

// # Top View:

// # 2 1 3 6

// # Why?

// # Column -1 → 2
// # Column 0 → 1
// # Column +1 → 3
// # Column +2 → 6

// # Nodes 4 and 5 are hidden behind top nodes.

// # EASY LOGIC

// # We use:

// # BFS (Level Order Traversal) → because top node comes first
// # Horizontal Distance (HD)

// # Rules:

// # Root HD = 0
// # Left child HD = parent - 1
// # Right child HD = parent + 1