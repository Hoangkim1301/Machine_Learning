import pandas as pd
import numpy as np
from ID3.utils import *


def entropy(vals: list) -> float:
    """
    Computes the entropy for a list of nominal attribute values
    :param vals: list[str] of values
    :return: entropy
    """
    
    # Insert your code here
    
    return 0.0


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

        # Insert your code here

        return ""

    def info_gain(self, examples: pd.DataFrame, attr: str) -> float:
        """
        Computes the information gain when splitting on `attr`
        :param examples: examples to compute information gain
        :param attr: attribute to use for splitting
        :return: information gain when `attr` is used for splitting
        """
        
        # Insert your code here
        
        return 0.0

    def get_split_attr(self, examples: pd.DataFrame, attributes: list) -> str:
        """
        Finds the attribute with highest information gain
        :param examples: remaining examples at current node
        :param attributes: list[str] of attributes to compute information gain for
        :return: attribute with split results in highest information gain
        """
        
        # Insert your code here
        
        return ""

    def build_tree(self, examples: pd.DataFrame, attributes: list) -> Node:
        """
        Constructs an ID3 decision tree recursively by splitting attributes with highest information gain
        :param examples: (partition of) examples
        :param attributes: list[str] of remaining attributes which can be used for splitting
        :return: Root node of a (sub)tree
        """
        
        # Insert your code here
        
        return None
