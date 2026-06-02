package Tree;
import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;

    TreeNode(int val) {
        this.val = val;
    }
}

class Pair {
    TreeNode node;
    int column;

    Pair(TreeNode node, int column) {
        this.node = node;
        this.column = column;
    }
}

public class Vertical_Order_Traversal_of_Binary_Tree {

    public static List<List<Integer>> verticalTraversal(TreeNode root) {

        List<List<Integer>> result = new ArrayList<>();

        if (root == null)
            return result;

        TreeMap<Integer, List<Integer>> map = new TreeMap<>();

        Queue<Pair> queue = new LinkedList<>();
        queue.offer(new Pair(root, 0));

        while (!queue.isEmpty()) {

            Pair current = queue.poll();

            TreeNode node = current.node;
            int col = current.column;

            map.putIfAbsent(col, new ArrayList<>());
            map.get(col).add(node.val);

            if (node.left != null) {
                queue.offer(new Pair(node.left, col - 1));
            }

            if (node.right != null) {
                queue.offer(new Pair(node.right, col + 1));
            }
        }

        for (List<Integer> list : map.values()) {
            result.add(list);
        }

        return result;
    }

    public static void main(String[] args) {

        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(20);
        root.right.left = new TreeNode(15);
        root.right.right = new TreeNode(7);

        System.out.println(verticalTraversal(root));
    }
}