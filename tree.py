class Node:
    def __init__(self, name, value=1):
        self.name = name
        self.value = value
        self.parent = None
        self.children = []

    def get_value(self):
        return self.value

    def get_level(self):
        """Returns the level of the node in the tree."""

        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level

    def get_parent(self):
        if self.parent:
            return self.parent
        else:
            return None

    def get_children(self):
        return self.children

    def set_child(self, child):
        self.children.append(child)
        child.parent = self

    def set_parent(self, parent):
        self.parent = parent
        parent.children.append(self)

    def remove_parent(self):
        self.parent = None

    def remove_child(self, child):
        print(f"The name of the parent was {child.get_parent().name}")
        print(child.get_value())
        print(type(child.get_parent()))
        child.remove_parent()
        self.children.remove(child)

