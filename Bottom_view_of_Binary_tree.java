
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

public class Bottom_view_of_Binary_tree {

    public static List<Integer> bottomView(TreeNode root) {

        // Final answer list
        List<Integer> result = new ArrayList<>();

        // Empty tree check
        if (root == null)
            return result;

        // TreeMap:
        // key   = horizontal distance
        // value = latest(bottom-most) node
        TreeMap<Integer, Integer> map = new TreeMap<>();

        // Queue for BFS
        Queue<Pair> queue = new LinkedList<>();

        // Root starts from HD = 0
        queue.offer(new Pair(root, 0));

        // BFS traversal
        while (!queue.isEmpty()) {

            Pair current = queue.poll();

            TreeNode node = current.node;
            int hd = current.hd;

            // IMPORTANT:
            // Always overwrite value
            // Last node becomes bottom view node
            map.put(hd, node.val);

            // Move left
            if (node.left != null) {
                queue.offer(new Pair(node.left, hd - 1));
            }

            // Move right
            if (node.right != null) {
                queue.offer(new Pair(node.right, hd + 1));
            }
        }

        // Store answer left -> right
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
        System.out.println(bottomView(root));
    }
}