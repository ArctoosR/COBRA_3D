import bpy
import bmesh

# آرایه‌ای از نقاط (مثال)
points =[(15,0,37), (-15,0,37), (0,12,11), (-59,-1,-3), (59,-1,-3), (-43,7,-19), (43,7,-19), (63,-3,-19),(-63,-3,-19), (0,12,-19), (-15,-11,-19), (15,-11,-19), (-17,3,-19), (-3,5,-19), (3,5,-19), (17,3,-19),(17,-5,-19), (3,-7,-19), (-3,-7,-19), (-17,-5,-19), (0,0,37), (0,0,44), (-39,-2,-19), (-39,2,-19),(-43,0,-19), (39,2,-19), (43,0,-19), (39,-2,-19), (63,-3,-19), (-63,-3,-19)]

# لبه‌ها بین نقاط (مثال)
edges = [(0,2), (0,1), (1,2), (1,5), (2,5), (0,6), (2,6), (1,3), (3,5), (0,4), (4,6), (2,9), (5,9), (6,9), (3,8), (5,8), (4,7), (6,7), (7,11), (10,11), (8,10), (1,10), (0,11), (14,17), (14,15), (15,16), (16,17), (12,19), (12,13), (13,18), (18,19), (22,23), (22,24), (23,24), (25,27), (25,26), (26,27)]

# وجه‌ها بین نقاط (مثال)
faces = [(2,0,1),(2,1,5),(6,0,2),(5,1,3),(4,0,6),(9,2,5),(6,2,9),(5,3,8),(7,4,6),(6,9,5,8,10,11,7),(8,3,1,10),(1,0,11,10),(11,0,4,7),(16,15,14,17),(18,13,12,19),(24,22,23),(26,25,27) ]


# ایجاد یک مش و یک شیء جدید
mesh = bpy.data.meshes.new(name="CobraMesh")
obj = bpy.data.objects.new(name="CobraObject", object_data=mesh)

# اضافه کردن شیء به صحنه
bpy.context.collection.objects.link(obj)

# ایجاد یک BMesh برای اضافه کردن نقاط، لبه‌ها و وجه‌ها
bm = bmesh.new()

# اضافه کردن نقاط به BMesh
verts = [bm.verts.new(point) for point in points]

# اضافه کردن لبه‌ها بین نقاط
for edge in edges:
    bm.edges.new((verts[edge[0]], verts[edge[1]]))

# اضافه کردن وجه‌ها بین نقاط
for face in faces:
    bm.faces.new([verts[i] for i in face])

# به‌روزرسانی مش با داده‌های BMesh
bm.to_mesh(mesh)
bm.free()

# انتخاب و فعال کردن شیء جدید
bpy.context.view_layer.objects.active = obj
obj.select_set(True)

# ایجاد ماده جدید
material = bpy.data.materials.new(name="EdgeMaterial")
material.diffuse_color = (1, 0, 0, 1)  # رنگ قرمز

# اضافه کردن ماده به شیء
if obj.data.materials:
    obj.data.materials[0] = material
else:
    obj.data.materials.append(material)

# فعال کردن حالت نمایش لبه‌ها
for edge in obj.data.edges:
    edge.use_freestyle_mark = True

# فعال کردن Freestyle در رندر
bpy.context.scene.render.use_freestyle = True
bpy.context.scene.view_layers["View Layer"].freestyle_settings.linesets.new(name="LineSet")
bpy.context.scene.view_layers["View Layer"].freestyle_settings.linesets["LineSet"].select_edge_mark = True


//********************************************_____استخراج___******************
import bpy
import bmesh

# انتخاب آبجکت فعال
obj = bpy.context.active_object

# وارد حالت ویرایش شوید
bpy.ops.object.mode_set(mode='EDIT')

# ایجاد یک BMesh از مش آبجکت
bm = bmesh.from_edit_mesh(obj.data)

# استخراج نقاط
vertices = [v.co for v in bm.verts]
print("Vertices:", vertices)

# استخراج لبه‌ها
edges = [(e.verts[0].co, e.verts[1].co) for e in bm.edges]
print("Edges:", edges)

# استخراج سطوح
faces = [[v.co for v in f.verts] for f in bm.faces]
print("Faces:", faces)

# بازگشت به حالت آبجکت
bpy.ops.object.mode_set(mode='OBJECT')

//********************************************************************************************************

    import bpy
import bmesh

# انتخاب آبجکت فعال
obj = bpy.context.active_object

# وارد حالت ویرایش شوید
bpy.ops.object.mode_set(mode='EDIT')

# ایجاد یک BMesh از مش آبجکت
bm = bmesh.from_edit_mesh(obj.data)
print("vertices:\n")
# استخراج نقاط
vertices = [v.co for v in bm.verts]
print( vertices)
print("edges:\n")
# استخراج لبه‌ها
edges = [(e.verts[0].co, e.verts[1].co) for e in bm.edges]
print( edges)
print("faces:\n")
# استخراج سطوح
faces = [[v.co for v in f.verts] for f in bm.faces]
print( faces)

# بازگشت به حالت آبجکت
bpy.ops.object.mode_set(mode='OBJECT')

