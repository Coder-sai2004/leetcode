# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        size=0
        dummy=head
        #calculating the size of linked list
        while dummy:
            size+=1
            dummy=dummy.next
        # part_size refers to number of equal parts, where extra_parts refers to first parts that have 1 extra size
        part_size=size//k
        extra_parts=size%k
        ans=[]
        for i in range(k):
            if extra_parts>0:
                current_part_size=part_size+1
                extra_parts-=1
            else:
                current_part_size=part_size
            #h refers to head and t refers to tail for new linked list parts
            h=None
            t=None
            i=0
            #single part linked list creation
            while i!=current_part_size and head:
                if h is None:
                    h=head
                    t=head
                else:
                    t.next=head
                    t=head
                head=head.next
                i+=1
            #disconnection between parts
            if t:
                t.next=None
            ans.append(h)
        return ans