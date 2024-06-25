// time gcc mandelbrot.c -o mandelbrot && time ./mandelbrot > mandelbrot.ppm && convert mandelbrot.ppm mandelbrot.jpeg && loupe mandelbrot.jpeg 


#include <stdio.h>
#include <stdlib.h>
#include <complex.h>

int mandelbrot(long res, long x, long y){
	float complex c = 3*((x-res/1.5) + (y-res/2) * I)/res;
	float complex z = 0;
	int n = 0;

	while (n<255){
		z=z*z+c;
		if (creal(z)*creal(z)+cimag(z)*cimag(z)>10000){
			printf("%d %d %d ",255-n,255-n,255-n);
			return 0;}
		n++;

	}
	printf("0 0 0  ");
	return 0;
}



int main(long argc, char *argv[]) {

	long res = atoi(argv[1]);
	long xstart = atoi(argv[2]);
	long xend = atoi(argv[3]);
	long ystart = atoi(argv[4]);
	long yend = atoi(argv[5]);

	printf("P3\n%d %d\n255\n",xend-xstart,yend-ystart);
	int y=ystart; int x;
	while (y<yend){x=xstart;
		while (x<xend){mandelbrot(res,x,y);x++;}
		printf("\n");y++;
	}
	return 0;
}
