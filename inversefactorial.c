#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int pre_defined(int n)
{
    return n == 1 ? 1 : n == 2 ? 2 : n == 6 ? 3 : n == 24 ? 4 : n == 120 ? 5 : 6;
}

int main()
{
    char num[1000001];
    scanf("%s", num);
    size_t digits = strlen(num);

    if (digits < 4)
    {
        printf("%d\n", pre_defined(atoi(num)));
    }
    else
    {
        int number = 6;
        double log_sum = 4 * log10(2.0) + 2 * log10(3.0) + log10(5.0);
        while (1)
        {
            log_sum += log10(++number);
            if (log_sum > digits)
            {
                printf("%d\n", number - 1);
                break;
            }
        }
    }
    return 0;
}