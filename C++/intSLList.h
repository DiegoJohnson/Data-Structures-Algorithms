//**************** intSLList.h ****************
//            singly-linked list class

#ifndef INT_SINGLY_LINKED_LIST
#DEFINE INT_SINGLY_LINKED_LIST

class IntSLLNode {
public:    
    IntSLLNode() {
        next = 0;
    }
    IntSLLNode(int i, IntSLLNode *in = 0) {
        info = i; next = in;
    }
    
    int info;
    IntSLLNode *next;
};

class IntSLList {
public:
    IntSLLNode() {
        head = tail = 0;
    }
    ~IntSLLNode();
    
    int isEmpty() {
        return head == 0;
    }
    
    void addToHead(int);
    void addToTail(int);
    int deleteFromHead();
    int deleteFromTail();
    void deleteNode(int);
    bool isInList(int) const;
    
private:
    IntSLLNode *head, *tail
};

#endif
