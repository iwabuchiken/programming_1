/************************************`
 * <Basics>
 *	1. File: sub1_p121_0to100.c
 *	2. Author: Iwabuchi Ken				*
 *	3. Date: 20120310_214838
 *	4. Dependencies:
 *		1)
 * <Aim>
 * 	1.
 * <Usage>
 *	1. Execute the program			*
 * <Source>
 * 	1. 
 * <Related>
 * 	1.
 * <Others>
 * <Description of the program>
 * 	1. 
 ************************************/

#ifndef INCLUDE_STDIO_H
#define INCLUDE_STDIO_H
#include <stdio.h>
#endif

#ifndef INCLUDE_STDLIB_H
#define INCLUDE_STDIO_H /* exit() */
#include <stdlib.h>
#endif

#ifndef INCLUDE_STRING_H
#define INCLUDE_STRING_H
#include <string.h>
#endif
#ifndef INCLUDE_TIME_H
#define INCLUDE_TIME_H
#include <time.h>
#endif

#ifndef INCLUDE_CTYPE_H
#define INCLUDE_CTYPE_H
#include <ctype.h>
#endif

#define show(dt, typ) \
			printf(#dt"=%"#typ"(%%"#typ")\n", dt)
#define show1(dt) \
			printf(#dt"\n")

/*
#include "mylib.h"
*/
#ifdef MYLIB
#ifndef INCLUDE_MYLIB_1_H
#define INCLUDE_MYLIB_1_H
#include "mylib.h"
#endif
#endif

// macros ============================

// global vars ============================
char    words[][15] = {
    /* 0 - 10 => 0 - 10   */
    "zero",
    "one", "two", "three", "four", "five",
    "six", "seven", "eight", "nine", "ten",
    /* 11 - 19 => 11 - 19  */
    "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    "sixteen", "seventeen", "eighteen", "nineteen",
    /* 20 - 90 => 20 - 27 */
    "twenty", "thirty", "forty", "fifty",
    "sixty", "seventy", "eighty", "ninety",
    /* 100 => 28        */
    "hundred"
};                  /* number words         */
enum NUMBERS {
    /* 0 - 10       */
    ZERO,
    ONE, TWO, THREE, FOUR, FIVE,
    SIX, SEVEN, EIGHT, NINE, TEN,
    /* 11 - 19      */
    ELEVEN, TWELVE, THIRTEEN, FOURTEEN, FIFTEEN,
    SIXTEEN, SEVENTEEN, EIGHTEEN, NINETEEN,
    /* 20 - 90      */
    TWENTY, THIRTY, FORTY, FIFTY,
    SIXTY, SEVENTY, EIGHTY, NINETY,
    /* 100          */
    HUNDRED    
} NUMBER;

// prototypes ============================
void conv_0_to_19(char line[]);
void conv_20_to_99(char line[]);
void conv_100(char line[]);
int input_number(char line[], int size);

// functions ============================

void conv_100(char line[])
{
    /* vars             */
    int     first;      /* third digit  */
    
    /* process
     */
    /* get the third digit into string  */
    first   = line[0] - '0';
    
    /* show in string    */
    printf("%s %s\n", words[first], words[28]);
    
}//void conv_100(char line[])

void conv_0_to_19(char line[])
{
    /* vars     */
    int     i;      /* index    */
    
    /* processes    */
    printf("%s\n", words[atoi(line)]);
    
/*
    for (i = 0; i < strlen(line); i++) {
        //printf("%s ", words[line[i] - '0' - 1]);
        printf("%s ", words[line[i] - '0']);
    }//for (i = 0; i < strlen(num); i++)

    printf("\n");
*/    
}//void conv_0_to_10(char line[])

void conv_20_to_99(char line[])
{
    /* vars         */
    int     first;      /* first digit      */
    int     second;     /* second digit      */
    int     second_index;   /* index for the second digit   */
    
    /* processes
     * 
     */
    /* digits into integers      */
    first   = line[1] - '0';
    second  = line[0] - '0';
    
    //debug
    //printf("second=%d first=%d\n", first, second);
    /* get index for the second     */
    second_index = 20 + (second - 2);
    
    /* show second digit as a string    */
    //printf("second=%s\n", words[second_index]);
    
    /* show the whole as a string       */
    printf("%s-%s\n", words[second_index], words[first]);
    
}//void conv_11_to_19(line)

int input_number(char line[], int size)
{
    while (1) {
        printf("Input a number (0 - 100 | -1 to quit): ");
        //fgets(line, sizeof(line), stdin);
        fgets(line, size, stdin);
        line[strlen(line) - 1] = '\0';
        if (is_digit(line)) {
            return 1;
        } else {//if (is_digit(line))
            printf("Input is not a number: %s\n", line);
        }//if (is_digit(line))
    }//while (1)
}//int input_number(char line[])

int main(int argc, char* argv[])
{
	/* variables	*/
    char    line[10];   /* entered number from stdin    */    
    int     i;         /* index                 */
    //char    num[] = "123";  /* number string    */

    //debug
/*
    i = 0;
    //while (words[i]) {
    while (i < 30) {
        printf("words[%d]=%s\n", i, words[i]);
        i ++;
    }//while (words[i])
*/

    //debug
/*
    char    s[]   = "-1";
    printf("%d\n", atoi(s));
    exit(0);
*/
    
    /* processes
     * 
     */
    /* get the input    */
    //input_number(line, sizeof(line));
/*
    while (1) {
        printf("Input a number (0 - 100): ");
        fgets(line, sizeof(line), stdin);
        line[strlen(line) - 1] = '\0';
        if (is_digit(line)) {
            break;
        } else {//if (is_digit(line))
            printf("Input is not a number: %s\n", line);
        }//if (is_digit(line))
    }//while (1)
*/

    /* convert to words     */
    while (1) {
        input_number(line, sizeof(line));
        if (atoi(line) == -1) {
            printf("Thank you for playing.\n");
            break;
        } else if (atoi(line) < 20) {
            /* 0 - 10       */
            conv_0_to_19(line);
        } else if (atoi(line) < 100) {
            /* 11*/
            conv_20_to_99(line);
        } else if (atoi(line) == 100) {
            conv_100(line);
        } else {//if (strlen(line) == 1)
            printf("Sorry. We can't handle this number: %s\n",
                        line);
        }//if (strlen(line) == 1)
    }//while (1)
    
/*
    for (i = 0; i < strlen(line); i++) {
        //printf("%s ", words[line[i] - '0' - 1]);
        printf("%s ", words[line[i] - '0']);
    }//for (i = 0; i < strlen(num); i++)
    printf("\n");
*/
    
	return (0);
}//int main(int argc, char* argv[])

/*
#ifdef D
    printf("[LINE:%d]", __LINE__);
#endif
 */
