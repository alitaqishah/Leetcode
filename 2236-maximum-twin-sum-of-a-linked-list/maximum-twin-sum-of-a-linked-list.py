class Solution:
    def pairSum(self, head):

        # Step 1: Find middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev = None
        curr = slow

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Step 3: Calculate maximum twin sum
        maximum = 0

        first = head
        second = prev

        while second:
            total = first.val + second.val
            maximum = max(maximum, total)

            first = first.next
            second = second.next

        return maximum