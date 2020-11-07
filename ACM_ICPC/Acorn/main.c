#include <stdio.h>
#include <stdlib.h>

// ACM ICPC 4106

/* test case #1:
    input:
        3 10 2
        0 1 0 0 1 0 0 0 0 0 1
        0 0 0 1 0 1 0 1 1 2 0
        0 0 0 1 1 1 1 0 0 1 0
    output:
        8
*/

int max(int, int);
int corn(int, int, int, int**);

int main(){
    // get input
    int t, h, f;
    scanf("%d %d %d", &t, &h, &f);
    int **acorn = malloc((t)*sizeof(int*));
    for(int i=0; i<t; i++){
        acorn[i] = calloc(h+1, sizeof(int));
        for(int j=0; j<=h; j++){
            scanf("%d", &acorn[i][j]);
        }
    }

    //
    int res = corn(t, h, f, acorn);
    printf("%d", res);

    //
    for(int i=0; i<t; i++){
        free(acorn[i]);
    }
    free(acorn);

    return 0;
}

int max(int a, int b){
    return a>b?a:b;
}

int corn(int t, int h, int f, int **acorn){
    int **dp = malloc((t)*sizeof(int*));
    for(int i=0; i<t; i++){
        dp[i] = calloc(h+1,sizeof(int));
    }
    int *mem = calloc(h+1, sizeof(int));
    for(int j=1; j<=h; j++){
        for(int i=0; i<t; i++){
            dp[i][j] = acorn[i][j] + max(
                dp[i][j-1],
                j>=f?mem[j-f]:0
            );
            mem[j] = max(mem[j], dp[i][j]);
        }
    }

    //
    for(int i=0; i<t; i++){
        free(dp[i]);
    }
    free(dp);
    free(mem);

    return mem[h];
}
