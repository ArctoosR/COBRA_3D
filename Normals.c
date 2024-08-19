#include <stdio.h>

// تابع برای محاسبه نرمال صفحه
void calculateNormal(float p1[3], float p2[3], float p3[3], float normal[3]) {
    // محاسبه بردارهای u و v
    float u[3], v[3];
    u[0] = p2[0] - p1[0];
    u[1] = p2[1] - p1[1];
    u[2] = p2[2] - p1[2];

    v[0] = p3[0] - p1[0];
    v[1] = p3[1] - p1[1];
    v[2] = p3[2] - p1[2];

    // محاسبه حاصل‌ضرب برداری u و v
    normal[0] = u[1] * v[2] - u[2] * v[1];
    normal[1] = u[2] * v[0] - u[0] * v[2];
    normal[2] = u[0] * v[1] - u[1] * v[0];
}

int main(int argc, char *argv[]) {
    // سه نقطه روی صفحه 15,0,37, -15,0,37, 0,12,11
    float p2[3] = {59.0, -1.0, -3.0};
    float p3[3] = {43.0, 7.0, -19.0};
    float p1[3] = {63.0, -3.0, -19.0};

    // متغیری برای ذخیره نرمال صفحه
    float normal[3];

    // محاسبه نرمال
    calculateNormal(p1, p2, p3, normal);

    // چاپ نرمال
    printf("نرمال صفحه: (%.2f, %.2f, %.2f)\n", normal[0]/6.7, normal[1]/6.7, normal[2]/6.7);

    return 0;
}