#include <stdio.h>
#define INT_MAX 999
#define vertices 6

int visited[vertices], parent[vertices], distance[vertices];

int cost[vertices][vertices] = {{0, 1, 5, 0, 0, 0},
        {0, 0, 2, 2, 1, 0},
        {0, 0, 0, 0, 2, 0},
        {0, 0, 0, 0, 3, 1},
        {0, 0, 0, 0, 0, 2},
        {0, 0, 0, 0, 0, 0}};

int isToExplore(){
    for(int i=0; i<vertices; i++){
        if (visited[i] == 0){
            return 1;
        }
    }
    return 0;
}

void initializeGraph(){
    for(int i=0; i<vertices; i++){
        for(int j=0; j<vertices; j++){
            if (i != j && cost[i][j] == 0){
                cost[i][j] = INT_MAX;
            }
        }
    }
}

void initializeSingleSource(int source){
    initializeGraph();
    for(int i=0; i<vertices; i++){
        parent[i] = -1;
        visited[i] = 0;
        distance[i] = INT_MAX;
    }
    distance[source] = 0;
}

int getMinNode(){
    int min;
    for(int i=0; i<vertices; i++){
        if(visited[i] != 1 && distance[i] != INT_MAX){
            min = i;
        }
    }
    for (int i=min; i<vertices; i++){
        if(visited[i] != 1 && distance[i]<distance[min]){
            min = i;
        }
    }
    return min;
}

void Relax(int u, int v){
    if((distance[u] + cost[u][v]) < distance[v]){
        distance[v] = distance[u] + cost[u][v];
        parent[v] = u;
    }
    printf("u : %d v : %d parent : %d distance : %d\n", u,v, parent[v], distance[v]);
}

void Dijkstra(int source){
    initializeSingleSource(source);
    printf("\n");
    while(isToExplore()){
        int u = getMinNode();
        for(int v=0; v<vertices; v++){
            if(cost[u][v] != INT_MAX && u != v){
                Relax(u,v);
            }
        }
        visited[u] = 1;
    }
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
    scanf("%d",&source);
    Dijkstra(source);
    printSol();
}