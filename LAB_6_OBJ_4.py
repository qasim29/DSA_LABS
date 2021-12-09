# include <stdio.h>
# include <conio.h>
#include<iostream>
#include <sys/time.h>
#include<stdlib.h>
using namespace std;

int front = -1;
int rear = -1;

void enqueue(int x ,int size, int* queue){
	if(front ==-1 && rear == -1){
		front = front +1;
		rear = rear + 1;
		queue[rear] = x;
	
	}else if(rear != -1 && rear < size ){
		rear = rear + 1;
		queue[rear] = x;
	}
	else{
		printf("Queue is overflow");	
	}
}

int dequeue(int* queue){
	if(front ==-1 && rear == -1){
		printf("Queue is empty..");
	}
	else if(front == rear){
		int dequeueElement = queue[rear];
		rear = front = -1;
		return dequeueElement;
	}else{
		int dequeueElement = queue[front];
		front = front + 1;
		return dequeueElement;
	}	
}

int peek(int* queue){
	if(front ==-1 && rear == -1){
		printf("Queue is empty..");
	}else{
		return queue[front];
	}
}

bool isFull(int size, int* queue){
	if(rear == size){
		return true;
	}else{
		return false;
	}
}

bool isEmpty(int* queue){
	if(front ==-1 && rear == -1){
		return true;
	}else{
		return false;
	}
}
int main(){
	int n,m;
    printf("Enter the size of queue:");
    scanf("%d",&n);
   	printf("Enter the number for repeating the process of enqueue and dequeue:");
	scanf("%d",&m) ; 
	int* queue = new  int (n);
	struct timespec start, end;    
	clock_gettime(CLOCK_MONOTONIC, &start);
	for (int c = 0 ; c < m ; c++){
		for (int i = 0 ; i < n ; i++){
		enqueue(rand()%100 , n , queue);	
		}
	
		for (int i = 0 ; i < n ; i++){
			printf("%d  ",dequeue(queue));	
		}
		printf("\n");
	}
	
	clock_gettime(CLOCK_MONOTONIC, &end);
  
    // Calculating total time taken by the program.
    double time_taken;
    time_taken = end.tv_sec - start.tv_sec; 
    time_taken = (time_taken + (end.tv_nsec - start.tv_nsec) * 1e-9);
    
    printf("\nTime measured: %.7f seconds.\n", time_taken);		
	return 0;
}