#include <stdio.h>
#define INT_MAX 999
#define vertices 6

int parent[vertices], distance[vertices];

int cost[vertices][vertices] = {{0, 1, 5, 0, 0, 0},
        {0, 0, 2, 2, 1, 0},
        {0, 0, 0, 0, 2, 0},
        {0, 0, 0, 0, 3, 1},
        {0, 0, 0, 0, 0, 2},
        {0, 0, 0, 0, 0, 0}};

void initializeGraph(){
    for(int i=0; i<vertices; i++){
        for(int j=0; j<vertices; j++){
            if(cost[i][j] == 0 && i!=j){
                cost[i][j] = INT_MAX;
            }
        }
    }
}

void initializeSingleSource(int source){
    initializeGraph();
    for(int i=0; i<vertices; i++){
        distance[i] = INT_MAX;
        parent[i] = -1;
    }
    distance[source] = 0;
}

void Relax(int u, int v){
    if(distance[u] + cost[u][v] < distance[v]){
        printf("%d is relxing vertex %d\n", u,v);
        distance[v] = distance[u] + cost[u][v];
        parent[v] = u;
    }
}

int BellmenFord(int source){    
    initializeSingleSource(source);
    for(int k=0; k<vertices; k++){
        for(int u=0; u<vertices; u++){
            for(int v=0; v<vertices; v++){
                if(cost[u][v]!=INT_MAX && u!=v){
                    Relax(u, v);
                }
            }
        }
    }
    for(int u=0; u<vertices; u++){
        for(int v=0; v<vertices; v++){
            if(cost[u][v]!=INT_MAX && u!=v){
                if(distance[u] + cost[u][v] < distance[v]){
                    return 0;
                }
            }
        }
    }
    return 1;
}

void printSol(){
    printf("\nNode\tDistance\tParent\n");
    for (int i=0; i<vertices; i++){
        printf("%d\t\t%d\t\t%d\n", i, distance[i], parent[i]);
    }
}

void main(){
    int source;
    printf("Enter the source vertex : ");
    scanf("%d", &source);
    int x = BellmenFord(source);
    if(x!=0){
        printSol();
    }
    else{
        printf("\nNO SOLUTION !!, The Graph has negative weight cycle\n");
    }
}