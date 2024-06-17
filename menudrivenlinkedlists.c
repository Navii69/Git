#include <stdio.h>
#include <stdlib.h>

struct Node
{

    int data;
    struct Node *next;
};

int getdata()
{
    int data;
    printf("Enter the element: ");
    scanf("%d", &data);
    return data;
}

// Functions for Inserting an element
// ############################################################
struct Node *insbeg(struct Node *head)
{
    struct Node *ptr = (struct Node *)malloc(sizeof(struct Node));

    ptr->data = getdata();
    ptr->next = head;
    head = ptr;
    return head;
}
// ############################################################

// ############################################################
void insend(struct Node *head)
{

    struct Node *ptr = (struct Node *)malloc(sizeof(struct Node));

    while (head->next != NULL)
    {
        head = head->next;
    }

    ptr->data = getdata();
    ptr->next = NULL;

    head->next = ptr;
}
// ############################################################

// ############################################################
void insindex(struct Node *head)
{
    struct Node *ptr = (struct Node *)malloc(sizeof(struct Node));
    int index, option, flag = 1;

    printf("Enter the position: ");
    scanf("%d", &index);

    while (flag == 1)
    {

        printf("\n1. Insert the element at the position\n");
        printf("2. Insert the element after the position\n");
        printf("3. Insert the element before the position\n");
        printf("Enter the option: ");
        scanf("%d", &option);

        if (option == 1)
        {
            for (int i = 0; i < index - 2; i++)
            {
                head = head->next;
            }
            break;
        }

        else if (option == 2)
        {
            for (int i = 0; i < index - 1; i++)
            {
                head = head->next;
            }
            break;
        }

        else if (option == 3)
        {
            for (int i = 0; i < index - 2; i++)
            {
                head = head->next;
            }
            break;
        }

        else
        {
            printf("\nPlease enter one of the options mentioned\n");
            continue;
        }
        break;
    }

    ptr->data = getdata();
    ptr->next = head->next;
    head->next = ptr;
}
// ############################################################

// Functions for Deleting an element
//  ############################################################
struct Node *delbeg(struct Node *head)
{
    struct Node *ptr;
    ptr = head->next;
    free(head);
    return ptr;
}
// ############################################################

// ############################################################
void delend(struct Node *head)
{
    struct Node *ptr;
    while (head->next != NULL)
    {
        ptr = head;
        head = head->next;
    }

    ptr->next = NULL;
    free(head);
}
// ############################################################

// ############################################################
void delval(struct Node *head)
{
    struct Node *ptr;
    int val;

    printf("Enter the element: ");
    scanf("%d", &val);

    while (head->data != val)
    {
        ptr = head;
        head = head->next;
    }

    ptr->next = head->next;
    free(head);
}
// ############################################################

// ############################################################
void delallval(struct Node *head)
{
    struct Node *ptr;
    struct Node *ptr2;
    int val;

    printf("Enter the element: ");
    scanf("%d", &val);

    while (head != NULL)
    {
        ptr = head;
        head = head->next;

        if (head->data == val)
        {
            ptr->next = head->next;
            ptr2 = head;
            free(ptr2);
        }
    }
}
// ############################################################

// Functions for searching an element
//  ############################################################
void search(struct Node *head)
{
    int el = getdata();
    int flag1 = 0;

    while (head != NULL)
    {
        if (head->data == el)
        {
            printf("\nElement is found\n");
            flag1 = 1;
            break;
        }
        head = head->next;
    }

    if (flag1 != 1)
        printf("\nElement doesn't exist\n");
}
// ############################################################

// ############################################################
void elecount(struct Node *head)
{
    int count = 0, el = getdata();

    while (head != NULL)
    {
        if (head->data == el)
            count++;

        head = head->next;
    }

    if (count != 0)
        printf("\nThe element was found %d number of times\n", count);

    else
        printf("\nThe element does not exist\n");
}
// ############################################################

// ############################################################
void findpos(struct Node *head)
{
    int count = 0, ele = getdata();

    while (head != NULL)
    {
        count++;
        if (head->data == ele)
        {
            printf("\nThe position of the element is %d\n", count);
            break;
        }
        head = head->next;
    }
}
// ############################################################

// Functions for Traversing an element
// ############################################################
void display(struct Node *head)
{

    while (head != NULL)
    {

        printf("Element is: %d\n", head->data);
        head = head->next;
    }
}
// ############################################################


// ############################################################
void revdisplay(struct Node *head)
{
    if (head == NULL)
        return;

    revdisplay(head->next);
    printf("Element is: %d\n", head->data);
}
// ############################################################


// ############################################################
void allcount(struct Node *head)
{
    int count = 0;

    while(head!=NULL)
    {
        count++;
        head = head->next;
    }
    printf("\nThe number of elements of are: %d\n",count);
}
// ############################################################



// Functions to Modify the data
// ############################################################
void update(struct Node *head)
{
    int index;
    int newdata;

    printf("Enter the position where you want to update the data:");
    scanf("%d", &index);

    newdata = getdata();

    for(int x =0; x < index-1; x++)
    {
        head = head -> next;
    }

    head -> data = newdata;
}
// ############################################################


// ############################################################
void revorder(struct Node *head)
{
    struct Node *ptr;
    if (head == NULL)
    return;

    ptr = head;
    head = head->next;

    revorder(head);
    
}  


void main()
{
    int primary, secondary, flag = 1;

    // Initializing the pointers and allocating them memory
    struct Node *head = (struct Node *)malloc(sizeof(struct Node));
    struct Node *second = (struct Node *)malloc(sizeof(struct Node));
    struct Node *third = (struct Node *)malloc(sizeof(struct Node));
    struct Node *fourth = (struct Node *)malloc(sizeof(struct Node));
    struct Node *fifth = (struct Node *)malloc(sizeof(struct Node));

    // Assiging the values and linking the nodes
    head->data = 15;
    head->next = second;

    second->data = 76;
    second->next = third;

    third->data = 130;
    third->next = fourth;

    fourth->data = 99;
    fourth->next = fifth;

    fifth->data = 57;
    fifth->next = NULL;

    while (flag == 1)
    {

        printf("\n ______________________________________________\n");
        printf("Menu Driven for Linked Lists\n");
        printf("\n1. Insert an element\n");
        printf("2. Delete an element\n");
        printf("3. Search the value\n");
        printf("4. Display the elements\n");
        printf("5. Modify an element\n");
        printf("6. More operations\n");
        printf("7. Exit\n");
        printf("Enter the option: ");
        scanf("%d", &primary);
        // Secondary options after choosing option number 1

        switch (primary)
        {
        case 1:
            while (flag == 1)
            {
                printf("\n ______________________________________________\n");
                printf("\n1.Insert at the beginning\n");
                printf("2.Insert at the end\n");
                printf("3.Insert at a index in the list\n");
                printf("4.Go back\n");
                printf("Choose the option: ");
                scanf("%d", &secondary);

                if (secondary == 1)
                {
                    head = insbeg(head);
                    display(head);
                    break;
                }

                else if (secondary == 2)
                {
                    insend(head);
                    display(head);
                    break;
                }

                else if (secondary == 3)
                {
                    insindex(head);
                    display(head);
                    break;
                }

                else if (secondary == 4)
                    break;

                else
                {
                    printf("Please enter the one of the options mentioned above");
                    continue;
                }
            }
            break;

        case 2:
            while (flag == 1)
            {
                printf("\n1.Delete from the beginning\n");
                printf("2.Delete from the end of the list\n");
                printf("3.Delete a specific element in the list\n");
                printf("4.Delete all occurences of a specific element from the list\n");
                printf("5.Go back\n");
                printf("Choose the option: ");
                scanf("%d", &secondary);

                switch (secondary)
                {
                case 1:
                    head = delbeg(head);
                    display(head);
                    break;

                case 2:
                    delend(head);
                    display(head);
                    break;

                case 3:
                    delval(head);
                    display(head);
                    break;

                case 4:
                    delallval(head);
                    display(head);

                case 5:
                    break;

                default:
                    printf("\n\nPlease enter one of the options mentioned above\n\n");
                    break;
                }
            }
            break;

        case 3:
            while (flag == 1)
            {
                printf("\n\n1.Search for a specific element in the list\n");
                printf("2.Find the position of a specific element in the list\n");
                printf("3.Count the number of times that element occur in the list\n");
                printf("4.Go back\n");
                printf("Choose the option: ");
                scanf("%d", &secondary);

                switch (secondary)
                {
                case 1:
                    search(head);
                    break;

                case 2:
                    findpos(head);
                    break;

                case 3:
                    elecount(head);
                    break;

                case 4:
                    break;

                default:
                    printf("Please enter one of the options given above");
                    break;
                }
            }
            break;

        case 4:
            while (flag == 1)
            {
                printf("\n\n1.Display the entire list\n");
                printf("2.Display the list in the reverse order\n");
                printf("3.Count the number of elements\n");
                printf("4.Go back\n");
                printf("Choose the option: ");
                scanf("%d", &secondary);

                switch (secondary)
                {
                case 1:
                    display(head);
                    break;

                case 2:
                    revdisplay(head);
                    break;

                case 3:
                    allcount(head);
                    break;
                
                case 4:
                    break;
                
                default:
                    printf("Please select one of the options mentioned above.");
                    break;
                }
            }
        
        case 5:
            while(flag ==1 )
            {
                printf("\n1.Update the value of a specific element in the list\n");
                printf("2.Reverse the order of elements in the list\n");
                printf("3.Sort the elements in the list\n");
                printf("4.Go back\n");
                printf("Choose the option: ");
                scanf("%d", &secondary);


                switch(secondary)
                {
                    case 1:
                        update(head);
                        display(head);
                        break;

                }
            }

        default:
            break;
        }
    }
}