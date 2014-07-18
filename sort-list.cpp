/**
 * Author: Yaguang Ding
 * Sort a linked list in O(n log n) time using constant space complexity.
 * 单链表归并排序，时间复杂度O(n log n)，空间复杂度O(1)
 */
#include <iostream>
#include <time.h>


struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};


void printList(ListNode * p, ListNode *end)
{
    while(p != end)
    {
        std::cout<<p->val << ' ';
        p = p->next;
    }
    std::cout<< '\n';
}

class Solution
{
public:
    ListNode *sortList(ListNode *head)
    {
        _sort(head, NULL);
        return head;
    }

private:
    /* [begin, end)区间
     * 归并排序
     */
    void _sort(ListNode *begin, ListNode *end)
    {
        //处理0~1个节点
        if (begin == NULL || begin->next == end)
        {
            return ;
        }
        //处理两个节点，交换数据
        else if (begin->next->next == end)
        {
            if ( begin->val > begin->next->val)
            {
                int t = begin->val;
                begin->val = begin->next->val;
                begin->next->val = t;
            }
            return ;
        }
        // 寻找中间节点
        ListNode * p1 = begin, *p2 = begin->next;
        while(p2 != end)
        {
            p1 = p1->next;
            p2 = p2->next;
            if(p2 != end)
            {
                p2 = p2->next;
            }
        }
        //排序
        _sort(begin, p1);
        _sort(p1, end);
        _merge(begin, p1, end);
    }
    
    void _merge(ListNode *begin, ListNode *half, ListNode *end)
    {
        ListNode *p1 = begin, *cur = begin, *p2 = half;
        // 如果p1 > p2 则需要调换位置，调整p1, p2
        if(p1->val > p2->val)
        {
            int p1_val = p1->val;
            ListNode * p1_next = p1->next;
            // 将p2->val 放到p1->val
            p1->val = p2->val;
            // new 一个新节点，作为新的p1
            p1 = new ListNode(p1_val);
            p1->next = p1_next;
            // 删除 p2, 并且指针后移
            ListNode * p2_old = p2;
            p2 = p2->next;
            delete p2_old;
        }else
        {
            p1 = begin->next;
        }
        //开始归并
        while(p1 != half || p2 != end)
        {
            if(p2!= end && (p1==half || p1->val > p2->val))
            {
                cur->next = p2;
                cur = p2;
                p2 = p2->next;
            }else
            {
                cur->next = p1;
                cur = p1;
                p1 = p1->next;
            }
        }
        cur->next = end;
    }
};




ListNode * createRandomList()
{
    srand((unsigned)time(NULL));
    ListNode *head = new ListNode(5);
    ListNode *p = head;
    for (int i=0; i< 101; i++)
    {
        p->next = new ListNode(rand()%100);
        p = p->next;
    };
    return head;
}


int main()
{
    
    ListNode * l = createRandomList();
    Solution s = Solution();
    printList(l, NULL);
    std::cout<<"sorted:"<< '\n';
    printList(s.sortList(l), NULL);
    return 0;
}