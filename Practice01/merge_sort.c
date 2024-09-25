#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void c_merge(int h, int m, int U[], int V[], int S[]) {
    int i = 1, j = 1, k = 1;

    while (i <= h && j <= m) {
        if (U[i] < V[j]) {
            S[k] = U[i];
            i++;
        } else {
            S[k] = V[j];
            j++;
        }
        k++;
    }

    if (i > h) {
        // V[j]부터 V[m]까지를 S[k]부터 S[h+m]까지 복사
        for (int index = j; index <= m; index++) {
            S[k + (index - j)] = V[index];
        }
    } else {
        // U[i]부터 U[h]까지를 S[k]부터 S[h+m]까지 복사
        for (int index = i; index <= h; index++) {
            S[k + (index - i)] = U[index];
        }
    }
}

void c_mergesort(int n, int S[]) {
    if (n > 1) {
        int h = n / 2;
        int m = n - h;
        int U[h + 1], V[m + 1];

        // U 배열에 S의 첫 번째 절반 복사
        for (int index = 1; index <= h; index++) {
            U[index] = S[index];
        }

        // V 배열에 S의 두 번째 절반 복사
        for (int index = 1; index <= m; index++) {
            V[index] = S[h + index];
        }

        // 병합 정렬 재귀 호출
        c_mergesort(h, U);
        c_mergesort(m, V);

        // 병합 과정
        c_merge(h, m, U, V, S);
    }
}

// 삽입 정렬
void insertion_sort(int n, int list[]){
  int i, j, key;

  // 인텍스 0은 이미 정렬된 것으로 볼 수 있다.
  for(i=1; i<n; i++){
    key = list[i]; // 현재 삽입될 숫자인 i번째 정수를 key 변수로 복사

    // 현재 정렬된 배열은 i-1까지이므로 i-1번째부터 역순으로 조사한다.
    // j 값은 음수가 아니어야 되고
    // key 값보다 정렬된 배열에 있는 값이 크면 j번째를 j+1번째로 이동
    for(j=i-1; j>=0 && list[j]>key; j--){
      list[j+1] = list[j]; // 레코드의 오른쪽으로 이동
    }

    list[j+1] = key;
  }
}

int main() {
    int n = 50000;  // 정렬할 정수의 개수
    int S[n + 1];   // 1부터 시작하는 인덱스를 사용하기 위해 배열 크기를 n+1로 설정

    // 난수 생성을 위한 시드 설정
    srand(time(NULL));

    // 1부터 n까지의 배열에 랜덤 정수 삽입 (1부터 10000 사이의 값)
    for (int i = 1; i <= n; i++) {
        S[i] = rand() % 10000 + 1;  // 1부터 10000 사이의 난수 생성
    }

    // 정렬 시작 시간 기록
    clock_t start = clock();

    // 정렬 실행
    c_mergesort(n, S);

    // 정렬 종료 시간 기록
    clock_t end = clock();

    // 실행 시간 계산
    double duration = (double)(end - start) / CLOCKS_PER_SEC;
    printf("시간: %f seconds\n", duration);

    // // 정렬된 결과 출력 (부분적으로 출력)
    // for (int i = 1; i <= n; i++) {
    //     printf("%d \n", S[i]);
    // }
    time_t start_time, end_time;

    // 현재 시간 기록 (초 단위)
    start_time = clock();

    // 삽입 정렬
    insertion_sort(n, S);

    // 끝난 시간 기록 (초 단위)
    end_time = clock();
    double time = (double)(end_time - start_time) / CLOCKS_PER_SEC;
    printf("시간: %f seconds\n", time);

    // divide back_tracking 
    
    return 0;
}