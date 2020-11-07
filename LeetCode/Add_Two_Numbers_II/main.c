/* main.c */

#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

int add(int, struct ListNode*, struct ListNode*, struct ListNode*);

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode* l1_ = l1;
    struct ListNode* l2_ = l2;
    int ll1=0, ll2=0;
    while (l1_ != NULL){ll1++;l1_=l1_->next;};
    while (l2_ != NULL){ll2++;l2_=l2_->next;};
    struct ListNode* l = &(struct ListNode){0, NULL};
    struct ListNode* l_ = l;
    l1_ = l1, l2_ = l2;
    int i = add(ll1 - ll2, l1_, l2_, l);
    printf("\n");
    while (l_ != NULL){
      printf("[%p] ", l_);
      printf("%d\n", l_->val);
      l_ = l_->next;
    }
    
    return l;
}

int add(int diff, struct ListNode* l1, struct ListNode* l2, struct ListNode* l){
        if (l1 != NULL && l2 != NULL){
          if (l1->next != NULL && l2->next != NULL){
            struct ListNode* ne = malloc(sizeof(struct ListNode));
            ne->val = 0;
            ne->next = NULL;
            l->next = ne;
          }
            int n = 0;
            if (diff < 0)
                n = l2->val + add(diff+1, l1, l2->next, l->next);
            else if (diff > 0)
                n = l1->val + add(diff-1, l1->next, l2, l->next);
            else
                n = l1->val + l2->val + add(0, l1->next, l2->next, l->next);
            l->val = n%10;
            printf("[%p] ", l);
            printf("%d\n", l->val);
            return n/10;
        }
        return 0;
}

int main(void){
    struct ListNode* l1 = &(struct ListNode){7, NULL};
    l1->next = &(struct ListNode){2, NULL};
    l1->next->next = &(struct ListNode){4, NULL};
    l1->next->next->next = &(struct ListNode){3, NULL};

    struct ListNode* l2 = &(struct ListNode){5, NULL};
    l2->next = &(struct ListNode){6, NULL};
    l2->next->next = &(struct ListNode){5, NULL};

    addTwoNumbers(l1, l2);
}
