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
//******************************___میخوام این ستاره از 60 لبه تشکیل شود باشد__*********************

import bpy
import math

# تابع برای ایجاد یک ستاره با 60 لبه
def create_solid_star(edges, radius1, radius2, depth):
    verts = []
    faces = []

    angle = math.pi / edges
    for i in range(2 * edges):
        r = radius1 if i % 2 == 0 else radius2
        x = r * math.cos(i * angle)
        y = r * math.sin(i * angle)
        verts.append((x, y, 0))

    for i in range(2 * edges):
        verts.append((verts[i][0], verts[i][1], depth))

    for i in range(2 * edges):
        faces.append((i, (i + 1) % (2 * edges), (i + 1) % (2 * edges) + (2 * edges), i + (2 * edges)))

    faces.append(tuple(range(2 * edges)))
    faces.append(tuple(range(2 * edges, 4 * edges)))

    mesh = bpy.data.meshes.new(name="SolidStar")
    mesh.from_pydata(verts, [], faces)
    obj = bpy.data.objects.new(name="SolidStar", object_data=mesh)
    bpy.context.collection.objects.link(obj)

# پارامترهای ستاره
edges = 30
radius1 = 1.0
radius2 = 0.5
depth = 0.2

# ایجاد ستاره توپر
create_solid_star(edges, radius1, radius2, depth)


//*********************__چاپ مختصات نقاط __******
import bpy
import math

# تابع برای ایجاد یک ستاره با 60 لبه
def create_solid_star(edges, radius1, radius2, depth):
    verts = []
    faces = []

    angle = math.pi / edges
    for i in range(2 * edges):
        r = radius1 if i % 2 == 0 else radius2
        x = r * math.cos(i * angle)
        y = r * math.sin(i * angle)
        verts.append((x, y, 0))
        print(f"Vertex {i}: ({x}, {y}, 0)")

    for i in range(2 * edges):
        verts.append((verts[i][0], verts[i][1], depth))
        print(f"Vertex {i + 2 * edges}: ({verts[i][0]}, {verts[i][1]}, {depth})")

    for i in range(2 * edges):
        faces.append((i, (i + 1) % (2 * edges), (i + 1) % (2 * edges) + (2 * edges), i + (2 * edges)))

    faces.append(tuple(range(2 * edges)))
    faces.append(tuple(range(2 * edges, 4 * edges)))

    mesh = bpy.data.meshes.new(name="SolidStar")
    mesh.from_pydata(verts, [], faces)
    obj = bpy.data.objects.new(name="SolidStar", object_data=mesh)
    bpy.context.collection.objects.link(obj)

# پارامترهای ستاره
edges = 30
radius1 = 1.0
radius2 = 0.5
depth = 0.2

# ایجاد ستاره توپر
create_solid_star(edges, radius1, radius2, depth)


//********************____یک فایل آبجکت دارم و آنرا در بلندر باز میکنم حالا میخوام مختصات نقاط و شماره لبه ها چاپ شود___*****

import bpy

# انتخاب آبجکت
obj = bpy.context.active_object

# اطمینان از اینکه آبجکت یک مش است
if obj.type == 'MESH':
    mesh = obj.data

    # چاپ مختصات نقاط
    print("Vertices:")
    for i, vert in enumerate(mesh.vertices):
        print(f"Vertex {i}: {vert.co}")

    # چاپ شماره لبه‌ها
    print("\nEdges:")
    for i, edge in enumerate(mesh.edges):
        print(f"Edge {i}: {edge.vertices[:]}")

else:
    print("Selected object is not a mesh.")


//********************************************8______چاپ مختصات نقاط به صورت اعداد صحیح__*****

import bpy

# انتخاب آبجکت
obj = bpy.context.active_object

# اطمینان از اینکه آبجکت یک مش است
if obj.type == 'MESH':
    mesh = obj.data

    # چاپ مختصات نقاط به صورت اعداد صحیح
    print("Vertices:")
    for i, vert in enumerate(mesh.vertices):
        co = vert.co
        print(f"Vertex {i}: ({int(co.x)}, {int(co.y)}, {int(co.z)})")

    # چاپ شماره لبه‌ها
    print("\nEdges:")
    for i, edge in enumerate(mesh.edges):
        print(f"Edge {i}: {edge.vertices[:]}")

else:
    print("Selected object is not a mesh.")






//***************************************************************


Vertices:
Vertex 0: (7, 1, -2)
Vertex 1: (2, 1, -2)
Vertex 2: (0, 1, -7)
Vertex 3: (-2, 1, -2)
Vertex 4: (-7, 1, -2)
Vertex 5: (-3, 1, 1)
Vertex 6: (-4, 1, 6)
Vertex 7: (0, 1, 4)
Vertex 8: (4, 1, 7)
Vertex 9: (3, 1, 1)
Vertex 10: (0, 0, 0)
Vertex 11: (0, 2, 0)
Vertex 12: (7, 1, -2)
Vertex 13: (2, 1, -2)
Vertex 14: (0, 1, -7)
Vertex 15: (-2, 1, -2)
Vertex 16: (-7, 1, -2)
Vertex 17: (-3, 1, 1)
Vertex 18: (-4, 1, 6)
Vertex 19: (0, 1, 4)
Vertex 20: (4, 1, 7)
Vertex 21: (3, 1, 1)
Vertex 22: (0, 0, 0)
Vertex 23: (0, 2, 0)
Vertex 24: (7, 1, -2)
Vertex 25: (2, 1, -2)
Vertex 26: (0, 1, -7)
Vertex 27: (-2, 1, -2)
Vertex 28: (-7, 1, -2)
Vertex 29: (-3, 1, 1)
Vertex 30: (-4, 1, 6)
Vertex 31: (0, 1, 4)
Vertex 32: (4, 1, 7)
Vertex 33: (3, 1, 1)
Vertex 34: (0, 0, 0)
Vertex 35: (0, 2, 0)

Edges:
Edge 0: (0, 1)
Edge 1: (1, 2)
Edge 2: (2, 3)
Edge 3: (3, 4)
Edge 4: (4, 5)
Edge 5: (5, 6)
Edge 6: (6, 7)
Edge 7: (7, 8)
Edge 8: (8, 9)
Edge 9: (0, 10)
Edge 10: (0, 11)
Edge 11: (19, 23)
Edge 12: (12, 13)
Edge 13: (13, 14)
Edge 14: (14, 15)
Edge 15: (15, 16)
Edge 16: (16, 17)
Edge 17: (17, 18)
Edge 18: (18, 19)
Edge 19: (19, 20)
Edge 20: (20, 21)
Edge 21: (12, 22)
Edge 22: (21, 22)
Edge 23: (18, 23)
Edge 24: (25, 26)
Edge 25: (26, 27)
Edge 26: (21, 23)
Edge 27: (28, 29)
Edge 28: (29, 30)
Edge 29: (30, 31)
Edge 30: (31, 32)
Edge 31: (32, 33)
Edge 32: (24, 34)
Edge 33: (24, 35)
Edge 34: (19, 22)
Edge 35: (0, 9)
Edge 36: (1, 10)
Edge 37: (24, 25)
Edge 38: (1, 11)
Edge 39: (2, 10)
Edge 40: (2, 11)
Edge 41: (3, 10)
Edge 42: (3, 11)
Edge 43: (20, 22)
Edge 44: (4, 10)
Edge 45: (4, 11)
Edge 46: (5, 10)
Edge 47: (5, 11)
Edge 48: (6, 10)
Edge 49: (27, 28)
Edge 50: (24, 33)
Edge 51: (6, 11)
Edge 52: (20, 23)
Edge 53: (7, 10)
Edge 54: (7, 11)
Edge 55: (8, 10)
Edge 56: (25, 34)
Edge 57: (8, 11)
Edge 58: (25, 35)
Edge 59: (9, 10)
Edge 60: (26, 34)
Edge 61: (9, 11)
Edge 62: (26, 35)
Edge 63: (27, 34)
Edge 64: (27, 35)
Edge 65: (28, 34)
Edge 66: (28, 35)
Edge 67: (29, 34)
Edge 68: (29, 35)
Edge 69: (30, 34)
Edge 70: (30, 35)
Edge 71: (31, 34)
Edge 72: (31, 35)
Edge 73: (32, 34)
Edge 74: (32, 35)
Edge 75: (33, 34)
Edge 76: (33, 35)
Edge 77: (12, 21)
Edge 78: (12, 23)
Edge 79: (13, 22)
Edge 80: (13, 23)
Edge 81: (14, 22)
Edge 82: (14, 23)
Edge 83: (15, 22)
Edge 84: (15, 23)
Edge 85: (16, 22)
Edge 86: (16, 23)
Edge 87: (17, 22)
Edge 88: (17, 23)
Edge 89: (18, 22)









//**************************************************




//****____ ذخیره مختصات نقاط و شماره لبه‌ها در دو تاپل به نام‌های vertices و edges    ____******
import bpy

# انتخاب آبجکت
obj = bpy.context.active_object

# اطمینان از اینکه آبجکت یک مش است
if obj.type == 'MESH':
    mesh = obj.data

    # ذخیره مختصات نقاط به صورت اعداد صحیح در تاپل vertices
    vertices = [(int(vert.co.x), int(vert.co.y), int(vert.co.z)) for vert in mesh.vertices]

    # ذخیره شماره لبه‌ها در تاپل edges
    edges = [(edge.vertices[0], edge.vertices[1]) for edge in mesh.edges]

    # چاپ تاپل‌ها
    print("Vertices:", vertices)
    print("Edges:", edges)

else:
    print("Selected object is not a mesh.")





//*******************************************************************

Vertices: [(7, 1, -2), (2, 1, -2), (0, 1, -7), (-2, 1, -2), (-7, 1, -2), (-3, 1, 1), (-4, 1, 6), (0, 1, 4), (4, 1, 7), (3, 1, 1), (0, 0, 0), (0, 2, 0), (7, 1, -2), (2, 1, -2), (0, 1, -7), (-2, 1, -2), (-7, 1, -2), (-3, 1, 1), (-4, 1, 6), (0, 1, 4), (4, 1, 7), (3, 1, 1), (0, 0, 0), (0, 2, 0), (7, 1, -2), (2, 1, -2), (0, 1, -7), (-2, 1, -2), (-7, 1, -2), (-3, 1, 1), (-4, 1, 6), (0, 1, 4), (4, 1, 7), (3, 1, 1), (0, 0, 0), (0, 2, 0)]
Edges: [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (0, 10), (0, 11), (19, 23), (12, 13), (13, 14), (14, 15), (15, 16), (16, 17), (17, 18), (18, 19), (19, 20), (20, 21), (12, 22), (21, 22), (18, 23), (25, 26), (26, 27), (21, 23), (28, 29), (29, 30), (30, 31), (31, 32), (32, 33), (24, 34), (24, 35), (19, 22), (0, 9), (1, 10), (24, 25), (1, 11), (2, 10), (2, 11), (3, 10), (3, 11), (20, 22), (4, 10), (4, 11), (5, 10), (5, 11), (6, 10), (27, 28), (24, 33), (6, 11), (20, 23), (7, 10), (7, 11), (8, 10), (25, 34), (8, 11), (25, 35), (9, 10), (26, 34), (9, 11), (26, 35), (27, 34), (27, 35), (28, 34), (28, 35), (29, 34), (29, 35), (30, 34), (30, 35), (31, 34), (31, 35), (32, 34), (32, 35), (33, 34), (33, 35), (12, 21), (12, 23), (13, 22), (13, 23), (14, 22), (14, 23), (15, 22), (15, 23), (16, 22), (16, 23), (17, 22), (17, 23), (18, 22)]

//************************



//************_____________ یک اسکریپت که مشخص کند آبجکت چند face  دارد وهر face از چه شماره لبه هایی تشکیل شدهوآنرا چاپ کند___*****

import bpy

# انتخاب آبجکت
obj = bpy.context.active_object

# اطمینان از اینکه آبجکت یک مش است
if obj.type == 'MESH':
    mesh = obj.data

    # چاپ تعداد faces
    print(f"Number of faces: {len(mesh.polygons)}")

    # چاپ شماره لبه‌های هر face در یک تاپل
    for i, face in enumerate(mesh.polygons):
        edge_indices = tuple(edge for edge in face.edge_keys)
        print(f"Face {i}: Edges {edge_indices}")

else:
    print("Selected object is not a mesh.")


//****************************************************************************************

Number of faces: 60
Face 0: Edges [(0, 10), (1, 10), (0, 1)]
Face 1: Edges [(1, 10), (2, 10), (1, 2)]
Face 2: Edges [(2, 10), (3, 10), (2, 3)]
Face 3: Edges [(3, 10), (4, 10), (3, 4)]
Face 4: Edges [(4, 10), (5, 10), (4, 5)]
Face 5: Edges [(5, 10), (6, 10), (5, 6)]
Face 6: Edges [(6, 10), (7, 10), (6, 7)]
Face 7: Edges [(7, 10), (8, 10), (7, 8)]
Face 8: Edges [(8, 10), (9, 10), (8, 9)]
Face 9: Edges [(9, 10), (0, 10), (0, 9)]
Face 10: Edges [(0, 11), (9, 11), (0, 9)]
Face 11: Edges [(9, 11), (8, 11), (8, 9)]
Face 12: Edges [(8, 11), (7, 11), (7, 8)]
Face 13: Edges [(7, 11), (6, 11), (6, 7)]
Face 14: Edges [(6, 11), (5, 11), (5, 6)]
Face 15: Edges [(5, 11), (4, 11), (4, 5)]
Face 16: Edges [(4, 11), (3, 11), (3, 4)]
Face 17: Edges [(3, 11), (2, 11), (2, 3)]
Face 18: Edges [(2, 11), (1, 11), (1, 2)]
Face 19: Edges [(1, 11), (0, 11), (0, 1)]
Face 20: Edges [(12, 22), (13, 22), (12, 13)]
Face 21: Edges [(13, 22), (14, 22), (13, 14)]
Face 22: Edges [(14, 22), (15, 22), (14, 15)]
Face 23: Edges [(15, 22), (16, 22), (15, 16)]
Face 24: Edges [(16, 22), (17, 22), (16, 17)]
Face 25: Edges [(17, 22), (18, 22), (17, 18)]
Face 26: Edges [(18, 22), (19, 22), (18, 19)]
Face 27: Edges [(19, 22), (20, 22), (19, 20)]
Face 28: Edges [(20, 22), (21, 22), (20, 21)]
Face 29: Edges [(21, 22), (12, 22), (12, 21)]
Face 30: Edges [(12, 23), (21, 23), (12, 21)]
Face 31: Edges [(21, 23), (20, 23), (20, 21)]
Face 32: Edges [(20, 23), (19, 23), (19, 20)]
Face 33: Edges [(19, 23), (18, 23), (18, 19)]
Face 34: Edges [(18, 23), (17, 23), (17, 18)]
Face 35: Edges [(17, 23), (16, 23), (16, 17)]
Face 36: Edges [(16, 23), (15, 23), (15, 16)]
Face 37: Edges [(15, 23), (14, 23), (14, 15)]
Face 38: Edges [(14, 23), (13, 23), (13, 14)]
Face 39: Edges [(13, 23), (12, 23), (12, 13)]
Face 40: Edges [(24, 34), (25, 34), (24, 25)]
Face 41: Edges [(25, 34), (26, 34), (25, 26)]
Face 42: Edges [(26, 34), (27, 34), (26, 27)]
Face 43: Edges [(27, 34), (28, 34), (27, 28)]
Face 44: Edges [(28, 34), (29, 34), (28, 29)]
Face 45: Edges [(29, 34), (30, 34), (29, 30)]
Face 46: Edges [(30, 34), (31, 34), (30, 31)]
Face 47: Edges [(31, 34), (32, 34), (31, 32)]
Face 48: Edges [(32, 34), (33, 34), (32, 33)]
Face 49: Edges [(33, 34), (24, 34), (24, 33)]
Face 50: Edges [(24, 35), (33, 35), (24, 33)]
Face 51: Edges [(33, 35), (32, 35), (32, 33)]
Face 52: Edges [(32, 35), (31, 35), (31, 32)]
Face 53: Edges [(31, 35), (30, 35), (30, 31)]
Face 54: Edges [(30, 35), (29, 35), (29, 30)]
Face 55: Edges [(29, 35), (28, 35), (28, 29)]
Face 56: Edges [(28, 35), (27, 35), (27, 28)]
Face 57: Edges [(27, 35), (26, 35), (26, 27)]
Face 58: Edges [(26, 35), (25, 35), (25, 26)]
Face 59: Edges [(25, 35), (24, 35), (24, 25)]
Number of faces: 60
Face 0: Edges ((0, 10), (1, 10), (0, 1))
Face 1: Edges ((1, 10), (2, 10), (1, 2))
Face 2: Edges ((2, 10), (3, 10), (2, 3))
Face 3: Edges ((3, 10), (4, 10), (3, 4))
Face 4: Edges ((4, 10), (5, 10), (4, 5))
Face 5: Edges ((5, 10), (6, 10), (5, 6))
Face 6: Edges ((6, 10), (7, 10), (6, 7))
Face 7: Edges ((7, 10), (8, 10), (7, 8))
Face 8: Edges ((8, 10), (9, 10), (8, 9))
Face 9: Edges ((9, 10), (0, 10), (0, 9))
Face 10: Edges ((0, 11), (9, 11), (0, 9))
Face 11: Edges ((9, 11), (8, 11), (8, 9))
Face 12: Edges ((8, 11), (7, 11), (7, 8))
Face 13: Edges ((7, 11), (6, 11), (6, 7))
Face 14: Edges ((6, 11), (5, 11), (5, 6))
Face 15: Edges ((5, 11), (4, 11), (4, 5))
Face 16: Edges ((4, 11), (3, 11), (3, 4))
Face 17: Edges ((3, 11), (2, 11), (2, 3))
Face 18: Edges ((2, 11), (1, 11), (1, 2))
Face 19: Edges ((1, 11), (0, 11), (0, 1))
Face 20: Edges ((12, 22), (13, 22), (12, 13))
Face 21: Edges ((13, 22), (14, 22), (13, 14))
Face 22: Edges ((14, 22), (15, 22), (14, 15))
Face 23: Edges ((15, 22), (16, 22), (15, 16))
Face 24: Edges ((16, 22), (17, 22), (16, 17))
Face 25: Edges ((17, 22), (18, 22), (17, 18))
Face 26: Edges ((18, 22), (19, 22), (18, 19))
Face 27: Edges ((19, 22), (20, 22), (19, 20))
Face 28: Edges ((20, 22), (21, 22), (20, 21))
Face 29: Edges ((21, 22), (12, 22), (12, 21))
Face 30: Edges ((12, 23), (21, 23), (12, 21))
Face 31: Edges ((21, 23), (20, 23), (20, 21))
Face 32: Edges ((20, 23), (19, 23), (19, 20))
Face 33: Edges ((19, 23), (18, 23), (18, 19))
Face 34: Edges ((18, 23), (17, 23), (17, 18))
Face 35: Edges ((17, 23), (16, 23), (16, 17))
Face 36: Edges ((16, 23), (15, 23), (15, 16))
Face 37: Edges ((15, 23), (14, 23), (14, 15))
Face 38: Edges ((14, 23), (13, 23), (13, 14))
Face 39: Edges ((13, 23), (12, 23), (12, 13))
Face 40: Edges ((24, 34), (25, 34), (24, 25))
Face 41: Edges ((25, 34), (26, 34), (25, 26))
Face 42: Edges ((26, 34), (27, 34), (26, 27))
Face 43: Edges ((27, 34), (28, 34), (27, 28))
Face 44: Edges ((28, 34), (29, 34), (28, 29))
Face 45: Edges ((29, 34), (30, 34), (29, 30))
Face 46: Edges ((30, 34), (31, 34), (30, 31))
Face 47: Edges ((31, 34), (32, 34), (31, 32))
Face 48: Edges ((32, 34), (33, 34), (32, 33))
Face 49: Edges ((33, 34), (24, 34), (24, 33))
Face 50: Edges ((24, 35), (33, 35), (24, 33))
Face 51: Edges ((33, 35), (32, 35), (32, 33))
Face 52: Edges ((32, 35), (31, 35), (31, 32))
Face 53: Edges ((31, 35), (30, 35), (30, 31))
Face 54: Edges ((30, 35), (29, 35), (29, 30))
Face 55: Edges ((29, 35), (28, 35), (28, 29))
Face 56: Edges ((28, 35), (27, 35), (27, 28))
Face 57: Edges ((27, 35), (26, 35), (26, 27))
Face 58: Edges ((26, 35), (25, 35), (25, 26))
Face 59: Edges ((25, 35), (24, 35), (24, 25))
