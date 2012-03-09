#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
//#include "main_c.h"
//v=1.0
//created_at=20111027_043828
//project=C:\workspaces\ws_ubuntu_1\G20111027_043828_etc_1\main.c

int num[7] = {1,2,3,6,2,1,6};

// funcs ===============================
int get_index(int *array, int size, int value)
{
    int i; // counter
    int flag = -1; // flag: 1 if value found

    for (i = 0; i < size; i++) {
        if (array[i] == value) {
            //flag = value;
            flag = i;
            break;
        }
    }

    return flag;
}//int get_index(int *array, int value)

int get_second_max( int *num, int size, int *index, int limit )
{
    int max2 = 0;
    int i; // counter
    int flag = get_index(num, size, limit);
    *index = -1;
    //flag = get_index(num, size, limit);

    for (i = 0; i < size; i++) {
        //if (num[i] > limit) continue;
        //flag = get_index(num, size, limit);

        //if (num[i] >= limit && i == flag) continue;
        if (i == flag) continue;
        if (max2 < num[i]) {
            max2 = num[i]; *index = i;
        }
    }

    return max2;
}//int get_second_max( int *num, int size, int *index, int limit )

int get_max( int *num, int size, int *index )
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
}//int get_max( int *num, int size, int *index )

int main( int argc, char *argv[] )
{
    int max;
    int second_max;
    int index;
    int index2;

    max = get_max(num, sizeof(num)/sizeof(num[0]), &index);
    second_max = get_second_max(
            num, sizeof(num)/sizeof(num[0]), &index2, max);
    
    //debug
    printf("[%s:%d]", __FILE__, __LINE__);
    printf("max=%d(index=%d)\n", max, index);
    printf("second_max=%d(index=%d)\n", second_max, index2);

    return 0;
}

/*
#ifdef D
    printf("[%s:%d]", __FILE__, __LINE__);
#endif
*/
