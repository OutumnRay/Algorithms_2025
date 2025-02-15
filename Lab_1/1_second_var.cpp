#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int compare(const void *a, const void *b) {
    double diff = (*(double *)a - *(double *)b);
    return (diff > 0) - (diff < 0);
}

void insertion_sort(double *our_mass, double *sorted_mass, int len, long long int *count_entering_the_array, long long int *count_exchange) {
    clock_t start_time = clock();
    
    // Подсчет операций
    for (int elem_id = 1; elem_id < len; elem_id++) {
        (*count_entering_the_array)++;
        double temp = our_mass[elem_id];
        int j = elem_id - 1;

        // Перемещаем элементы, которые больше текущего, на одну позицию вправо
        while (j >= 0 && our_mass[j] > temp) {
            (*count_exchange)++;
            our_mass[j + 1] = our_mass[j];
            j--;
        }
        our_mass[j + 1] = temp;
    }

    // Измерение времени выполнения
    clock_t finish_time = clock();
    double time_taken = ((double)(finish_time - start_time)) / CLOCKS_PER_SEC; // seconds

    // Запись результата в файл
    FILE *file = fopen("datas.txt", "a");
    if (file == NULL) {
        printf("Error opening file.\n");
    }

    fprintf(file, "%d Time taken: %f seconds, Entries: %lld, Exchanges: %lld\n", len, time_taken, *count_entering_the_array, *count_exchange);

    fclose(file);

    printf("%d Time taken: %f seconds, Entries: %lld, Exchanges: %lld\n", len, time_taken, *count_entering_the_array, *count_exchange);
}

int main() {
    int dimensions[] = {1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000};
    int dimensions_count = sizeof(dimensions) / sizeof(dimensions[0]);
    
    for (int i = 0; i < dimensions_count; i++) {
        int dimension = dimensions[i];
        for (int approach = 0; approach < 20; approach++) {
            double *mass = (double *)malloc(dimension * sizeof(double));
            double *tmp = (double *)malloc(dimension * sizeof(double));

            // Генерация случайных чисел
            for (int j = 0; j < dimension; j++) {
                mass[j] = (double)rand() / RAND_MAX * 2.0 - 1.0;  // Случайное число от -1 до 1
                tmp[j] = mass[j];
            }

            // Сортировка массива tmp для сравнения
            qsort(tmp, dimension, sizeof(double), compare);

            long long int count_entering_the_array = 0, count_exchange = 0;
            insertion_sort(mass, tmp, dimension, &count_entering_the_array, &count_exchange);

            free(mass);
            free(tmp);
        }
    }

    return 0;
}
