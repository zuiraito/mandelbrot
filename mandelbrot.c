#include <stdio.h>
#include <stdlib.h>
#include <complex.h>

int mandelbrot(long double x, long double y){
	double complex c = x + y*I;
	double complex z = 0;
	int n = 0;

	while (n<255){
		z=z*z+c;
		if (creal(z)*creal(z)+cimag(z)*cimag(z)>4){
			printf("%d %d %d ",255-n,255-n,255-n);
			return 0;}
		n++;

	}
	printf("0 0 0  ");
	return 0;
}



int main(int argc, char *argv[]) {
	
	double zoom = 400000000;
	int res = 500;

	float xin=-0.5581613309865028;
	float yin=-0.6370080199091355;

	if (argc==5){
		zoom = atof(argv[1]);
		res = atoi(argv[2]);
		xin = atof(argv[3]);
		yin = atof(argv[4]);}

	zoom = zoom*res;
	
	printf("P3\n%d %d\n255\n",res,res);

	for (int pixY = -res/2; pixY < res/2; pixY++){
	for (int pixX = -res/2; pixX < res/2; pixX++){
		long double x = pixX / zoom + xin;
		long double y = pixY / zoom + yin;
		mandelbrot(x,y);
	}
	printf("\n");}

	return 0;
}
