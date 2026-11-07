"""Build the CH01 storefront pipeline experiment in its existing chapter map."""
from pathlib import Path
import unreal

ROOT = Path(__file__).resolve().parents[2]
BASE = '/Game/RenderingLab/Chapters/Part01_RenderingBasics/CH01_RenderingPipeline'
MAP = BASE + '/Maps/L_CH01_RenderingPipeline'
assets = unreal.EditorAssetLibrary
tools = unreal.AssetToolsHelpers.get_asset_tools()
levels = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
actors = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
lib = unreal.MaterialEditingLibrary


def surface(name, color, roughness=0.6, metallic=0.0):
    path = BASE + '/Materials/' + name
    if assets.does_asset_exist(path):
        return unreal.load_asset(path)
    instance = tools.create_asset(name, BASE + '/Materials', unreal.MaterialInstanceConstant,
                                 unreal.MaterialInstanceConstantFactoryNew())
    lib.set_material_instance_parent(instance, unreal.load_asset('/Game/RenderingLab/Common/Materials/M_LabSurface'))
    lib.set_material_instance_vector_parameter_value(instance, 'BaseColor', unreal.LinearColor(*color, 1))
    lib.set_material_instance_scalar_parameter_value(instance, 'Roughness', roughness)
    lib.set_material_instance_scalar_parameter_value(instance, 'Metallic', metallic)
    assets.save_loaded_asset(instance)
    return instance


def constant(material, value, prop, position):
    cls = unreal.MaterialExpressionConstant3Vector if isinstance(value, tuple) else unreal.MaterialExpressionConstant
    node = lib.create_material_expression(material, cls, *position)
    if isinstance(value, tuple):
        node.set_editor_property('constant', unreal.LinearColor(*value, 1))
    else:
        node.set_editor_property('r', value)
    lib.connect_material_property(node, '', prop)


def special_material(name, kind):
    path = BASE + '/Materials/' + name
    if assets.does_asset_exist(path):
        return unreal.load_asset(path)
    material = tools.create_asset(name, BASE + '/Materials', unreal.Material, unreal.MaterialFactoryNew())
    if kind == 'glass':
        material.set_editor_property('blend_mode', unreal.BlendMode.BLEND_TRANSLUCENT)
        material.set_editor_property('translucency_lighting_mode', unreal.TranslucencyLightingMode.TLM_SURFACE_PER_PIXEL_LIGHTING)
        constant(material, (0.10, 0.32, 0.38), unreal.MaterialProperty.MP_BASE_COLOR, (-450, -160))
        constant(material, 0.28, unreal.MaterialProperty.MP_OPACITY, (-450, 30))
        constant(material, 0.1, unreal.MaterialProperty.MP_ROUGHNESS, (-450, 160))
    elif kind == 'emissive':
        constant(material, (0.04, 3.5, 5.0), unreal.MaterialProperty.MP_EMISSIVE_COLOR, (-450, -100))
        constant(material, (0.02, 0.2, 0.25), unreal.MaterialProperty.MP_BASE_COLOR, (-450, 100))
    elif kind == 'decal':
        material.set_editor_property('material_domain', unreal.MaterialDomain.MD_DEFERRED_DECAL)
        material.set_editor_property('blend_mode', unreal.BlendMode.BLEND_TRANSLUCENT)
        constant(material, (0.5, 0.18, 0.045), unreal.MaterialProperty.MP_BASE_COLOR, (-450, -100))
        constant(material, 0.8, unreal.MaterialProperty.MP_ROUGHNESS, (-450, 90))
        constant(material, 0.55, unreal.MaterialProperty.MP_OPACITY, (-450, 230))
    lib.recompile_material(material)
    if not assets.save_loaded_asset(material):
        raise RuntimeError(f'Cannot save {path}')
    return material


def spawn(cls, name, location, folder, rotation=(0, 0, 0)):
    actor = actors.spawn_actor_from_class(cls, unreal.Vector(*location),
                                          unreal.Rotator(pitch=rotation[0], yaw=rotation[1], roll=rotation[2]))
    actor.set_actor_label(name)
    actor.set_folder_path(folder)
    actor.tags = [unreal.Name('CH01')]
    return actor


def mesh(name, shape, pos, scale, material, folder='01_OpaqueArchitecture', rotation=(0, 0, 0)):
    actor = spawn(unreal.StaticMeshActor, name, pos, folder, rotation)
    actor.static_mesh_component.set_static_mesh(unreal.load_asset('/Engine/BasicShapes/' + shape))
    actor.static_mesh_component.set_material(0, material)
    actor.set_actor_scale3d(unreal.Vector(*scale))
    return actor


def label(name, text, pos, size=32, material=None):
    actor = spawn(unreal.TextRenderActor, name, pos, '05_Signage', (0, 180, 0))
    component = actor.get_component_by_class(unreal.TextRenderComponent)
    component.set_text(text)
    component.set_world_size(size)
    component.set_horizontal_alignment(unreal.HorizTextAligment.EHTA_CENTER)
    component.set_text_render_color(unreal.Color(220, 240, 245, 255))
    if material:
        component.set_text_material(material)
    return actor


if not levels.load_level(MAP):
    raise RuntimeError('CH01 starter map is missing')
for actor in actors.get_all_level_actors():
    if isinstance(actor, (unreal.WorldSettings, unreal.LevelScriptActor)):
        continue
    actors.destroy_actor(actor)

stone = surface('MI_CH01_Sandstone', (0.50, 0.36, 0.23), 0.82)
stone_alt = surface('MI_CH01_SandstoneLight', (0.60, 0.46, 0.31), 0.75)
paving = surface('MI_CH01_Paving', (0.11, 0.135, 0.15), 0.7)
grout = surface('MI_CH01_Grout', (0.035, 0.05, 0.055), 0.9)
metal = surface('MI_CH01_MetalFrame', (0.10, 0.15, 0.18), 0.26, 0.85)
teal = surface('MI_CH01_TealPaint', (0.025, 0.20, 0.21), 0.6)
wood = surface('MI_CH01_Wood', (0.27, 0.105, 0.035), 0.7)
ceramic = surface('MI_CH01_Ceramic', (0.72, 0.31, 0.095), 0.22)
cream = surface('MI_CH01_Cream', (0.8, 0.72, 0.52), 0.4)
glass = special_material('M_CH01_Glass', 'glass')
emissive = special_material('M_CH01_SignEmission', 'emissive')
decal = special_material('M_CH01_WallPatina', 'decal')

mesh('GroundBase', 'Cube', (0, 0, -30), (26, 25, 0.5), grout)
for ix in range(9):
    for iy in range(10):
        mesh(f'Paving_{ix:02d}_{iy:02d}', 'Cube', (-1050+ix*220, -1080+iy*220, 0),
             (2.15, 2.15, 0.08), paving)
mesh('RearWall', 'Cube', (780, 0, 310), (0.4, 17, 6.2), teal)
mesh('InteriorFloor', 'Cube', (580, 0, 30), (4.2, 15, 0.6), wood)
for y in (-780, 0, 780):
    mesh(f'StonePier_{y}', 'Cube', (460, y, 280), (1.4, 1.3, 5.6), stone)
    for z in (70, 180, 290, 400, 510):
        mesh(f'PierJoint_{y}_{z}', 'Cube', (387, y, z), (0.04, 1.32, 0.045), grout)
mesh('StoneLintel', 'Cube', (460, 0, 590), (1.4, 17, 0.8), stone_alt)
mesh('StonePlinth', 'Cube', (455, 0, 65), (1.5, 17, 1.0), stone)
for bay, y in enumerate((-395, 395), 1):
    for side_y in (y-290, y+290):
        mesh(f'WindowFrame_{bay}_{side_y}', 'Cube', (369, side_y, 310), (0.3, 0.16, 4.5), metal)
    for z in (105, 520):
        mesh(f'WindowRail_{bay}_{z}', 'Cube', (369, y, z), (0.3, 5.9, 0.16), metal)
    mesh(f'GlassPane_{bay}', 'Cube', (375, y, 310), (0.025, 5.7, 4.0), glass, '03_Translucency')
    for shelf_z in (150, 325):
        mesh(f'DisplayShelf_{bay}_{shelf_z}', 'Cube', (635, y, shelf_z), (2.4, 5.3, 0.13), wood, '02_OpaqueDisplay')
        for item in range(4):
            item_y = y-200+item*130
            mesh(f'Ceramic_{bay}_{shelf_z}_{item}', 'Sphere', (610, item_y, shelf_z+48),
                 (0.70, 0.70, 0.85), ceramic if item%2 else cream, '02_OpaqueDisplay')
            mesh(f'PotNeck_{bay}_{shelf_z}_{item}', 'Cylinder', (610, item_y, shelf_z+90),
                 (0.28, 0.28, 0.20), ceramic if item%2 else cream, '02_OpaqueDisplay')
mesh('Canopy', 'Cube', (245, 0, 655), (5.4, 18.0, 0.24), teal)
mesh('SignBacking', 'Cube', (362, 0, 590), (0.12, 11, 0.65), metal, '05_Signage')
label('StoreName', 'PIPELINE  /  MATERIAL  LAB', (351, 0, 580), 30)
for y in (-590, 590):
    mesh(f'EmissiveLightBar_{y}', 'Cube', (120, y, 605), (2.0, 0.13, 0.10), emissive, '05_Signage')
for i in range(3):
    mesh(f'Crate_{i}', 'Cube', (50+i*115, 850, 55+i*10), (1.05, 1.05, 1.1+i*0.2), wood, '02_OpaqueDisplay')
    mesh(f'CrateRim_{i}', 'Cube', (50+i*115, 850, 115+i*20), (1.1, 1.1, 0.07), metal, '02_OpaqueDisplay')
for y in (-1050, 1020):
    mesh(f'Bollard_{y}', 'Cylinder', (-320, y, 65), (0.40, 0.40, 1.3), metal)
    mesh(f'BollardBand_{y}', 'Cylinder', (-320, y, 100), (0.41, 0.41, 0.10), cream)
patina = spawn(unreal.DecalActor, 'WallPatina_DBuffer', (382, 0, 270), '04_Decals')
patina.decal.set_decal_material(decal)
patina.decal.set_editor_property('decal_size', unreal.Vector(24, 48, 150))
sun = spawn(unreal.DirectionalLight, 'Sun_Key', (-700, -900, 1000), '06_Lighting', (-38, -32, 0))
sun.light_component.set_mobility(unreal.ComponentMobility.MOVABLE)
sun.light_component.set_intensity(3.0)
sun.light_component.set_editor_property('light_source_angle', 2.0)
for bay, y in enumerate((-395, 395), 1):
    fill = spawn(unreal.PointLight, f'WarmDisplayLight_{bay}', (560, y, 450), '06_Lighting')
    fill.light_component.set_mobility(unreal.ComponentMobility.MOVABLE)
    fill.light_component.set_intensity(80)
    fill.light_component.set_light_color(unreal.LinearColor(1.0, 0.65, 0.35, 1))
    fill.light_component.set_editor_property('attenuation_radius', 650)
    fill.light_component.set_cast_shadows(True)
sky = spawn(unreal.SkyLight, 'Sky_Fill', (0, 0, 900), '06_Lighting')
sky.light_component.set_mobility(unreal.ComponentMobility.MOVABLE)
sky.light_component.set_intensity(0.5)
camera = spawn(unreal.CameraActor, 'CH01_ComparisonCamera', (-1550, -1600, 1000), '07_Cameras', (-17, 40, 0))
camera.camera_component.set_field_of_view(58)
camera.set_editor_property('auto_activate_for_player', unreal.AutoReceiveInput.PLAYER0)
spawn(unreal.PlayerStart, 'PlayerStart', (-1000, -900, 160), '07_Cameras')
post = spawn(unreal.PostProcessVolume, 'CH01_FixedExposure', (0, 0, 0), '08_PostProcess')
post.set_editor_property('unbound', True)
settings = post.get_editor_property('settings')
for key, value in (
    ('override_auto_exposure_method', True),
    ('auto_exposure_method', unreal.AutoExposureMethod.AEM_MANUAL),
    ('override_auto_exposure_apply_physical_camera_exposure', True),
    ('auto_exposure_apply_physical_camera_exposure', False),
    ('override_bloom_intensity', True), ('bloom_intensity', 1.0),
):
    settings.set_editor_property(key, value)
post.set_editor_property('settings', settings)
if not levels.save_current_level():
    raise RuntimeError('Cannot save CH01 experiment')
unreal.log(f'CH01_BUILD_OK actors={len(actors.get_all_level_actors())}')
