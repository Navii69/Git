#include <stdio.h>
#include <stdlib.h>

struct Node{

    int data;
    struct Node *next;

};

void traverse(struct Node * head){
    struct Node *ptr = head;
    do{
        printf("Element is: %d\n", ptr->data);
        ptr = ptr->next;
    }while(ptr!=head);

}

struct Node * insertatbeg(struct Node *head, int data){
    struct Node *ptr = (struct Node *)malloc(sizeof(struct Node));
    struct Node * p = head-> next;

    while(p->next!=head){
        p= p->next;
    }
    ptr->data= data;
    p->next= ptr;
    ptr->next= head;
    head=ptr;
}
    

void main(){
    struct Node *head = (struct Node *)malloc(sizeof(struct Node));
    struct Node *second = (struct Node *)malloc(sizeof(struct Node));
    struct Node *third = (struct Node *)malloc(sizeof(struct Node));
    struct Node *fourth = (struct Node *)malloc(sizeof(struct Node));

    head->next = second;
    head->data=10;

    second->data = 31;
    second->next = third;

    third->data = 41;
    third->next = fourth;

    fourth->data = 89;
    fourth->next = head;

    head = insertatbeg(head,43);
    traverse(head);

}