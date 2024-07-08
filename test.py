import carla
import random


client = carla.Client('localhost', 2000)
world = client.load_world('Town01')

vehicle_blueprints = world.get_blueprint_library().filter('*vehicle*')

spawn_points = world.get_map().get_spawn_points()

for bp in world.get_blueprint_library().filter('vehicle'):
    print(bp.id)

ego_bp = world.get_blueprint_library().find('vehicle.audi.etron')

ego_bp.set_attribute('role_name', 'hero')

ego_vehicle = world.spawn_actor(ego_bp, random.choice(spawn_points))

for vehicle in world.get_actors().filter('*vehicle*'):
    vehicle.set_autopilot(True)