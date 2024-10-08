# COBRA_3D
HELP
برای استفاده از قابلیت visible edges در کد خود به منظور نمایش لبه‌های قابل مشاهده و همچنین استفاده از زاویه دید، می‌توانید مراحل زیر را دنبال کنید:

محاسبه لبه‌های قابل مشاهده:
ابتدا باید لبه‌های قابل مشاهده را بر اساس زاویه دید محاسبه کنید. این کار معمولاً با استفاده از الگوریتم‌های تعیین سطح پنهان (Hidden Surface Determination) انجام می‌شود. در کد شما، این کار با محاسبه مساحت وجه انجام می‌شود. اگر مساحت مثبت باشد، وجه به سمت دوربین است و لبه‌های آن قابل مشاهده هستند.
ذخیره‌سازی لبه‌های قابل مشاهده:
لبه‌های قابل مشاهده را در آرایه visible_edges ذخیره کنید. این کار در کد شما با استفاده از عملیات بیتی انجام می‌شود. برای هر وجه، اگر قابل مشاهده باشد، لبه‌های آن به visible_edges اضافه می‌شوند.
رسم لبه‌های قابل مشاهده:
در نهایت، لبه‌های قابل مشاهده را رسم کنید. این کار با استفاده از توابع رسم گرافیکی انجام می‌شود. در کد شما، این کار با استفاده از تابع po.draw() انجام می‌شود.
در اینجا یک مثال ساده از نحوه استفاده از این قابلیت‌ها آورده شده است:
void draw_faces() {
  memset(visible_edges, 0, sizeof(visible_edges));

  const PROGMEM uint8_t *p = COBRA_faces;
  byte n;
  Poly po;
  while ((n = pgm_read_byte_near(p++)) != 0xff) {
    int8_t nx = pgm_read_byte_near(p++);
    int8_t ny = pgm_read_byte_near(p++);
    int8_t nz = pgm_read_byte_near(p++);
    byte face_edges[EDGE_BYTES];
    for (byte i = 0; i < EDGE_BYTES; i++)
      face_edges[i] = pgm_read_byte_near(p++);
    byte v1 = pgm_read_byte_near(p);
    byte v2 = pgm_read_byte_near(p + 1);
    byte v3 = pgm_read_byte_near(p + 2);
    long x1 = projected[v1].x;
    long y1 = projected[v1].y;
    long x2 = projected[v2].x;
    long y2 = projected[v2].y;
    long x3 = projected[v3].x;
    long y3 = projected[v3].y;
    long area = (x1 - x3) * (y2 - y1) - (x1 - x2) * (y3 - y1);

    if (area > 0) {
      for (byte i = 0; i < EDGE_BYTES; i++)
        visible_edges[i] |= face_edges[i];
      po.begin();
      for (int i = 0; i < n; i++) {
        byte vi = pgm_read_byte_near(p++);
        xyz *v = &projected[vi];
        po.v(v->x, v->y);
      }
      // محاسبه نور و رنگ
      transform_normal(nx, ny, nz);
      uint16_t r = 10, g = 10, b = 20;  // نور محیطی
      int d = -ny;                      // نور پخش شده از +Y
      if (d > 0) {
        r += d >> 2;
        g += d >> 1;
        b += d;
      }
      d = ny * -90 + nz * -90;          // نور بازتابی
      if (d > 8192) {
        byte l = pgm_read_byte_near(shiny + ((d - 8192) >> 4));
        r += l;
        g += l;
        b += l;
      }
      GD.ColorRGB(fmin(255, r), fmin(255, g), fmin(255, b));
      po.draw();
    } else {
      p += n;
    }
  }
}


در این مثال، لبه‌های قابل مشاهده بر اساس زاویه دید محاسبه و ذخیره می‌شوند و سپس رسم می‌شوند. همچنین، نور و رنگ برای هر وجه محاسبه می‌شود تا جلوه‌های بصری بهتری ایجاد شود

بیایید ساختار آرایه COBRA_faces را با جزئیات بیشتری بررسی کنیم و نام‌گذاری کنیم تا وظایف هر عضو مشخص شود. در اینجا یک نمونه از آرایه آورده شده است:

static const PROGMEM uint8_t COBRA_faces[] = {
  3, 0, 115, 53, 7, 0, 0, 0, 0, 2, 0, 1,
  3, -36, 117, 32, 28, 0, 0, 0, 0, 2, 1, 5,
  // ...
  -1
};

هر خط از این آرایه شامل اطلاعات مربوط به یک وجه (Face) است. بیایید هر بخش را نام‌گذاری کنیم:

تعداد رئوس (Vertices Count):
اولین عدد در هر خط نشان‌دهنده تعداد رئوس وجه است. در این مثال، 3 به معنای سه راس است.
مختصات نرمال (Normal Coordinates):
سه عدد بعدی مختصات نرمال وجه هستند. این مختصات جهت نرمال وجه را مشخص می‌کنند. در این مثال، 0, 115, 53 مختصات نرمال هستند.
بایت‌های لبه (Edge Bytes):
پنج عدد بعدی بایت‌های لبه هستند که اطلاعات مربوط به لبه‌های وجه را ذخیره می‌کنند. این بایت‌ها برای تعیین لبه‌های قابل مشاهده استفاده می‌شوند. در این مثال، 7, 0, 0, 0, 0 بایت‌های لبه هستند.
اندیس‌های رئوس (Vertex Indices):
بقیه اعداد در هر خط اندیس‌های رئوس هستند که به آرایه projected اشاره می‌کنند. این اندیس‌ها مختصات رئوس وجه را مشخص می‌کنند. در این مثال، 2, 0, 1 اندیس‌های رئوس هستند.
بنابراین، ساختار هر خط به صورت زیر است:

[تعداد رئوس] [مختصات نرمال x, y, z] [بایت‌های لبه] [اندیس‌های رئوس]

//*************************************************************
عملکرد تابع
ورودی‌های تابع:

nx, ny, nz: نرمال‌های سطحی به صورت int8_t (اعداد صحیح 8 بیتی) که به عنوان پارامترهای مرجع (reference) وارد تابع می‌شوند.
عملیات درون تابع:

تابع با استفاده از ماتریس normal_mat (ماتریس نرمال‌ها) که قبلاً تعریف شده است، نرمال‌های ورودی را به روز می‌کند.
نرمال‌های جدید به دست آمده از ترکیب نرمال‌های ورودی با ماتریس نرمال‌ها محاسبه می‌شوند.
ماتریس نرمال‌ها (normal_mat):

normal_mat یک ماتریس ۳x۳ است که برای تبدیل نرمال‌ها در نظر گرفته شده است. این ماتریس معمولاً شامل اطلاعاتی است که نرمال‌های سه‌بعدی را به فضای جدیدی که در آن پردازش نور انجام می‌شود، تبدیل می‌کند.
عملیات ریاضی:

نرمال‌های جدید (xx, yy, zz) با استفاده از ضرب ماتریسی محاسبه می‌شوند.
نتیجه درون متغیرهای nx, ny, nz قرار می‌گیرد، به طوری که این مقادیر به روز شده و نرمال‌های جدید در دسترس خواهند بود.
دلیل استفاده از transform_normal
هدف از استفاده از تابع transform_normal این است که نرمال‌ها مطابق با تغییرات مدل (مدل ماتریس) و دیگر تبدیل‌ها به روز رسانی شوند. این امر برای اطمینان از اینکه محاسبات نورپردازی و سایه‌ها به درستی و با توجه به تغییرات هندسی مدل، انجام شود، ضروری است.

بدون تبدیل صحیح نرمال‌ها، نتایج نورپردازی می‌تواند نادرست باشد و تاثیرات نور در سطح‌های مختلف مدل به درستی محاسبه نشود.

ارتباط بایت‌های لبه با visible_edges
بایت‌های لبه (Edge Bytes) ارتباط مستقیمی با visible_edges دارند. این بایت‌ها برای ذخیره‌سازی اطلاعات مربوط به لبه‌های هر وجه استفاده می‌شوند. در کد شما، اگر مساحت وجه مثبت باشد (یعنی وجه به سمت دوربین است)، بایت‌های لبه آن وجه به visible_edges اضافه می‌شوند. این فرآیند به منظور تعیین لبه‌هایی که باید رسم شوند و لبه‌هایی که باید پنهان بمانند، انجام می‌شود.


//****************************************************************

نرمال‌های سطحی (surface normals) در گرافیک سه‌بعدی برای محاسبه درست نورپردازی و سایه‌زنی مورد استفاده قرار می‌گیرند. در این کد، نرمال‌های هر صفحه (یا وجه) از یک مدل سه‌بعدی معمولاً با استفاده از مختصات رئوس آن صفحه محاسبه می‌شوند. در اینجا، نحوه محاسبه نرمال‌های صفحات به طور کلی توضیح داده می‌شود:

محاسبه نرمال‌های صفحات
برای محاسبه نرمال یک صفحه (مثلث)، معمولاً از محصول برداری (cross product) استفاده می‌شود. نرمال یک صفحه به صورت یک بردار عمود بر صفحه تعریف می‌شود و با استفاده از رئوس صفحه محاسبه می‌شود.

مراحل محاسبه نرمال یک صفحه
محاسبه بردارهای دو ضلع از مثلث:
برای محاسبه نرمال، ابتدا باید دو بردار از رئوس مثلث را محاسبه کنیم. فرض کنید رئوس مثلث به صورت 
𝑉
1
(
𝑥
1
,
𝑦
1
,
𝑧
1
)
V1(x1,y1,z1)، 
𝑉
2
(
𝑥
2
,
𝑦
2
,
𝑧
2
)
V2(x2,y2,z2)، و 
𝑉
3
(
𝑥
3
,
𝑦
3
,
𝑧
3
)
V3(x3,y3,z3) داده شده‌اند. بردارهای دو ضلع را می‌توان به صورت زیر محاسبه کرد:

بردار 
𝐴
A از 
𝑉
1
V1 به 
𝑉
2
V2:
𝐴
=
(
𝑥
2
−
𝑥
1
,
𝑦
2
−
𝑦
1
,
𝑧
2
−
𝑧
1
)
A=(x2−x1,y2−y1,z2−z1)
بردار 
𝐵
B از 
𝑉
1
V1 به 
𝑉
3
V3:
𝐵
=
(
𝑥
3
−
𝑥
1
,
𝑦
3
−
𝑦
1
,
𝑧
3
−
𝑧
1
)
B=(x3−x1,y3−y1,z3−z1)
محاسبه محصول برداری (Cross Product):
نرمال صفحه با استفاده از محصول برداری این دو بردار محاسبه می‌شود:

𝑁
=
𝐴
×
𝐵
N=A×B
که به صورت زیر محاسبه می‌شود:

𝑁
𝑥
=
(
𝐴
𝑦
⋅
𝐵
𝑧
)
−
(
𝐴
𝑧
⋅
𝐵
𝑦
)
N 
x
​
 =(A 
y
​
 ⋅B 
z
​
 )−(A 
z
​
 ⋅B 
y
​
 )

𝑁
𝑦
=
(
𝐴
𝑧
⋅
𝐵
𝑥
)
−
(
𝐴
𝑥
⋅
𝐵
𝑧
)
N 
y
​
 =(A 
z
​
 ⋅B 
x
​
 )−(A 
x
​
 ⋅B 
z
​
 )

𝑁
𝑧
=
(
𝐴
𝑥
⋅
𝐵
𝑦
)
−
(
𝐴
𝑦
⋅
𝐵
𝑥
)
N 
z
​
 =(A 
x
​
 ⋅B 
y
​
 )−(A 
y
​
 ⋅B 
x
​
 )
نرمال‌سازی نرمال:
معمولاً نرمال‌ها باید نرمال‌سازی شوند تا واحد باشند. این کار با تقسیم نرمال‌ها بر طول آن‌ها (مقدار آن) انجام می‌شود:

Length
=
𝑁
𝑥
2
+
𝑁
𝑦
2
+
𝑁
𝑧
2
Length= 
N 
x
2
​
 +N 
y
2
​
 +N 
z
2
​
 
​
 

𝑁
𝑥
′
=
𝑁
𝑥
Length
N 
x
′
​
 = 
Length
N 
x
​
 
​
 

𝑁
𝑦
′
=
𝑁
𝑦
Length
N 
y
′
​
 = 
Length
N 
y
​
 
​
 

𝑁
𝑧
′
=
𝑁
𝑧
Length
N 
z
′
​
 = 
Length
N 
z
​
 
​
 
پیاده‌سازی در کد
در کد شما، نرمال‌ها برای هر صفحه در قالب داده‌های ذخیره‌شده در حافظه برنامه (PROGMEM) موجود است و از قبل محاسبه شده‌اند. این نرمال‌ها در تابع draw_faces() برای محاسبه روشنایی و رنگ صفحه مورد استفاده قرار می‌گیرند.

مثال ساده از محاسبه نرمال
برای یک مثلث با رئوس (1, 0, 0)، (0, 1, 0)، و (0, 0, 1)، مراحل به صورت زیر است:

بردارهای ضلع:

𝐴
=
(
0
−
1
,
1
−
0
,
0
−
0
)
=
(
−
1
,
1
,
0
)
A=(0−1,1−0,0−0)=(−1,1,0)

𝐵
=
(
0
−
1
,
0
−
0
,
1
−
0
)
=
(
−
1
,
0
,
1
)
B=(0−1,0−0,1−0)=(−1,0,1)
محصول برداری:

𝑁
𝑥
=
(
1
⋅
1
)
−
(
0
⋅
0
)
=
1
N 
x
​
 =(1⋅1)−(0⋅0)=1

𝑁
𝑦
=
(
0
⋅
(
−
1
)
)
−
(
1
⋅
1
)
=
−
1
N 
y
​
 =(0⋅(−1))−(1⋅1)=−1

𝑁
𝑧
=
(
(
−
1
)
⋅
0
)
−
(
1
⋅
(
−
1
)
)
=
1
N 
z
​
 =((−1)⋅0)−(1⋅(−1))=1
نرمال غیر نرمالیزه: (1, -1, 1)

نرمال‌سازی:

Length
=
1
2
+
(
−
1
)
2
+
1
2
=
3
Length= 
1 
2
 +(−1) 
2
 +1 
2
 
​
 = 
3
​
 

𝑁
𝑥
′
=
1
3
,
𝑁
𝑦
′
=
−
1
3
,
𝑁
𝑧
′
=
1
3
N 
x
′
​
 = 
3
​
 
1
​
 ,N 
y
′
​
 = 
3
​
 
−1
​
 ,N 
z
′
​
 = 
3
​
 
1
​
 
این نرمال‌ها سپس می‌توانند برای محاسبه نورپردازی استفاده شوند.




