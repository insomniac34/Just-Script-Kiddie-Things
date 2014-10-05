#include <iostream>
#include <cmath>

struct Node {
  Node *next;
  int data;
};


Node *RemoveDuplicates(Node*);
int main(void) {

  Node *first = new Node;
  first->data = 75;
  first->next = NULL;

  Node *second = new Node;
  second->data = 75;
  second->next = first;

  Node *third = new Node;
  third->data = 75;
  third->next = second;

  Node *fourth = new Node;
  fourth->data = 99;
  fourth->next = third;

  Node *fifth = new Node;
  fifth->data = 102;
  fifth->next = fourth;

  Node *sixth = new Node;
  sixth->data = 102;
  sixth->next = fifth;

  Node *seventh = new Node;
  seventh->data = 103;
  seventh->next = sixth;

  Node *theHead = RemoveDuplicates(seventh);
  //Node *theHead = fifth;

  Node *iter = theHead;
  while (iter!=NULL) {
    std::cout << iter->data << "->";
    if (iter->next==NULL) std::cout << "NULL" << std::endl;
    iter = iter->next;
  }

  return 0;
}

Node* RemoveDuplicates(Node *head)
{
  if (head==NULL) return NULL;
  // This is a "method-only" submission. 
  // You only need to complete this method.
  Node *ret = head;
  Node *prev = head;
  head = head->next;
  int pos = 0;
  while (head!=NULL) {
    if (prev->data==head->data) {
     
      prev->next = head->next;
      head->next = NULL;
      head = prev->next;
    }
    else {
      head=head->next;
      prev=prev->next;
    }
  }
  return ret;
}