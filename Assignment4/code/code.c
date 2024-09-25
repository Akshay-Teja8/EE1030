#include<stdio.h>
int main(){
    double i;
    int A=1,B=1;
    int direction_vector[2]={A,B};
    int normal_vector[2]={-B,A};
    printf("%d %d\n%d %d\n",direction_vector[0],direction_vector[1],normal_vector[0],normal_vector[1]);
    for ( i=-1;i<=1;i+=0.01){
        printf("%.2lf %.2lf\n",i,i);
    } 
}
