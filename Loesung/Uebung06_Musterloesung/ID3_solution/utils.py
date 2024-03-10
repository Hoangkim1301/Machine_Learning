class Node:
    def __init__(self, label):
        self.label = label


class SplitNode(Node):
    """
    Internal node which splits on attribute `attr_name`. It contains references to its children which correspond to
    all possible values of this attribute.
    """

    def __init__(self, attr_name, children: list, attr_values: list):
        """
        :param attr_name: name of attribute
        :param children: list[Node] - list of child nodes
        :param attr_values: list[str] - list of attribute values
        """
        self.children = children
        self.attr_values = attr_values
        self.attr_name = attr_name
        self.attr_val_child_map = {attr_val: child for (attr_val, child) in zip(attr_values, children)}
        super(SplitNode, self).__init__(attr_name)

    def get_child(self, attr_val: str) -> Node:
        """
        Returns child node corresponding `attr_val`
        :param attr_val: a value of nodes attribute
        :return: child node for attribute value
        """
        return self.attr_val_child_map[attr_val]

    def get_children(self) -> list:
        """
        Returns all children of node
        :return: list[Node] of child nodes
        """
        return self.children

    def get_attr_vals(self) -> list:
        """
        Returns all attribute values of node
        :return: list[str] of attribute values
        """
        return self.attr_values


class PredictionNode(Node):
    """
    A leaf node which only holds the predicted target class.
    """

    def __init__(self, prediction):
        self.prediction = prediction
        super(PredictionNode, self).__init__(prediction)


def tree_to_dot(tree: Node) -> str:
    """
    Converts a tree to graph description in DOT.
    For DOT graph description language see: https://en.wikipedia.org/wiki/DOT_(graph_description_language)
    :param tree: root node of the decision tree
    :return: String in DOT
    """
    global current_id
    current_id = 0

    def get_next_id():
        global current_id
        current_id += 1
        return "Node" + str(current_id)

    def convert_node(node: Node, node_id: int) -> str:
        if type(node) is PredictionNode:
            return "%s [label=\"%s\" shape=rect color=lightgrey style=filled];\n" % (node_id, node.label)
        if type(node) is SplitNode:
            s = "%s [label=\"%s\" shape=ellipse color=lightblue2 style=filled];\n" % (node_id, node.label)
            for c, attr_val in zip(node.get_children(), node.get_attr_vals()):
                child_node_id = get_next_id()
                s += "%s -> %s [label=\"%s\"];\n" % (node_id, child_node_id, attr_val)
                s += convert_node(c, child_node_id)
            return s

    return "digraph ID3 { %s }" % convert_node(tree, current_id)
