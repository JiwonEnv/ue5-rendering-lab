"""Capture the existing CH01 level through a real DX12 editor viewport."""
from pathlib import Path
import json
import time
import traceback
import unreal

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / 'Docs/Images/CH01'
OUTPUT.mkdir(parents=True, exist_ok=True)
MAP = '/Game/RenderingLab/Chapters/Part01_RenderingBasics/CH01_RenderingPipeline/Maps/L_CH01_RenderingPipeline'
unreal.EditorPythonScripting.set_keep_python_script_alive(True)
levels = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
actors = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
if not levels.load_level(MAP):
    raise RuntimeError('CH01 level could not be loaded')
all_actors = actors.get_all_level_actors()
camera = next(a for a in all_actors if a.get_actor_label() == 'CH01_ComparisonCamera')
glass = [a for a in all_actors if a.get_actor_label().startswith('GlassPane_')]
decal = next(a for a in all_actors if a.get_actor_label() == 'WallPatina_DBuffer')
post = next(a for a in all_actors if a.get_actor_label() == 'CH01_FixedExposure')
for actor in all_actors:
    if actor.get_actor_label().startswith('WarmDisplayLight_'):
        actor.light_component.set_intensity(80)
decal.set_actor_rotation(unreal.Rotator(pitch=0, yaw=0, roll=0), False)
original_location = camera.get_actor_location()
original_rotation = camera.get_actor_rotation()
original_fov = camera.camera_component.get_editor_property('field_of_view')
world = unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem).get_editor_world()

for command in ('r.VSync 0', 't.MaxFPS 60', 'r.ScreenPercentage 100', 'r.DynamicRes.OperationMode 0'):
    unreal.SystemLibrary.execute_console_command(world, command)
unreal.EditorLevelLibrary.set_level_viewport_camera_info(camera.get_actor_location(), camera.get_actor_rotation())
unreal.AutomationLibrary.set_editor_viewport_view_mode(unreal.ViewModeIndex.VMI_LIT)
unreal.AutomationLibrary.finish_loading_before_screenshot()

shots = [
    ('01_Lit', 'lit'), ('02_BaseColor', 'BaseColor'),
    ('03_WorldNormal', 'WorldNormal'), ('04_SceneDepth', 'SceneDepth'),
    ('05_Roughness', 'Roughness'), ('06_Wireframe', 'wireframe'),
    ('07_GlassOff', 'glass_off'), ('08_BloomOff', 'bloom_off'),
    ('09_DecalOff', 'decal_off'), ('10_LightingOnly', 'lightingonly'),
    ('11_DecalCloseup', 'decal_closeup'), ('12_DecalOffCloseup', 'decal_off_closeup'),
]
state = {'index': 0, 'phase': 'configure', 'deadline': time.monotonic() + 35,
         'task': None, 'started': time.monotonic()}
manifest = {
    'engine': unreal.SystemLibrary.get_engine_version(), 'map': MAP,
    'resolution': [1600, 900], 'capture_type': 'Unreal Editor DX12 viewport',
    'camera_location': [camera.get_actor_location().x, camera.get_actor_location().y, camera.get_actor_location().z],
    'camera_rotation': [camera.get_actor_rotation().pitch, camera.get_actor_rotation().yaw, camera.get_actor_rotation().roll],
    'screen_percentage': 100, 'dynamic_resolution': False,
    'exposure': 'Manual, physical camera exposure disabled',
    'images': [], 'measurement_note': 'Screenshots are visual evidence, not GPU performance benchmarks.',
}


def configure(mode):
    camera.set_actor_location(unreal.Vector(-250, -180, 300) if 'closeup' in mode else original_location, False, False)
    camera.set_actor_rotation(unreal.Rotator(pitch=0, yaw=16, roll=0) if 'closeup' in mode else original_rotation, False)
    camera.camera_component.set_field_of_view(45 if 'closeup' in mode else original_fov)
    for actor in glass:
        actor.set_is_temporarily_hidden_in_editor(mode == 'glass_off')
    decal.set_is_temporarily_hidden_in_editor(mode in ('decal_off', 'decal_off_closeup'))
    settings = post.get_editor_property('settings')
    settings.set_editor_property('bloom_intensity', 0.0 if mode == 'bloom_off' else 1.0)
    post.set_editor_property('settings', settings)
    enum = {'wireframe': unreal.ViewModeIndex.VMI_WIREFRAME,
            'lightingonly': unreal.ViewModeIndex.VMI_LIGHTING_ONLY}
    if mode in ('BaseColor', 'WorldNormal', 'SceneDepth', 'Roughness'):
        unreal.AutomationLibrary.set_editor_viewport_visualize_buffer(mode)
    else:
        unreal.AutomationLibrary.set_editor_viewport_view_mode(enum.get(mode, unreal.ViewModeIndex.VMI_LIT))
    unreal.AutomationLibrary.finish_loading_before_screenshot()


def finish(success):
    unreal.unregister_slate_post_tick_callback(handle)
    configure('lit')
    # Revert all transient A/B changes before saving the final level.
    levels.save_current_level()
    manifest['complete'] = success
    (OUTPUT / 'CaptureManifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    unreal.log('CH01_CAPTURE_OK' if success else 'CH01_CAPTURE_FAILED')
    unreal.EditorPythonScripting.set_keep_python_script_alive(False)
    unreal.SystemLibrary.quit_editor()


def tick(delta):
    try:
        now = time.monotonic()
        if now - state['started'] > 900:
            raise RuntimeError('Capture session exceeded 15 minutes')
        if now < state['deadline']:
            return
        if state['index'] >= len(shots):
            finish(True)
            return
        name, mode = shots[state['index']]
        if state['phase'] == 'configure':
            configure(mode)
            state['phase'] = 'capture'
            state['deadline'] = time.monotonic() + 10
            unreal.log(f'CH01_CAPTURE_CONFIGURED {name}')
        elif state['phase'] == 'capture':
            state['task'] = unreal.AutomationLibrary.take_high_res_screenshot(
                1600, 900, str(OUTPUT / (name + '.png')), camera=camera, delay=2.0)
            state['phase'] = 'waiting'
            state['deadline'] = time.monotonic() + 4
        elif state['task'].is_task_done():
            path = OUTPUT / (name + '.png')
            if not path.exists() or path.stat().st_size == 0:
                raise RuntimeError(f'Capture file is missing: {path}')
            location = camera.get_actor_location()
            rotation = camera.get_actor_rotation()
            manifest['images'].append({'file': path.name, 'mode': mode,
                                       'camera_location': [location.x, location.y, location.z],
                                       'camera_rotation': [rotation.pitch, rotation.yaw, rotation.roll],
                                       'field_of_view': camera.camera_component.get_editor_property('field_of_view')})
            unreal.log(f'CH01_CAPTURE_SAVED {path.name}')
            state['index'] += 1
            state['phase'] = 'configure'
            state['deadline'] = time.monotonic() + 1
    except Exception:
        unreal.log_error(traceback.format_exc())
        finish(False)


handle = unreal.register_slate_post_tick_callback(tick)
unreal.log('CH01_CAPTURE_STARTED')
