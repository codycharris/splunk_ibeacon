/*
you could get rid of math.h if you replace pow.

I used gets and atof instead of scanf because I find it more reliable.

Hope this helps :)
*/


#include<stdio.h>
#include<stdlib.h>

#define pow(a,b) (a*a)

int main()
{
double xa, xb, xc;
double ya, yb, yc;
double ra, rb, rc;
double x, y;
double S, T;
double y1, y2;
char input[80];

xa = 0;
xb = 40;
xc = 40;
ya = 40;
yb = 40;
yc = 0;


printf("\nDistance to R1: ");
gets(input);
ra = atof(input);
printf("\nDistance to R2: ");
gets(input);
rb = atof(input);
printf("\nDistance to R3: ");
gets(input);
rc = atof(input);

printf("\nxa2: %f", pow(xa,2));
printf("\nxb2: %f", pow(xb,2));
printf("\nxc2: %f", pow(xc,2));

printf("\nya2: %f", pow(ya,2));
printf("\nyb2: %f", pow(yb,2));
printf("\nyc2: %f", pow(yc,2));


S = (pow(xc,2.) - pow(xb,2.) + pow(yc,2.) -
     pow(yb,2.) + pow(rb,2.) - pow(rc,2.)    ) / 2.0;
T = (pow(xa,2.) - pow(xb,2.) + pow(ya,2.) -
     pow(yb,2.) + pow(rb,2.) - pow(ra,2.)    ) / 2.0;

printf("\n((T*(xb-xc):%f) - (S*(xb-xa):%f)) / (((ya-yb)*(xb-xc):%f) - ((yc-yb)*(xb-xa):%f))", (xb-xc), (xb-xa) , (ya-yb)*(xb-xc), (yc-yb)*(xb-xa) );

y = ((T*(xb-xc)) - (S*(xb-xa))) /
    (((ya-yb)*(xb-xc)) - ((yc-yb)*(xb-xa)));

x = ((y*(ya-yb)) - T) / (xb-xa);

printf("\nPoint D: (%f,%f)\n", x, y);
return 0;
} /* main */