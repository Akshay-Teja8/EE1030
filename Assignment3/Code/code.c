#include<stdio.h>

int main(){
	double P[]={-2,3,5},Q[]={1,2,3},R[]={7,0,-1};

	int numberOfValues=100;

	double x_values[numberOfValues],y_values[numberOfValues],z_values[numberOfValues];

	for(int i=0;i<numberOfValues;i++){
		double t=(double)i/numberOfValues;
		x_values[i]=P[0]+t*(Q[0]-P[0]);
		y_values[i]=P[1]+t*(Q[1]-P[1]);
		z_values[i]=P[2]+t*(Q[2]-P[2]);
	}
	   for (int i = 0; i < numberOfValues; i++) {
        printf("%.2f %.2f %.2f\n", x_values[i], y_values[i], z_values[i]);
    }

    return 0;
}
