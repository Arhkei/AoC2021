#include <stdio.h>

int increaseFinder(int *dataset, size_t size){
    int previousDepth = dataset[0];
    int increase = 0;

    for(int i = 0; i < size; i++){
        if(dataset[i] > previousDepth)
            increase++;
        previousDepth = dataset[i];
    }
    
    return increase;
}

int main(){
    FILE *fptr = fopen("input.txt", "r");
    int data[2048];
    int counter = 0;
    
    while((fscanf(fptr, "%d", &data[counter++])) != EOF){
        continue;
    }
    fclose(fptr);

    int answer1 = increaseFinder(data, counter);
    printf("Increases: %d\n", answer1);

    int sumData[2048];
    for(int i = 0; i < counter; i++)
        if(i < counter - 2)
            sumData[i] = data[i] + data[i+1] + data[i+2];

    int answer2 = increaseFinder(sumData, counter);
    printf("Sum Increases: %d\n", answer2);
}
