#写一段python程序来生成并保存xml数据样本。
#xml数据包含道路抽象类，生成若干条不同id的道路，这些道路分别有随机2到10条车道，不同道路有不同的限速，限速为10的倍数。
#xml数据包含车辆抽象类。
#随机生成若干数量的车辆，这些车辆具有不同的id和不同的速度，并且可分为自动驾驶和有人驾驶两种类型。
#这些车辆行驶在不同道路的不同车道上，车辆与车道关系体现在车辆信息中。

import random
from xml.etree.ElementTree import Element, SubElement, Comment, ElementTree

# roadCount = 10
# vehicleCount = 100 * roadCount

def generate_road_element(id, lane_count, max_speed):
    road = Element("road")
    road_id_elem = SubElement(road,'id')
    road_id_elem.text = str(id)
    lane_count_elem = SubElement(road, "laneCount")
    lane_count_elem.text = str(lane_count)
    max_speed_elem = SubElement(road, "maxSpeed")
    max_speed_elem.text = str(max_speed)
    return road

def generate_vehicle_element(id, speed, vehicle_type, road_id, lane):
    vehicle = Element("vehicle")
    vehicle_id = SubElement(vehicle,'id')
    vehicle_id.text = str(id)
    speed_elem = SubElement(vehicle, "speed")
    speed_elem.text = str(speed)
    type_elem = SubElement(vehicle, "type")
    type_elem.text = vehicle_type
    road_elem = SubElement(vehicle, "road")
    road_elem.text = road_id
    lane_elem = SubElement(vehicle, "lane")
    lane_elem.text = str(lane)
    return vehicle

def generate_data():
    roads = []
    vehicles = []

    road_count = roadCount
    for i in range(road_count):
        road_id = "road" + str(i + 1)
        lane_count = random.randint(2, 10)
        max_speed = random.randint(3, 12) * 10
        road = generate_road_element(road_id, lane_count, max_speed)
        roads.append(road)
        vehicle_count = vehicleCount
        for j in range(vehicle_count):
            vehicle_id = "vehicle" + str(i * vehicle_count + j + 1)
            speed = random.randint(30, max_speed)
            vehicle_type = "auto" if random.random() < 0.5 else "human"
            lane = random.randint(1, lane_count)
            vehicle = generate_vehicle_element(vehicle_id, speed, vehicle_type, road_id, lane)
            vehicles.append(vehicle)
    return roads, vehicles

def generate_xml():
    roads, vehicles = generate_data()
    root = Element("data")
    roads_elem = SubElement(root, "roads")
    for road in roads:
        roads_elem.append(road)
    vehicles_elem = SubElement(root, "vehicles")
    for vehicle in vehicles:
        vehicles_elem.append(vehicle)
    return ElementTree(root)

def save_xml(filename):
    xml_doc = generate_xml()
    xml_doc.write(filename, encoding="utf-8", xml_declaration=True)


# for i in range(1,21):
#     roadCount = 100
#     vehicleCount = i * roadCount * 100
#     fileName = 'data' + str(roadCount) + '_' + str(vehicleCount) + '.xml'
#     save_xml(fileName)

for i in range(1,2):
    roadCount = 10
    vehicleCount = i * roadCount * 10
    fileName = 'data' + str(roadCount) + '_' + str(vehicleCount) + '.xml'
    save_xml(fileName)