#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
//#include "main_c.h"
//v=1.0
//created_at=20111027_043828
//project=C:\workspaces\ws_ubuntu_1\G20111027_043828_etc_1\main.c

int num[6] = {1,2,3,2,1,6};

int func1( int *num, int size, int *index )
{
    int max = 0;
    int i; // counter
    *index = -1;

/*
    printf("sizeof(num)/sizeof(num[0])=%d\n",
                sizeof(num)/sizeof(num[0]));
*/
    for (i = 0; i < size; i++) {
        if (max < num[i]) {
            max = num[i]; *index = i;
        }
    }

    //printf("max=%d(index=%d)\n", max, *index);

    return max;
}

int main( int argc, char *argv[] )
{
    int max;
    int index;

    max = func1(num, sizeof(num)/sizeof(num[0]), &index);
    
    //debug
    printf("[%s:%d]", __FILE__, __LINE__);
    printf("max=%d(index=%d)\n", max, index);

    return 0;
}

/*
#ifdef D
    printf("[%s:%d]", __FILE__, __LINE__);
#endif
*/
