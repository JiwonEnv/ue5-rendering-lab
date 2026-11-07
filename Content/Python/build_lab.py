"""Create missing starter maps inside Unreal Editor, preserving existing assets."""
from pathlib import Path
import json
import unreal


ROOT = Path(__file__).resolve().parents[2]
CONTENT = '/Game/RenderingLab'
assets = unreal.EditorAssetLibrary
tools = unreal.AssetToolsHelpers.get_asset_tools()
levels = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
actors = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)


def get_surface():
    path = f'{CONTENT}/Common/Materials/M_LabSurface'
    if assets.does_asset_exist(path):
        return unreal.load_asset(path)
    material = tools.create_asset('M_LabSurface', f'{CONTENT}/Common/Materials',
                                  unreal.Material, unreal.MaterialFactoryNew())
    if material is None:
        raise RuntimeError('Cannot create shared surface material')
    library = unreal.MaterialEditingLibrary
    color = library.create_material_expression(material, unreal.MaterialExpressionVectorParameter, -420, -160)
    color.set_editor_property('parameter_name', 'BaseColor')
    color.set_editor_property('default_value', unreal.LinearColor(0.12, 0.28, 0.34, 1))
    library.connect_material_property(color, '', unreal.MaterialProperty.MP_BASE_COLOR)
    for name, value, prop, y in (
        ('Metallic', 0.0, unreal.MaterialProperty.MP_METALLIC, 30),
        ('Roughness', 0.45, unreal.MaterialProperty.MP_ROUGHNESS, 180),
    ):
        node = library.create_material_expression(material, unreal.MaterialExpressionScalarParameter, -420, y)
        node.set_editor_property('parameter_name', name)
        node.set_editor_property('default_value', value)
        library.connect_material_property(node, '', prop)
    library.recompile_material(material)
    if not assets.save_loaded_asset(material):
        raise RuntimeError('Cannot save shared surface material')
    return material


def get_instance(name, color, roughness, metallic=0.0):
    path = f'{CONTENT}/Common/Materials/{name}'
    if assets.does_asset_exist(path):
        return unreal.load_asset(path)
    instance = tools.create_asset(name, f'{CONTENT}/Common/Materials',
                                 unreal.MaterialInstanceConstant,
                                 unreal.MaterialInstanceConstantFactoryNew())
    library = unreal.MaterialEditingLibrary
    library.set_material_instance_parent(instance, surface)
    library.set_material_instance_vector_parameter_value(instance, 'BaseColor', unreal.LinearColor(*color, 1))
    library.set_material_instance_scalar_parameter_value(instance, 'Roughness', roughness)
    library.set_material_instance_scalar_parameter_value(instance, 'Metallic', metallic)
    if not assets.save_loaded_asset(instance):
        raise RuntimeError(f'Cannot save {path}')
    return instance


def spawn(cls, name, location, rotation=(0, 0, 0), folder='Environment'):
    orientation = unreal.Rotator(pitch=rotation[0], yaw=rotation[1], roll=rotation[2])
    actor = actors.spawn_actor_from_class(cls, unreal.Vector(*location), orientation)
    if actor is None:
        raise RuntimeError(f'Cannot spawn {name}')
    actor.set_actor_label(name)
    actor.set_folder_path(folder)
    return actor


def mesh(name, shape, location, scale, material, folder):
    actor = spawn(unreal.StaticMeshActor, name, location, folder=folder)
    actor.static_mesh_component.set_static_mesh(unreal.load_asset(f'/Engine/BasicShapes/{shape}'))
    actor.static_mesh_component.set_material(0, material)
    actor.set_actor_scale3d(unreal.Vector(*scale))
    return actor


def text(name, value, location, size):
    actor = spawn(unreal.TextRenderActor, name, location, (0, 180, 0), 'Instructions')
    component = actor.get_component_by_class(unreal.TextRenderComponent)
    component.set_text(value)
    component.set_world_size(size)
    component.set_horizontal_alignment(unreal.HorizTextAligment.EHTA_CENTER)
    component.set_text_render_color(unreal.Color(225, 240, 245, 255))
    return actor


def create_map(path, heading, instruction):
    if assets.does_asset_exist(path):
        unreal.log(f'LAB_KEEP {path}')
        return False
    if not levels.new_level(path):
        raise RuntimeError(f'Cannot create level {path}')
    mesh('Floor', 'Cube', (0, 0, -20), (14, 14, 0.4), floor, 'Environment')
    mesh('Backdrop', 'Cube', (400, 0, 240), (0.3, 14, 5.2), floor, 'Environment')
    for index, y in enumerate((-260, 0, 260)):
        mesh(f'ComparisonPedestal_{index+1}', 'Cube', (0, y, 35),
             (1.8, 1.8, 0.7), floor, 'ComparisonStage')
        mesh(f'ComparisonSphere_{index+1}', 'Sphere', (0, y, 130),
             (1.25, 1.25, 1.25), samples[index], 'ComparisonStage')
    light = spawn(unreal.DirectionalLight, 'KeyLight', (-300, -200, 500), (-35, -30, 0), 'Lighting')
    light.light_component.set_mobility(unreal.ComponentMobility.MOVABLE)
    light.light_component.set_intensity(4)
    sky = spawn(unreal.SkyLight, 'FillLight', (0, 0, 450), folder='Lighting')
    sky.light_component.set_mobility(unreal.ComponentMobility.MOVABLE)
    camera = spawn(unreal.CameraActor, 'ComparisonCamera', (-1100, 0, 380), (-12, 0, 0), 'Cameras')
    camera.camera_component.set_field_of_view(65)
    camera.set_editor_property('auto_activate_for_player', unreal.AutoReceiveInput.PLAYER0)
    spawn(unreal.PlayerStart, 'PlayerStart', (-950, 0, 140), folder='Cameras')
    post = spawn(unreal.PostProcessVolume, 'FixedExposure', (0, 0, 0), folder='Lighting')
    post.set_editor_property('unbound', True)
    settings = post.get_editor_property('settings')
    settings.set_editor_property('override_auto_exposure_method', True)
    settings.set_editor_property('auto_exposure_method', unreal.AutoExposureMethod.AEM_MANUAL)
    settings.set_editor_property('override_auto_exposure_apply_physical_camera_exposure', True)
    settings.set_editor_property('auto_exposure_apply_physical_camera_exposure', False)
    post.set_editor_property('settings', settings)
    text('ChapterTitle', heading, (350, 0, 365), 42)
    text('StarterStatus', 'STARTER LEVEL - Build the chapter experiment here', (340, 0, 310), 20)
    text('LabInstructions', instruction, (330, 0, 255), 17)
    if not levels.save_current_level():
        raise RuntimeError(f'Cannot save level {path}')
    unreal.log(f'LAB_CREATED {path}')
    return True


chapters = json.loads((ROOT / 'Docs/chapters.json').read_text(encoding='utf-8'))
surface = get_surface()
floor = get_instance('MI_LabFloor', (0.045, 0.065, 0.075), 0.8)
samples = [
    get_instance('MI_LabMatte', (0.08, 0.30, 0.35), 0.8),
    get_instance('MI_LabGloss', (0.08, 0.30, 0.35), 0.18),
    get_instance('MI_LabMetal', (0.65, 0.42, 0.18), 0.25, 1.0),
]
created = []
for chapter in chapters:
    if create_map(chapter['map'], f"{chapter['id']} - {chapter['slug']}",
                  f"Read Docs/Chapters/{chapter['folder']}.md"):
        created.append(chapter['id'])
lobby = f'{CONTENT}/Maps/L_RenderingLab'
create_map(lobby, 'UE5 RENDERING LAB', 'Open a chapter map from RenderingLab/Chapters. See README for the learning order.')
if not levels.load_level(lobby):
    raise RuntimeError('Cannot load the project startup level')
missing = [c['map'] for c in chapters if not assets.does_asset_exist(c['map'])]
if missing:
    raise RuntimeError(f'Missing chapter maps: {missing}')
unreal.log(f'LAB_BUILD_OK chapters={len(chapters)} created={len(created)}')
