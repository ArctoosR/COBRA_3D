import bpy
import math

# تابع برای ایجاد یک ستاره پنج‌پر
def create_star(radius1, radius2, depth):
    verts = []
    faces = []

    angle = math.pi / 5
    for i in range(10):
        r = radius1 if i % 2 == 0 else radius2
        x = r * math.cos(i * angle)
        y = r * math.sin(i * angle)
        verts.append((x, y, 0))

    verts.append((0, 0, depth))

    for i in range(10):
        faces.append((i, (i + 1) % 10, 10))

    mesh = bpy.data.meshes.new(name="Star")
    mesh.from_pydata(verts, [], faces)
    obj = bpy.data.objects.new(name="Star", object_data=mesh)
    bpy.context.collection.objects.link(obj)

# پارامترهای ستاره
radius1 = 1.0
radius2 = 0.5
depth = 0.2

# ایجاد ستاره
create_star(radius1, radius2, depth)



///********************************************__ستاره تو پر___*******************************************************


import bpy
import math

# تابع برای ایجاد یک ستاره پنج‌پر
def create_solid_star(radius1, radius2, depth):
    verts = []
    faces = []

    angle = math.pi / 5
    for i in range(10):
        r = radius1 if i % 2 == 0 else radius2
        x = r * math.cos(i * angle)
        y = r * math.sin(i * angle)
        verts.append((x, y, 0))

    for i in range(10):
        verts.append((verts[i][0], verts[i][1], depth))

    for i in range(10):
        faces.append((i, (i + 1) % 10, (i + 1) % 10 + 10, i + 10))

    faces.append((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    faces.append((10, 11, 12, 13, 14, 15, 16, 17, 18, 19))

    mesh = bpy.data.meshes.new(name="SolidStar")
    mesh.from_pydata(verts, [], faces)
    obj = bpy.data.objects.new(name="SolidStar", object_data=mesh)
    bpy.context.collection.objects.link(obj)

# پارامترهای ستاره
radius1 = 1.0
radius2 = 0.5
depth = 0.2

# ایجاد ستاره توپر
create_solid_star(radius1, radius2, depth)
