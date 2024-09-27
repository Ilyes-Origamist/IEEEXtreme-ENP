// Challenge Link:
// https://csacademy.com/prextreme18/task/xor-game/

// Solved using segment tree
// PreXtreme 18.0, 2024

#include <iostream>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

// modified code taken from CS Academy Lessons
// https://csacademy.com/lesson/segment_trees

vector<int> segm_tree, arr;

int operation(int n1, int n2){
    // our operation here is bitwise XOR
    return n1 ^ n2;
}

// computes the parent of the two sons
// having the indices 2*node+1 and 2*node+2
void recalculate(int node) {
    //calculate the solution for the current segment,
    //considering the sons are correctly solved
    // node represents the index on the tree, 
    // while segm_tree[node] its value.
    segm_tree[node] = operation(segm_tree[2 * node + 1], segm_tree[2 * node + 2]);
}

// build the tree from an array
void build(int node, int left, int right) { //"node" is the index in the array, while "left"
                                            // and "right" are the ends of the current segment
    if (left == right) {
        segm_tree[node] = arr[left]; //we are in a leaf node
    } else {
        int middle = (left + right) / 2;
        build(2 * node + 1, left, middle);
        build(2 * node + 2, middle + 1, right);
        recalculate(node);
    }
}

// update an element "x" by the new lement "y" from query
void update(int node, int left, int right, int x, int y) {
    if (left == right) { //we are in the xth leaf
        segm_tree[node] = y;
    } else {
        int middle = (left + right) / 2;
        if (x <= middle) { //we need to update the left son
            update(2 * node + 1, left, middle, x, y);
        } else {
            update(2 * node + 2, middle + 1, right, x, y);
        }
        //after updating said son, recalculate the current segment
        recalculate(node);
    }
}

// computes the result of the operation on a segment [x,y]
int query(int node, int left, int right, int x, int y) {
    if (x <= left && right <= y) {
        //the segment of "node" is completely included in the query
        return segm_tree[node];
    } else {
        // initial value according to the operation
        int answer = 0;
        int middle = (left + right) / 2;
        if (x <= middle) {
            //the query segment and the left son segment have at least one element in common
            answer = operation(answer, query(2 * node + 1, left, middle, x, y));
        }
        if (y >= middle + 1) {
            //the query segment and the right son segment have at least one element in common
            answer = operation(answer, query(2 * node + 2, middle + 1, right, x, y));
        }
        //we would not have entered this function if (x, y) and (left, right) had nothing in common,
        //so there is no risk of answer returning -Infinity here, as either the left or the right son
        //would update it
        return answer;
    }
}

int main() {
    int N, Q;
    int a, b;
    cin >> N >> Q;
    arr.resize(N);
    segm_tree.resize(2*N);
    // initialize the array
    for (int i=0; i<N; i++){
        cin >> arr[i];
    }
    // build the tree
    build(0, 0, N-1);
    // queries
    for (int q=1; q<=Q; q++){
        cin >> a >> b;
        cout << query(0,0,N-1,a-1,b-1) << endl;
    }
    return 0;
}
