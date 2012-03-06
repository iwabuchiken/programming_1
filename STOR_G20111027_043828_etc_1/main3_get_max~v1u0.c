#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
//#include "main_c.h"
//v=1.0
//created_at=20111027_043828
//project=C:\workspaces\ws_ubuntu_1\G20111027_043828_etc_1\main.c

int num[6] = {1,2,3,2,1,6};

void func1( void )
{
    int current;
    int max = 0;
    int i; // counter
    int index = -1;

    //printf("strlen(num)=%d\n", strlen(num));
    //printf("sizeof(num)=%d\n", sizeof(num)/sizeof(num[0]));

    //for (i = 0; i < strlen(num); i++) {
    for (i = 0; i < sizeof(num)/sizeof(num[0]); i++) {
        if (max < num[i]) {
            max = num[i]; index = i;
        }
    }

    printf("max=%d(index=%d)\n", max, index);
}

int main( int argc, char *argv[] )
{
    func1();
    return 0;
}

/*
#ifdef D
    printf("[LINE:%d]", __LINE__);
#endif
*/
