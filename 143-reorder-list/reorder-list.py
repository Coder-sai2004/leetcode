# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        if head and head.next:
            tail=head
            head=head.next
            tail.next=None
        else:
            return head
            
        while head:
            x=head.next
            head.next=tail
            tail=head
            head=x
            
        return tail
    
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        n=0
        dummy=head
        while dummy:
            n+=1
            dummy=dummy.next
        m=n//2
        st=[]
        i=0
        #adding first half of linked list nodes to the stack.
        while head:
            if i==m:
                break
            i+=1
            x=head.next
            head.next=None
            st.append(head)
            head=x
        
        #intializing middle of linked list to the res for returning purpose.
        res=head   
        #if size is even there is no problem.but if it is odd ,there will be an extra node ,so we move forward and extra node.
        if n%2!=0:
            head=head.next
        
        #attaching the nodes in the desired format
        while head:
            x=head.next
            if st:
                node=st.pop()
            head.next=node
            node.next=x
            head=x
            
        #we attached it in the reverse order,so in order to get required result,we just need to reverse the linked list.
        ans=self.reverse(res)     
        return ans