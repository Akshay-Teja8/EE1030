#include<stdio.h>
#include<math.h>

int main(void){
	int N=100;
	double x_parabola[N];
	double y_parabola[N];
	double x_line[N];
	double y_line[N];
	double x_min=-2;
	double x_max=3;
	double step=(x_max-x_min)/N;
	double x_intersection[2]={2,-1},y_intersection[2]={1,0.25};
	printf("%lf %lf\n", x_intersection[0], y_intersection[0]);
        printf("%lf %lf\n", x_intersection[1], y_intersection[1]);
	for (int i = 0; i < N; i++) {
        double x = x_min + i * step;  
        x_parabola[i] = x;            
	y_parabola[i] = (x * x) / 4.0;  
    }

    for (int i = 0; i < N; i++) {
        double x = x_min + i * step; 
	x_line[i] = x;               
        y_line[i] = (x + 2) / 4.0;   
    }

       for (int i = 0; i < N; i++) {
        printf("%lf %lf %lf %lf\n", x_parabola[i], y_parabola[i], x_line[i], y_line[i]);
    }

    return 0;
}
