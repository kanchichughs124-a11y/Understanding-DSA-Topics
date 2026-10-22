
# ==================================================
# PART 1: MAKE ONE BOX (NODE)
# ==================================================

class Node:
    def __init__(self, info, next=None):

        self.data = info
        # Store the number inside the box.

        self.next = next
        # Store the link to the next box.
        # If there is no next box, next is None.


# Example:
#
# a = Node(10)
#
#      a
#      |
#      v
#   +--------+
#   | 10 |None|
#   +--------+
#
# 10 is the number.
# None means there is no next box.


# ==================================================
# PART 2: MAKE AN EMPTY LINKED LIST
# ==================================================

class SinglyLinkedlist:
    def __init__(self):

        self.head = None
        # Head tells us where the first box is.
        # None means there are no boxes yet.


# Empty list:
#
# head
#   |
#   v
#  None


# ==================================================
# PART 3: INSERT A BOX AT THE END
# ==================================================

    def insertAtEnd(self, value):

        temp = Node(value)
        # Make a new box.
        # temp points to this new box.

        # Example: Add 30.
        #
        # BEFORE:
        #
        # head
        #   |
        #   v
        # +------+    +--------+
        # | 10 |next|->| 20 |None|
        # +------+    +--------+
        #
        # NEW BOX:
        #
        # temp
        #   |
        #   v
        # +--------+
        # | 30 |None|
        # +--------+

        if self.head == None:
            # Is the list empty?

            self.head = temp
            # If empty, make the new box the first box.

            return
            # Stop because we have finished inserting.

        t1 = self.head
        # Start looking from the first box.
        #
        # t1
        #  |
        #  v
        # [10] -> [20] -> None

        while t1.next != None:
            # Is there another box after this one?

            t1 = t1.next
            # Move t1 to the next box.

        # We have reached the last box.
        #
        # t1
        #  |
        #  v
        # [20] -> None

        t1.next = temp
        # Connect the last box to the new box.
        #
        # FINAL:
        #
        # head
        #   |
        #   v
        # [10] -> [20] -> [30] -> None


# ==================================================
# PART 4: INSERT A BOX AT THE BEGINNING
# ==================================================

    def insertAtBeg(self, value):

        temp = Node(value)
        # Make a new box.
        # Example: Add 5.
        #
        # temp -> [5 | None]
        #
        # OLD LIST:
        # head -> [10] -> [20] -> None

        temp.next = self.head
        # Make box 5 point to the old first box.
        #
        # temp -> [5] -> [10] -> [20] -> None

        self.head = temp
        # Now make head point to box 5.
        #
        # FINAL:
        #
        # head -> [5] -> [10] -> [20] -> None


# ==================================================
# PART 5: INSERT AFTER A GIVEN VALUE
# ==================================================

    def insertInMid(self, value, x):

        temp = Node(value)
        # Make the new box.
        # Example: Add 40 after 20.

        t1 = self.head
        # Start looking from the first box.

        # BEFORE:
        #
        # head -> [10] -> [20] -> [30] -> None
        #
        # We want:
        #
        # head -> [10] -> [20] -> [40] -> [30] -> None

        while t1 != None:
            # Keep checking boxes until the list ends.

            if t1.data == x:
                # Did we find the box containing x?
                # Here, x is 20.

                temp.next = t1.next
                # First, make 40 point to the box after 20.
                #
                # [40] -> [30] -> None

                t1.next = temp
                # Now make 20 point to 40.
                #
                # [20] -> [40] -> [30] -> None

                return
                # Stop because insertion is finished.

            t1 = t1.next
            # If x was not found, check the next box.

        print("Value not found")
        # Show this if x is not in the list.


# ==================================================
# PART 6: DELETE A BOX
# ==================================================

    def deleteLL(self, value):

        # Example: Delete box 20.
        #
        # BEFORE:
        #
        # head -> [10] -> [20] -> [30] -> None
        #
        # AFTER:
        #
        # head -> [10] --------> [30] -> None
        #
        # Box 10 now points directly to box 30.

        if self.head == None:
            # Is the list empty?

            print("List is empty")
            # Nothing is available to delete.

            return
            # Stop here.

        if self.head.data == value:
            # Is the first box the one we want to delete?

            self.head = self.head.next
            # Move head to the second box.
            #
            # BEFORE:
            # head -> [10] -> [20] -> None
            #
            # AFTER:
            # head --------> [20] -> None

            return
            # Stop because deletion is finished.

        prev = None
        # prev will remember the box before t1.

        t1 = self.head
        # Start t1 at the first box.

        while t1 != None:
            # Check each box.

            if t1.data == value:
                # Did we find the number to delete?

                prev.next = t1.next
                # Make the previous box skip this box.
                #
                # BEFORE:
                # [10] -> [20] -> [30] -> None
                #
                # AFTER:
                # [10] --------> [30] -> None

                return
                # Stop because deletion is finished.

            prev = t1
            # Remember the current box as the previous box.

            t1 = t1.next
            # Move to the next box.

        print("Value not found")
        # The number was not in the list.


# ==================================================
# PART 7: PRINT ALL THE BOXES
# ==================================================

    def printLL(self):

        t1 = self.head
        # Start at the first box.

        # Example:
        #
        # head -> [10] -> [20] -> [30] -> None
        #
        # First, print 10.
        # Then move to 20 and print it.
        # Then move to 30 and print it.
        # Then move to None and stop.

        while t1 != None:
            # Keep going while a box exists.

            print(t1.data, end=" -> ")
            # Print the number inside this box.

            t1 = t1.next
            # Move to the next box.

        print("None")
        # Show that the train has ended.


# ==================================================
# PART 8: TRY ALL THE OPERATIONS
# ==================================================

obj = SinglyLinkedlist()
# Make an empty linked list.
#
# head -> None


# -------- INSERT AT THE END --------

obj.insertAtEnd(10)
# head -> [10] -> None

obj.insertAtEnd(20)
# head -> [10] -> [20] -> None

obj.insertAtEnd(30)
# head -> [10] -> [20] -> [30] -> None

obj.printLL()
# OUTPUT:
# 10 -> 20 -> 30 -> None


# -------- INSERT AT THE BEGINNING --------

obj.insertAtBeg(5)
# Add 5 before 10.
#
# head -> [5] -> [10] -> [20] -> [30] -> None

obj.printLL()
# OUTPUT:
# 5 -> 10 -> 20 -> 30 -> None


# -------- INSERT AFTER A VALUE --------

obj.insertInMid(40, 20)
# Add 40 after 20.
#
# head -> [5] -> [10] -> [20] -> [40] -> [30] -> None

obj.printLL()
# OUTPUT:
# 5 -> 10 -> 20 -> 40 -> 30 -> None


# -------- DELETE A VALUE --------

obj.deleteLL(30)
# Remove the box containing 30.
#
# head -> [5] -> [10] -> [20] -> [40] -> None

obj.printLL()
# OUTPUT:
# 5 -> 10 -> 20 -> 40 -> None
