#include<stdio.h>
#include<stdlib.h>

#define pow(a,b) (a*a)

int main()
{
double xa, xb, xc;
double ya, yb, yc;
double r1d, r2d, r3d;
double x, y;
double S, T;
double y1, y2;
char input[80];

xa = 0;
xb = 100;
xc = 100;
ya = 100;
yb = 100;
yc = 0;


printf("\nDistance to R1: ");
gets(input);
r1d = atof(input);
printf("\nDistance to R2: ");
gets(input);
r2d = atof(input);
printf("\nDistance to R3: ");
gets(input);
r3d = atof(input);

//x = (((-10000.0 + pow(r2d,2.) - pow(r3d,2.) ) / 2.0)*100)/10000;
//y = -((-10000.0  + pow(r2d ,2.) - pow(r1d, 2.) ) / 2.0)/100;  

x = -(((-1600.0 + pow(r2d,2.) - pow(r3d,2.) ) / 2.0)*40)/1600;
y = -((-1600.0 + pow(r2d ,2.) - pow(r1d, 2.) ) / 2.0)/40;  



// y = -(S*100) / 10000;
// x = -T / 100;

printf("\nPoint D: (%f,%f)\n", x, y);
return 0;
} /* main */