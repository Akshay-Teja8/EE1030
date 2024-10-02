#include<stdio.h>
#include<math.h>
int main(){
	double x,y;
	int points = 100;
	double step = 2.0/(points-1);
	for(int i=0;i<points;i++){
		x = -1 + i*step;
		y = x * fabs(x);
		printf("%.2f %.2f\n",x,y);
	}
}
