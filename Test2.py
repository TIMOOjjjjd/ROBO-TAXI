import subprocess
import time

import carla
import random

import keyboard
from pygame.locals import K_BACKSPACE, K_p
import pygame
vehicle_ids = []  # 初始化一个空的列表，用于存储生成的载具的ID


# 连接到 Carla 客户端并加载 Town01 地图
client = carla.Client('localhost', 2000)
world = client.load_world('Town01')
# world = client.get_world
# 获取可用的生成点
spawn_points = world.get_map().get_spawn_points()


settings = world.get_settings()
settings.synchronous_mode = True
settings.fixed_delta_seconds = 0.05
world.apply_settings(settings)

# Traffic Manager 设置
traffic_manager = client.get_trafficmanager()
tm_port = traffic_manager.get_port()
autopilot_enabled = False
pygame.init()
# 创建批量生成车辆的命令
batch = []
blueprint_library = world.get_blueprint_library()
# subprocess.Popen(["python", "C:/3rd year project/carla/WindowsNoEditor/PythonAPI/examples/manual_control.py"])
for _ in range(10):
    spawn_point = random.choice(spawn_points) if spawn_points else carla.Transform()
    vehicle_bp = random.choice(blueprint_library.filter('vehicle.*'))
    npc = world.try_spawn_actor(vehicle_bp, spawn_point)
    if npc:
        print("Vehicle spawned.")
    else:
        print("Vehicle could not be spawned.")

    npc.set_autopilot(True)
settings.synchronous_mode = False
settings.fixed_delta_seconds = None
world.apply_settings(settings)
traffic_manager.set_synchronous_mode(False)
time.sleep(300)


# while (True):
    #     if keyboard.is_pressed('a'):
    #         print('1111')
    #         time.sleep(2)
# 应用生成的载具并设置为自动驾驶模式
# for response in client.apply_batch_sync(batch):
#     if response.error:
#         print(f"Failed to spawn vehicle: {response.error}")
#     else:
#         actor_id = response.actor_id
#         vehicle_ids.append(actor_id)
#
#         # 获取生成的车辆并设置为自动驾驶模式
#         vehicle = world.get_actor(actor_id)
#         if vehicle:
#             vehicle.set_autopilot(True)
#             print(f"Vehicle {actor_id} set to autopilot.")
#         else:
#             print(f"Failed to find vehicle with ID {actor_id}.")

# 检查并打印所有车辆的ID
# print("All vehicle IDs:", vehicle_ids)


# for event in pygame.event.get():
#         if event.type == pygame.KEYUP:
#
#             if event.key == K_p:
#                 if autopilot_enabled:
#                     npc.set_autopilot(False)
#                     world.hud.notification('now off')
#                 else:
#                     npc.set_autopilot(True)
#                     world.hud.notification('now off')
#
# while(True):
#     for event in pygame.event.get():
#             if event.type == pygame.KEYUP:
#
#                 if event.key == K_p:
#                     if autopilot_enabled:
#                         npc.set_autopilot(False)
#                         world.hud.notification('now off')
#                     else:
#                         npc.set_autopilot(True)
#                         world.hud.notification('now off')

# 允许一些时间来观察结果
