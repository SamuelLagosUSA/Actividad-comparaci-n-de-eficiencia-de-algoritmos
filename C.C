#include <stdio.h>
#include <time.h>
#include <sys/resource.h>

unsigned long long factorial_recursivo(int n) {
    if (n <= 1)
        return 1;
    return n * factorial_recursivo(n - 1);
}

unsigned long long factorial_iterativo(int n) {
    unsigned long long resultado = 1;
    for (int i = 2; i <= n; i++) {
        resultado *= i;
    }
    return resultado;
}

long memoria_kb() {
    struct rusage uso;
    getrusage(RUSAGE_SELF, &uso);
    return uso.ru_maxrss;
}

int main() {
    FILE *f = fopen("resultados.csv", "w");
    if (!f) {
        printf("Error al crear el archivo\n");
        return 1;
    }

    fprintf(f, "n,Resultado_Recursivo,Tiempo_Recursivo_seg,Memoria_Recursivo_KB,Resultado_Iterativo,Tiempo_Iterativo_seg,Memoria_Iterativo_KB\n");

    for (int n = 1; n <= 20; n++) {
        clock_t inicio_r = clock();
        unsigned long long res_r = factorial_recursivo(n);
        clock_t fin_r = clock();
        long mem_r = memoria_kb();
        double tiempo_r = (double)(fin_r - inicio_r) / CLOCKS_PER_SEC;

        clock_t inicio_i = clock();
        unsigned long long res_i = factorial_iterativo(n);
        clock_t fin_i = clock();
        long mem_i = memoria_kb();
        double tiempo_i = (double)(fin_i - inicio_i) / CLOCKS_PER_SEC;

        fprintf(f, "%d,%llu,%f,%ld,%llu,%f,%ld\n", n, res_r, tiempo_r, mem_r, res_i, tiempo_i, mem_i);
    }

    fclose(f);
    printf("Archivo 'resultados.csv' generado correctamente\n");
    return 0;
}
