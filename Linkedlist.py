
# ==========================================
# PART 1: MAKE ONE BOX (NODE)
# ==========================================

class Node:
    def __init__(self, info, next=None):
        self.data = info       # Number inside the box
        self.next = next       # Arrow to the next box


# ==========================================
# PART 2: MAKE AN EMPTY LINKED LIST
# ==========================================

class SinglyLinkedlist:
    def __init__(self):
        self.head = None       # No boxes yet


# ==========================================
# PART 3: ADD A BOX AT THE END
# ==========================================

    def insertAtEnd(self, value):
        temp = Node(value)     # Make a new box

        # Example: Add 30
        #
        # BEFORE:
        # head -> [10|next] -> [20|None]
        #
        # NEW BOX:
        # temp -> [30|None]
        #
        # AFTER:
        # head -> [10|next] -> [20|next] -> [30|None]

        if self.head == None:  # Is the list empty?
            self.head = temp   # The new box becomes first
            return

        t1 = self.head         # Start at the first box

        while t1.next != None: # Is there another box?
            t1 = t1.next       # Move to the next box

        t1.next = temp         # Connect the last box to temp


# ==========================================
# PART 4: ADD A BOX AT THE BEGINNING
# ==========================================

    def insertAtBeg(self, value):
        temp = Node(value)     # Make a new box

        # Example: Add 5
        #
        # BEFORE:
        # head -> [10|next] -> [20|None]
        #
        # FIRST: Connect 5 to the old first box
        # temp -> [5|next] -> [10|next] -> [20|None]
        #
        # THEN: Move head to 5
        # head -> [5|next] -> [10|next] -> [20|None]

        temp.next = self.head  # Point 5 to the old first box
        self.head = temp       # Make 5 the first box


# ==========================================
# PART 5: ADD A BOX AFTER A GIVEN VALUE
# ==========================================

    def insertInMid(self, value, x):
        temp = Node(value)     # Make the new box
        t1 = self.head         # Start at the first box

        # Example: Add 40 after 20
        #
        # BEFORE:
        # head -> [10] -> [20] -> [30] -> None
        #
        # AFTER:
        # head -> [10] -> [20] -> [40] -> [30] -> None

        while t1 != None:      # Check each box

            if t1.data == x:   # Did we find x?

                temp.next = t1.next  # 40 points to 30
                t1.next = temp       # 20 points to 40

                return         # Stop after inserting

            t1 = t1.next       # Check the next box

        print("Value not found")


# ==========================================
# PART 6: DELETE A BOX
# ==========================================

    def deleteLL(self, value):

        # Example: Delete 20
        #
        # BEFORE:
        # head -> [10] -> [20] -> [30] -> None
        #
        # AFTER:
        # head -> [10] --------> [30] -> None
        #
        # The arrow skips box 20.

        if self.head == None:  # Is the list empty?
            print("List is empty")
            return

        # Is the first box the one to delete?
        if self.head.data == value:
            self.head = self.head.next  # Skip first box
            return

        prev = None             # Box before the current box
        t1 = self.head          # Current box

        while t1 != None:       # Check each box

            if t1.data == value:  # Found the box?
                prev.next = t1.next  # Skip that box
                return

            prev = t1           # Remember this box
            t1 = t1.next         # Move to the next box

        print("Value not found")


# ==========================================
# PART 7: PRINT ALL THE BOXES
# ==========================================

    def printLL(self):
        t1 = self.head          # Start at the first box

        # Example:
        # head -> [10] -> [20] -> None
        #
        # Print 10, then move to 20.
        # Print 20, then move to None.
        # Stop when t1 becomes None.

        while t1 != None:
            print(t1.data, end=" -> ")  # Print the number
            t1 = t1.next                # Move forward

        print("None")            # Show the end


# ==========================================
# PART 8: TRY THE OPERATIONS
# ==========================================

obj = SinglyLinkedlist()         # Make an empty list

obj.insertAtEnd(10)              # Add 10
obj.insertAtEnd(20)              # Add 20 at the end
obj.insertAtEnd(30)              # Add 30 at the end
obj.printLL()
# 10 -> 20 -> 30 -> None

obj.insertAtBeg(5)               # Add 5 at the beginning
obj.printLL()
# 5 -> 10 -> 20 -> 30 -> None

obj.insertInMid(40, 20)          # Add 40 after 20
obj.printLL()
# 5 -> 10 -> 20 -> 40 -> 30 -> None

obj.deleteLL(30)                 # Delete the box containing 30
obj.printLL()
# 5 -> 10 -> 20 -> 40 -> None
