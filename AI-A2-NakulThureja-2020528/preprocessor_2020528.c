#include <stdio.h>
#include <ctype.h>

int main()
{
    FILE *file1 = fopen("roaddistance.csv", "rt");
    FILE *file2 = fopen("capitalroaddistance.csv", "wt");

    int c;
    int skip = 0;
    int count = 0;
    int row = 0;
    while (EOF != (c = fgetc(file1))) {
        if(c == '\n'){
            skip++;
            if(count==0){
                c = fgetc(file1);
                while ((c=fgetc(file1))!=',');
                skip--; 
            }
            count++;
        }
        if(count>0){
            if(skip==0){
                if(c=='-'){
                    c = '0';
                }
                fputc(toupper(c), file2);
            }
            else{
                fseek(file2, -2, SEEK_CUR);
                if(row<47){
                    fputc('\n',file2);
                }
                if(row==47){
                    fputc(' ',file2);
                }
                row++;
                c = fgetc(file1);
                skip--;
            }
        }
    }
    fclose(file1);
    fclose(file2);
    return 0;
}