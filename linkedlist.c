#include <stdio.h>
#include <stdlib.h>

struct Node{

    int data;
    struct Node *next;

};



void traverse(struct Node *ptr)
{
    while (ptr!= NULL)
    {
        printf("Element is: %d\n", ptr->data);
        ptr = ptr->next;
    }
}


struct Node * insertatbeg(struct Node * head, int data){
    struct Node *ptr = (struct Node *)malloc(sizeof(struct Node));
    ptr->next = head;
    ptr->data= data;
    return ptr;
}

void insertatend(struct Node * head, int data){
    struct Node *ptr = (struct Node *)malloc(sizeof(struct Node));
    while (head->next!=NULL){
        head = head->next;
    }
    head->next = ptr;
    ptr->data = data;
    ptr->next = NULL;
    
    
}

void insertinbet(struct Node * head, int index, int data){
    struct Node *ptr = (struct Node *)malloc(sizeof(struct Node));
    int num=1;
    while (num!=index){
        num++;
        head = head->next;
    }
    ptr->next = head->next;
    ptr->data= data;
    head->next = ptr;
}

void insertafternode(struct Node * prevnode, int data){
    struct Node *ptr = (struct Node *)malloc(sizeof(struct Node));
    ptr-> data = data;

    ptr->next = prevnode->next;
    prevnode->next= ptr;
}

struct Node * deleteatbeg(struct Node * head){
    struct Node *ptr= head->next;
    free(head);
    return ptr;
}

void deleteatend(struct Node * head){
    struct Node *ptr = (struct Node *)malloc(sizeof(struct Node));
    while(head->next!=NULL){
        ptr= head;
        head= head->next;
    }
    free(head);
    ptr->next = NULL;
}

void deleteinbet(struct Node * head, int index){
    int num=0;
    struct Node *ptr = (struct Node *)malloc(sizeof(struct Node));
    while(index-1!=num){
        num++;
        ptr=head;
        head=head->next;
    }
    ptr->next= head->next;
    free(head);
}

void deleteafternode(struct Node * node){
    struct Node *ptr = node->next;
    node->next= ptr->next;
    free(ptr);
}

void main() 
{   
    struct Node *head;
    struct Node *second;
    struct Node *third;
    struct Node *fourth; 

    head = (struct Node *) malloc(sizeof(struct Node));
    second = (struct Node *) malloc(sizeof(struct Node));
    third = (struct Node *) malloc(sizeof(struct Node));
    fourth = (struct Node *) malloc(sizeof(struct Node));
    
    head->data = 10;
    head->next = second;

    second->data = 28;
    second->next = third;
    
    third->data = 91;
    third->next = fourth;

    fourth->data = 41;
    fourth->next = NULL;

    insertinbet(head,1,69);
    head = insertatbeg(head, 15);
    head = insertatbeg(head, 13);
    insertatend(head,96);
    insertafternode(fourth, 79);
    //deleteatend(head);
    //head = deleteatbeg(head);
    //deleteinbet(head,2);
    //deleteafternode(fourth);
    traverse(head);

}