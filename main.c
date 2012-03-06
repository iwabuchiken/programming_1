#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
//#include "main_c.h"
//v=1.0
//created_at=20111027_043828
//project=C:\workspaces\ws_ubuntu_1\G20111027_043828_etc_1\main.c

void func1( void )
{
    char *p;
    p = malloc(sizeof(char)*20);
    strcpy(p, "abc");
    printf("p: %%s=%s %%p=%p &=%p\n",
                    p, p, &p);
    printf("p[1]: %%c=%c %%p=%p &=%p\n",
                    p[1], p[1], &p[1]);
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
