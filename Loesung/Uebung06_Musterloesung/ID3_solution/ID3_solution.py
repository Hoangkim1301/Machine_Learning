import pandas as pd
import numpy as np
from ID3_solution.utils import *


def entropy(vals: list) -> float:
    """
    Computes the entropy for a list of nominal attribute values
    :param vals: list[str] of values
    :return: entropy
    """
    attr_vals, counts = np.unique(vals, return_counts=True)
    sum_counts = np.sum(counts)
    entropy = np.sum([
        (-counts[i] / sum_counts) * np.log2(counts[i] / sum_counts)
        for i in range(len(attr_vals))])
    return entropy


class ID3:
    """
    ID3 decision tree for nominal attributes
    """

    def __init__(self, csv_file):
        # Read a CSV file
        data = pd.read_csv(csv_file)
        # Select column containing target values (e.g. "Play Tennis")
        self.target_col = list(data.columns)[-1]
        # All other columns are attributes
        attr_cols = list(data.columns)[:-1]
        self.tree = self.build_tree(data, attr_cols)

    def get_tree(self) -> Node:
        return self.tree

    def predict(self, instance: dict) -> str:
        """
        Traverses decision tree and returns the target value in the leaf node
        :param instance: a dict containing (attribute name: attribute value) entries
        :return: prediction of leaf node after traversing tree
        """

        def traverse(node: Node):
            # If node is a leaf, return prediction
            if type(node) is PredictionNode:
                return node.prediction
            # Otherwise, node is an internal node, follow branch where attribute has the same value as instance
            else:
                attr_name = node.attr_name
                attr_val = instance[attr_name]
                attr_node = node.get_child(attr_val)
                return traverse(attr_node)

        return traverse(self.tree)

    def info_gain(self, examples: pd.DataFrame, attr: str) -> float:
        """
        Computes the information gain when splitting on `attr`
        :param examples: examples to compute information gain
        :param attr: attribute to use for splitting
        :return: information gain when `attr` is used for splitting
        """
        attr_vals = list(examples[attr].unique())
        hs = entropy(examples[self.target_col])
        subsets = [examples[examples[attr] == v] for v in attr_vals]
        hsa = []
        for s in subsets:
            p = len(s) / len(examples)
            hsa += [p * entropy(s[self.target_col])]
        ig = hs - sum(hsa)
        return ig

    def get_split_attr(self, examples: pd.DataFrame, attributes: list) -> str:
        """
        Finds the attribute with highest information gain
        :param examples: remaining examples at current node
        :param attributes: list[str] of attributes to compute information gain for
        :return: attribute with split results in highest information gain
        """
        info_gains = []
        for a in attributes:
            info_gains += [self.info_gain(examples, a)]
        return attributes[np.argmax(info_gains)]

    def build_tree(self, examples: pd.DataFrame, attributes: list) -> Node:
        """
        Constructs an ID3 decision tree recursively by splitting attributes with highest information gain
        :param examples: (partition of) examples
        :param attributes: list[str] of remaining attributes which can be used for splitting
        :return: Root node of a (sub)tree
        """
        target_vals = list(examples[self.target_col].unique())
        if len(target_vals) == 1:
            # If target values are all the same, node is a leaf node which predicts this target class
            return PredictionNode(target_vals[0])
        elif len(attributes) == 0:
            # If no attributes to split are left, node is a leaf node which predicts most frequent class
            return PredictionNode(examples[self.target_col].mode()[0])
        else:
            # Otherwise, find the best attribute to split
            attr = self.get_split_attr(examples, attributes)
            attr_vals = list(examples[attr].unique())
            children = []
            # Recursively build tree for each possible attribute value
            for a in attr_vals:
                remaining_attrs = attributes.copy()
                remaining_attrs.remove(attr)
                selected_examples = examples[examples[attr] == a]
                children.append(self.build_tree(selected_examples, remaining_attrs))
            return SplitNode(attr, children, attr_vals)
