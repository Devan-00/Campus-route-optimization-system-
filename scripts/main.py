"""
Campus Route Optimization System
Author: Deva Krishna Jayan

This script implements Dijkstra’s algorithm
for indoor navigation using graph-based modeling.
"""

import bpy
import heapq

# ---------------------------------------------------
# 1. GRAPH CONSTRUCTION (GROUND + FIRST + SECOND)
# ---------------------------------------------------

def build_graph():
    graph = {}
    nodes = [obj for obj in bpy.data.objects if 
             obj.name.startswith("Node_F_") or 
             obj.name.startswith("Node_G_") or 
             obj.name.startswith("Node_S_") or
             obj.name.startswith("Node_S0") or 
             obj.name.startswith("Node_S1") or 
             obj.name.startswith("Node_S2") or 
             obj.name.startswith("Node_S3") or 
             obj.name == "College_Lobby" or
             obj.name == "Node_Project_Lab"]

    for obj in nodes:
        graph[obj.name] = []

    def connect(a, b):
        if a in graph and b in graph:
            loc1 = bpy.data.objects[a].location
            loc2 = bpy.data.objects[b].location
            weight = (loc1 - loc2).length
            graph[a].append((b, weight))
            graph[b].append((a, weight))

    # --- GROUND CONNECTIONS ---
    connect("Node_G_P1","Node_G_P2"); connect("Node_G_P2","Node_G_J1")
    connect("Node_G_J1","Node_G_J2"); connect("Node_G_J2","Node_G_P3")
    connect("Node_G_P3","Node_G_P4"); connect("Node_G_P4","Node_G_P5")
    connect("Node_G_P5","Node_G_J6"); connect("Node_G_J6","Node_G_P6")
    connect("Node_G_P6","Node_G_P7"); connect("Node_G_P7","Node_G_P8")
    connect("Node_G_P8","Node_G_P9"); connect("Node_G_P9","Node_G_P10")
    connect("Node_G_P10","Node_G_P11"); connect("Node_G_P11","Node_G_P12")
    connect("Node_G_P12","Node_G_J7"); connect("Node_G_J7","Node_G_P13")
    connect("Node_G_J7","Node_G_P14"); connect("Node_G_P14","Node_G_P15")
    connect("Node_G_P15","Node_G_P16"); connect("Node_G_P16","Node_G_P17")
    connect("Node_G_P17","Node_G_P18"); connect("Node_G_P18","Node_G_J8")
    connect("Node_G_J8","Node_G_P19"); connect("Node_G_J8","Node_G_P30")
    connect("Node_G_P30","Node_G_J4"); connect("Node_G_J4","Node_G_P37")
    connect("Node_G_P37","Node_G_J3"); connect("Node_G_J3","Node_G_P20")
    connect("Node_G_J3","Node_G_P21"); connect("Node_G_P21","Node_G_P23")
    connect("Node_G_P23","Node_G_P24"); connect("Node_G_J1","Node_G_P24")
    connect("Node_G_J2","Node_G_P25"); connect("Node_G_P25","Node_G_P26")
    connect("Node_G_P26","Node_G_P27"); connect("Node_G_P27","Node_G_P28")
    connect("Node_G_J5","Node_G_P28"); connect("Node_G_J5","Node_G_J4")
    connect("Node_G_P8","Node_G_P29"); connect("Node_G_P30","Node_G_P29")
    
    # Ground Rooms
    connect("Node_G_P1","Node_G_WashArea"); connect("Node_G_P1","Node_G_ChemistryLab")
    connect("Node_G_P16","Node_G_Record room")
    connect("Node_G_P2","Node_G_PhysicsLab"); connect("Node_G_J1","Node_G_Stair_1")
    connect("Node_G_P3","Node_G_G03"); connect("Node_G_P4","Node_G_G04")
    connect("Node_G_P5","Node_G_G05"); connect("Node_G_J6","Node_G_Ramp")
    connect("Node_G_P6","Node_G_Wending_machine"); connect("Node_G_P7","Node_G_Stair_7")
    connect("Node_G_P8","College_Lobby"); connect("College_Lobby","Node_G_Lobby_Reception")
    connect("Node_G_P10","Node_G_Stair_6"); connect("Node_G_P11","Node_G_G06")
    connect("Node_G_P12","Node_G_G07"); connect("Node_G_P13","Node_G_G08")
    connect("Node_G_P13","Node_G_Stair_5"); connect("Node_G_P14","Node_G_EEE_HOD")
    connect("Node_G_P14","Node_G_Facultyroom4"); connect("Node_G_P15","Node_G_EE_lib")
    connect("Node_G_P16","Node_G_Record_room"); connect("Node_G_P16","Node_G_Facultyroom3")
    connect("Node_G_P17","Node_G_EC_Hod"); connect("Node_G_P17","Node_G_Facultyroom2")
    connect("Node_G_P18","Node_G_Facultyroom1"); connect("Node_G_P18","Node_G_Lab_eee")
    connect("Node_G_P19","Node_G_Stair_4"); connect("Node_G_J5","Node_G_S_Boys_Restroom2")
    connect("Node_G_J5","Node_G_S_Boys_Restroom1"); connect("Node_G_P26","Node_G_Main_Stage")
    connect("Node_G_P25","Node_G_Girls_Restroom"); connect("Node_G_P29","Node_G_Courtyard")
    connect("Node_G_P23","Node_G_Library"); connect("Node_G_P37","Node_G_Lift")
    connect("Node_G_P20","Node_G_Stair_2"); connect("Node_G_P20","Node_G_Boys_Restroom")
    connect("Node_G_P20","Node_G_P22"); connect("Node_G_P22","Node_G_TwowheelerParking")

    # --- FIRST CONNECTIONS ---
    connect("Node_F_J1", "Node_F_J2"); connect("Node_F_J2", "Node_F_P1")
    connect("Node_F_P1", "Node_F_P2"); connect("Node_F_P1", "Node_F_J3")
    connect("Node_F_J3", "Node_F_J4"); connect("Node_F_J4", "Node_F_P3")
    connect("Node_F_J4", "Node_F_P33"); connect("Node_F_P33", "Node_F_P32")
    connect("Node_F_P32", "Node_F_P31"); connect("Node_F_P31", "Node_F_P30")
    connect("Node_F_P30", "Node_F_P29"); connect("Node_F_P29", "Node_F_P35")
    connect("Node_F_P35", "Node_F_P28"); connect("Node_F_P28", "Node_F_P27")
    connect("Node_F_P27", "Node_F_J12"); connect("Node_F_J12", "Node_F_P26")
    connect("Node_F_J12", "Node_F_P25"); connect("Node_F_P25", "Node_F_P24")
    connect("Node_F_P24", "Node_F_P23"); connect("Node_F_P23", "Node_F_P22")
    connect("Node_F_P22", "Node_F_P21"); connect("Node_F_P21", "Node_F_P20")
    connect("Node_F_P20", "Node_F_P19"); connect("Node_F_P19", "Node_F_J8")
    connect("Node_F_P4", "Node_F_P3"); connect("Node_F_J5", "Node_F_P4")
    connect("Node_F_J5", "Node_F_P5"); connect("Node_F_P5", "Node_F_P6")
    connect("Node_F_P7", "Node_F_J5"); connect("Node_F_P7", "Node_F_P8")
    connect("Node_F_P8", "Node_F_P9"); connect("Node_F_P9", "Node_F_P10")
    connect("Node_F_P10", "Node_F_P11"); connect("Node_F_P11", "Node_F_J6")
    connect("Node_F_J6", "Node_F_J7"); connect("Node_F_J6", "Node_F_P12")
    connect("Node_F_P12", "Node_F_J8"); connect("Node_F_J8", "Node_F_P34")
    connect("Node_F_P34", "Node_F_P36"); connect("Node_F_P13", "Node_F_P36")
    connect("Node_F_P13", "Node_F_J11"); connect("Node_F_J11", "Node_F_P14")
    connect("Node_F_J11", "Node_F_P15"); connect("Node_F_P15", "Node_F_P16")
    connect("Node_F_P16", "Node_F_P17"); connect("Node_F_P17", "Node_F_P18")
    connect("Node_F_P2", "Node_F_J3")
    
    # First Rooms
    connect("Node_F_J1", "Node_F_Office"); connect("Node_F_J1", "Node_F_Meeting_Hall")
    connect("Node_F_J2", "Node_F_Principle_Office"); connect("Node_F_J2", "Node_F_CTO")
    connect("Node_F_P1", "Node_F_Reception"); connect("Node_F_P2", "Node_F_DirectorAcademics")
    connect("Node_F_J3", "Node_F_Stair_1"); connect("Node_F_P3", "Node_F_Exam_cell")
    connect("Node_F_P4", "Node_F_SeminarHall"); connect("Node_F_J5", "Node_F_IQAC")
    connect("Node_F_P5", "Node_F_F30"); connect("Node_F_P6", "Node_F_Stair_2")
    connect("Node_F_P6", "Node_F_Boys_Restroom"); connect("Node_F_P7", "Node_F_Lift")
    connect("Node_F_P8", "Node_F_PL_Lab"); connect("Node_F_P9", "Node_F_ADP_Lab")
    connect("Node_F_P10", "Node_F_Stair_3"); connect("Node_F_P11", "Node_F_CofeeShop")
    connect("Node_F_J7", "Node_F_Print_Shop"); connect("Node_F_J7", "Node_F_College_Store")
    connect("Node_F_P12", "Node_F_NP_Lab"); connect("Node_F_J8", "Node_F_CSE_SeminarHall")
    connect("Node_F_P34", "Node_F_Drinking_Water1"); connect("Node_F_P36", "Node_F_Girls_Washroom")
    connect("Node_F_P13", "Node_F_Stair_4"); connect("Node_F_P14", "Node_F_Robotics_FacultyRoom")
    connect("Node_F_P14", "Node_F_Robotics_Library"); connect("Node_F_P15", "Node_F_F21")
    connect("Node_F_P16", "Node_F_F20"); connect("Node_F_P17", "Node_F_F19")
    connect("Node_F_P18", "Node_F_F18"); connect("Node_F_P19", "Node_F_Robotics_SeminarHall")
    connect("Node_F_P19", "Node_F_Faculty4"); connect("Node_F_P20", "Node_F_RecordRoom")
    connect("Node_F_P21", "Node_F_HOD_CS"); connect("Node_F_P21", "Node_F_Facultyroom1")
    connect("Node_F_P22", "Node_F_Library_CS"); connect("Node_F_P23", "Node_F_F10B")
    connect("Node_F_P23", "Node_F_Facultyroom2"); connect("Node_F_P24", "Node_F_F10A")
    connect("Node_F_P25", "Node_F_TraningAndPlacement"); connect("Node_F_P25", "Node_F_Facultyroom3")
    connect("Node_F_P26", "Node_F_Stair_5"); connect("Node_F_P26", "Node_F_F09")
    connect("Node_F_J12", "Node_F_F08"); connect("Node_F_P27", "Node_F_F07")
    connect("Node_F_P28", "Node_F_Stair_6"); connect("Node_F_P35", "Node_F_Drinking_Water2")
    connect("Node_F_P29", "Node_F_SI_Lab"); connect("Node_F_P30", "Node_F_Stair_7")
    connect("Node_F_P31", "Node_F_F05"); connect("Node_F_P32", "Node_F_F04")
    connect("Node_F_P33", "Node_F_F03")

    # --- SECOND CONNECTIONS ---
    connect("Node_S_P1","Node_S_P2"); connect("Node_S_P2","Node_S_J1")
    connect("Node_S_J1","Node_S_Stair_1"); connect("Node_S_J1","Node_S_P3")
    connect("Node_S_P3","Node_S_P4"); connect("Node_S_P4","Node_S_P5")
    connect("Node_S_P5","Node_S_P6"); connect("Node_S_P7","Node_S_P6")
    connect("Node_S_P7","Node_S_P8"); connect("Node_S_P8","Node_S_P9")
    connect("Node_S_P9","Node_S_J2"); connect("Node_S_J2","Node_S_P10")
    connect("Node_S_J2","Node_S_P11"); connect("Node_S_P11","Node_S_P12")
    connect("Node_S_P12","Node_S_P13"); connect("Node_S_P14","Node_S_P13")
    connect("Node_S_P14","Node_S_P15"); connect("Node_S_P15","Node_S_P16")
    connect("Node_S_P16","Node_S_J3"); connect("Node_S_J3","Node_S_P17")
    connect("Node_S_P17","Node_S_P18"); connect("Node_S_P18","Node_S_P19")
    connect("Node_S_P19","Node_S_J4"); connect("Node_S_J4","Node_S_P20")
    connect("Node_S_P20","Node_S_P21"); connect("Node_S_P21","Node_S_P22")
    connect("Node_S_P22","Node_S_P23"); connect("Node_S_J3","Node_S_P24")
    connect("Node_S_P24","Node_S_P25"); connect("Node_S_P25","Node_S_P26")
    connect("Node_S_P26","Node_S_J6"); connect("Node_S_J6","Node_S_P27")
    connect("Node_S_P27","Node_S_P28"); connect("Node_S_P28","Node_S_P29")
    connect("Node_S_J7","Node_S_P30"); connect("Node_S_P30","Node_S_P31")
    connect("Node_S_J7","Node_S_P33")
    connect("Node_S_P33","Node_S_J1")
    connect("Node_S_P29","Node_S_J7")

    # Second Rooms 
    connect("Node_S_MuSpace","Node_S_P1"); connect("Node_S_P1","Node_S37")
    connect("Node_S36","Node_S_P2"); connect("Node_S01","Node_S_P3")
    connect("Node_S02","Node_S_P4"); connect("Node_S03","Node_S_P5")
    connect("Node_S_Stair_7","Node_S_P6"); connect("Node_S_MINI_SEMINARHALL","Node_S_P7")
    connect("Node_S_Stair_6","Node_S_P8"); connect("Node_S05","Node_S_P9")
    connect("Node_S06","Node_S_J2"); connect("Node_S07","Node_S_P10")
    connect("Node_S_P10","Node_S_Stair_5"); connect("Node_S_P11","Node_S_ECE_HOD_ROOM")
    connect("Node_S_P11","Node_S_Library_ECE"); connect("Node_S_P12","Node_S_ECE_RecordRoom1")
    connect("Node_S_P13","Node_S_Facultyroom3_ECE"); connect("Node_S_P13","Node_S_Facultyroom1_ECE")
    connect("Node_S_P14","Node_S_Facultyroom4_ECE"); connect("Node_S_P14","Node_S_Facultyroom2_ECE")
    connect("Node_S_P15","Node_S_ECE_RecordRoom2"); connect("Node_S_P16","Node_S_Facultyroom5_ECE")
    connect("Node_S_P16","Node_S_IOT_LAB"); connect("Node_Project_Lab","Node_S_P23")
    connect("Node_S_P23","Node_S18"); connect("Node_S_P22","Node_S19")
    connect("Node_S_P21","Node_S20"); connect("Node_S_P20","Node_S21")
    connect("Node_S_J4","Node_S_Centre_For_Antennadesign"); connect("Node_S_P18","Node_S_Girls_Washroom")
    connect("Node_S_P17","Node_S_Drinking_Water1"); connect("Node_S_J3","Node_S_Powersystem_SimulationLab")
    connect("Node_S_P24","Node_S_Programming_And_SimulationLab"); connect("Node_S_P25","Node_S_SimulationLab")
    connect("Node_S_P26","Node_S_VLSI_DesignLab"); connect("Node_S_J6","Node_S_StudentsCouncil")
    connect("Node_S_J6","Node_S_Stair_3"); connect("Node_S_P27","Node_S_ElectronicsWorkshop")
    connect("Node_S_P28","Node_S_CircuitLab"); connect("Node_S_P29","Node_S_MTec_EmbeddedSystems")
    connect("Node_S_P29","Node_S_Lift"); connect("Node_S_Microprocessor_MicrocontrollerLab","Node_S_P30")
    connect("Node_S_P31","Node_S_Stair_2"); connect("Node_S_P33","Node_S_SeminarHall")
    connect("Node_S_P19","Node_S_Stair_4")
    connect("Node_S_P31","Node_S_Boys_Restroom")

    # --- VERTICAL BRIDGES ---
    connect("Node_G_Stair_1", "Node_F_Stair_1"); connect("Node_G_Stair_7", "Node_F_Stair_7")
    connect("Node_G_Stair_6", "Node_F_Stair_6"); connect("Node_G_Stair_5", "Node_F_Stair_5")
    connect("Node_G_Stair_4", "Node_F_Stair_4"); connect("Node_G_Lift",    "Node_F_Lift")
    connect("Node_G_Stair_2", "Node_F_Stair_2"); connect("Node_F_Stair_1", "Node_S_Stair_1")
    connect("Node_F_Stair_7", "Node_S_Stair_7"); connect("Node_F_Stair_6", "Node_S_Stair_6")
    connect("Node_F_Stair_5", "Node_S_Stair_5"); connect("Node_F_Stair_4", "Node_S_Stair_4")
    connect("Node_F_Lift",    "Node_S_Lift");    connect("Node_F_Stair_3", "Node_S_Stair_3")
    connect("Node_F_Stair_2", "Node_S_Stair_2")

    return graph

# ---------------------------------------------------
# 2. DIJKSTRA ENGINE
# ---------------------------------------------------

def dijkstra(graph, start, end):
    queue = [(0, start, [])]
    visited = set()
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node in visited: continue
        visited.add(node)
        path = path + [node]
        if node == end: return path
        if node in graph:
            for neighbor, weight in graph[node]:
                heapq.heappush(queue, (cost + weight, neighbor, path))
    return None

# ---------------------------------------------------
# 3. HELPERS: ROOM LISTS (WITH SEARCH FILTER)
# ---------------------------------------------------

def get_rooms(prefix, filter_str=""):
    rooms = []
    extra_starts = ["Node_S0", "Node_S1", "Node_S2", "Node_S3"]
    f_low = filter_str.lower()
    
    for obj in bpy.data.objects:
        is_path = "_P" in obj.name and any(c.isdigit() for c in obj.name)
        is_junc = "_J" in obj.name and any(c.isdigit() for c in obj.name)
        match = obj.name.startswith(prefix) or any(obj.name.startswith(s) for s in extra_starts) if prefix == "Node_S_" else obj.name.startswith(prefix)
        
        if match and not (is_path or is_junc):
            label = obj.name.replace("Node_", "").replace("_", " ")
            # Only add if filter matches label or object name
            if not f_low or (f_low in label.lower() or f_low in obj.name.lower()):
                rooms.append((obj.name, label, ""))
    
    if not rooms:
        rooms.append(("NONE", "No results found", ""))
        
    return sorted(rooms)

# ---------------------------------------------------
# 4. OPERATORS
# ---------------------------------------------------

class NAV_OT_find_route(bpy.types.Operator):
    bl_idname = "nav.find_route"
    bl_label = "Generate Path"

    def create_label(self, context, name, text, location):
        font_curve = bpy.data.curves.new(type="FONT", name=name)
        font_curve.body = text
        font_curve.size = 0.17
        obj = bpy.data.objects.new(name, font_curve)
        obj.location = (location.x, location.y, location.z + 0.6)
        context.collection.objects.link(obj)
        
        mat = bpy.data.materials.get("NavRed")
        if mat:
            obj.data.materials.append(mat)
        return obj
    
    def execute(self, context):
        scene = context.scene
        if scene.nav_floor_start == 'G': start = scene.nav_start_g
        elif scene.nav_floor_start == 'F': start = scene.nav_start_f
        else: start = scene.nav_start_s
            
        if scene.nav_floor_end == 'G': end = scene.nav_end_g
        elif scene.nav_floor_end == 'F': end = scene.nav_end_f
        else: end = scene.nav_end_s

        if start == "NONE" or end == "NONE":
            self.report({'ERROR'}, "Please select a valid room!")
            return {'CANCELLED'}

        graph = build_graph()
        full_path = dijkstra(graph, start, end)

        if not full_path:
            self.report({'ERROR'}, "No path found!")
            return {'CANCELLED'}

        for obj in list(bpy.data.objects):
            if obj.name.startswith("Nav_Path_") or obj.name.startswith("Nav_Label_"):
                bpy.data.objects.remove(obj, do_unlink=True)

        current_segment = []
        segments = []
        last_floor = None

        for node in full_path:
            if "Node_G_" in node or node == "College_Lobby": floor = 'G'
            elif "Node_F_" in node: floor = 'F'
            else: floor = 'S'
            
            if last_floor and floor != last_floor:
                segments.append(current_segment)
                current_segment = [node]
            else:
                current_segment.append(node)
            last_floor = floor
        segments.append(current_segment)

        mat = bpy.data.materials.get("NavRed")
        if not mat:
            mat = bpy.data.materials.new("NavRed")
            mat.use_nodes = False
            mat.diffuse_color = (1.0, 0.0, 0.0, 1.0)

        for idx, seg in enumerate(segments):
            if len(seg) < 2: continue
            curve = bpy.data.curves.new(f"PathCurve_{idx}", type='CURVE')
            curve.dimensions = '3D'
            spline = curve.splines.new('POLY')
            spline.points.add(len(seg)-1)
            for i, node_name in enumerate(seg):
                loc = bpy.data.objects[node_name].location
                spline.points[i].co = (loc.x, loc.y, loc.z + 0.1, 1)
            
            obj = bpy.data.objects.new(f"Nav_Path_{idx}", curve)
            context.collection.objects.link(obj)
            obj.data.bevel_depth = 0.02
            obj.data.materials.append(mat)

        start_text = start.replace("Node_", "").replace("_", " ")
        end_text = end.replace("Node_", "").replace("_", " ")
        self.create_label(context, "Nav_Label_Start", f"   Now You Are Here: {start_text}", bpy.data.objects[start].location)
        self.create_label(context, "Nav_Label_End", f"GOAL: {end_text}", bpy.data.objects[end].location)

        return {'FINISHED'}

class NAV_OT_clear_path(bpy.types.Operator):
    bl_idname = "nav.clear_path"
    bl_label = "Clear Path"
    def execute(self, context):
        for obj in list(bpy.data.objects):
            if obj.name.startswith("Nav_Path_") or obj.name.startswith("Nav_Label_"):
                bpy.data.objects.remove(obj, do_unlink=True)
        return {'FINISHED'}

# ---------------------------------------------------
# 5. UI PANEL (WITH SEARCH BOXES)
# ---------------------------------------------------

class NAV_PT_panel(bpy.types.Panel):
    bl_label = "Campus Navigation"
    bl_idname = "NAV_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Navigation'

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # --- START POINT BOX ---
        box = layout.box()
        box.label(text="Start Point", icon='TRIA_RIGHT')
        box.row().prop(scene, "nav_floor_start", expand=True)
        
        # New Search Field for Start
        box.prop(scene, "nav_search_start", text="", icon='VIEWZOOM', placeholder="Search start room...")
        
        if scene.nav_floor_start == 'G': box.prop(scene, "nav_start_g", text="Room")
        elif scene.nav_floor_start == 'F': box.prop(scene, "nav_start_f", text="Room")
        else: box.prop(scene, "nav_start_s", text="Room")

        # --- DESTINATION BOX ---
        box = layout.box()
        box.label(text="Destination", icon='TRIA_DOWN')
        box.row().prop(scene, "nav_floor_end", expand=True)
        
        # New Search Field for End
        box.prop(scene, "nav_search_end", text="", icon='VIEWZOOM', placeholder="Search destination...")
        
        if scene.nav_floor_end == 'G': box.prop(scene, "nav_end_g", text="Room")
        elif scene.nav_floor_end == 'F': box.prop(scene, "nav_end_f", text="Room")
        else: box.prop(scene, "nav_end_s", text="Room")

        layout.separator()
        row = layout.row()
        row.scale_y = 1.8
        row.operator("nav.find_route", text="NAVIGATE", icon='ORIENTATION_VIEW')
        layout.operator("nav.clear_path", icon='CANCEL')

# ---------------------------------------------------
# 6. REGISTRATION
# ---------------------------------------------------

def register():
    bpy.utils.register_class(NAV_OT_find_route)
    bpy.utils.register_class(NAV_OT_clear_path)
    bpy.utils.register_class(NAV_PT_panel)

    floor_items = [('G','Ground',''),('F','First',''),('S','Second','')]
    bpy.types.Scene.nav_floor_start = bpy.props.EnumProperty(items=floor_items, name="Floor")
    bpy.types.Scene.nav_floor_end = bpy.props.EnumProperty(items=floor_items, name="Floor")
    
    # New Search String Properties
    bpy.types.Scene.nav_search_start = bpy.props.StringProperty(name="Search Start")
    bpy.types.Scene.nav_search_end = bpy.props.StringProperty(name="Search End")
    
    # Updated Enums to include the search filter
    bpy.types.Scene.nav_start_g = bpy.props.EnumProperty(items=lambda s,c: get_rooms("Node_G_", s.nav_search_start))
    bpy.types.Scene.nav_start_f = bpy.props.EnumProperty(items=lambda s,c: get_rooms("Node_F_", s.nav_search_start))
    bpy.types.Scene.nav_start_s = bpy.props.EnumProperty(items=lambda s,c: get_rooms("Node_S_", s.nav_search_start))
    
    bpy.types.Scene.nav_end_g = bpy.props.EnumProperty(items=lambda s,c: get_rooms("Node_G_", s.nav_search_end))
    bpy.types.Scene.nav_end_f = bpy.props.EnumProperty(items=lambda s,c: get_rooms("Node_F_", s.nav_search_end))
    bpy.types.Scene.nav_end_s = bpy.props.EnumProperty(items=lambda s,c: get_rooms("Node_S_", s.nav_search_end))

    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            for space in area.spaces:
                if space.type == 'VIEW_3D':
                    space.overlay.show_relationship_lines = False

def unregister():
    bpy.utils.unregister_class(NAV_OT_find_route)
    bpy.utils.unregister_class(NAV_OT_clear_path)
    bpy.utils.unregister_class(NAV_PT_panel)
    
    # Cleanup properties
    del bpy.types.Scene.nav_search_start
    del bpy.types.Scene.nav_search_end

if __name__ == "__main__":
    register()
