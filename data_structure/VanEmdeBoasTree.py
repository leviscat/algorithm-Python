import math

class VanEmdeBoasTree:
    def __init__(self, universe_size):
        self.u = universe_size  # Universe size
        self.min = None  # Minimum value in the tree
        self.max = None  # Maximum value in the tree
        if self.u > 2:
            # Initialize the summary and clusters
            sqrt_u = int(math.ceil(math.sqrt(self.u)))
            self.summary = VanEmdeBoasTree(sqrt_u)  # Summary tree
            self.cluster = [VanEmdeBoasTree(sqrt_u) for _ in range(sqrt_u)]  # Cluster trees
#summary 是一个 VanEmdeBoasTree 对象 python的对象不需要指定类型，所以可以直接赋值 和java不一样，java需要指定类型
    # Find minimum value
    def find_min(self):
        return self.min

    # Find maximum value
    def find_max(self):
        return self.max

    # Insert a value into the tree
    def insert(self, x):
        if self.min is None:
            self.min = self.max = x  # If tree is empty
        else:
            if x < self.min:
                self.min, x = x, self.min
            if self.u > 2:
                cluster_index = self._high(x)
                if self.cluster[cluster_index].min is None:
                    self.summary.insert(self._high(x))  # Update the summary
                self.cluster[cluster_index].insert(self._low(x))
        return

    # Delete a value from the tree
    def delete(self, x):
        if self.min == self.max:  # Only one element in the tree
            self.min = self.max = None
        elif self.u == 2:
            self.min = 1 - self.min
            self.max = self.min
        else:
            if x == self.min:
                first_cluster = self.summary.find_min()
                x = self._index(first_cluster, self.cluster[first_cluster].find_min())
                self.min = x
            cluster_index = self._high(x)
            self.cluster[cluster_index].delete(self._low(x))
            if self.cluster[cluster_index].min is None:
                self.summary.delete(cluster_index)
                if x == self.max:
                    summary_max = self.summary.find_max()
                    if summary_max is None:
                        self.max = self.min
                    else:
                        self.max = self._index(summary_max, self.cluster[summary_max].find_max())
        return

    # Helper methods
    def _high(self, x):
        return x // int(math.sqrt(self.u))

    def _low(self, x):
        return x % int(math.sqrt(self.u))

    def _index(self, high, low):
        return high * int(math.sqrt(self.u)) + low

# Example usage:
vEB_tree = VanEmdeBoasTree(16)  # Tree size 16
vEB_tree.insert(5)
vEB_tree.insert(9)
vEB_tree.insert(3)

print("Min:", vEB_tree.find_min())  # Min: 3
print("Max:", vEB_tree.find_max())  # Max: 9
vEB_tree.delete(3)
print("Min after delete:", vEB_tree.find_min())  # Min after delete: 5
#主要思想是将一个大的问题分解成小的问题，然后递归解决，这样可以减少问题的规模，提高效率"Van Emde Boas 树" 就是以 Peter van Emde Boas 的名字命名的