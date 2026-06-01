# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        st=[]
        res=[0]*len(arr)
        for i in range(len(arr)):
            while st and arr[st[-1]]<arr[i]:
                idx=st.pop()
                res[idx]=arr[i]
            st.append(i)

        return res
        
        #i we return in linked list.
        # result=None
        # tail=None
        # for i in range(len(res)):
        #     node=ListNode(res[i])
        #     if result is None:
        #         result=node
        #         tail=node
        #     else:
        #         tail.next=node
        #         tail=tail.next
        # return result

