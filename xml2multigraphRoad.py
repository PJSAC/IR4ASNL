import networkx as nx
import xml.etree.ElementTree as ET
import pickle

def create_graph(filename):
    G = nx.MultiGraph()
    tree = ET.parse(filename)
    root = tree.getroot()
    roadRoot = root.find('roads')
    vehicleRoot = root.find('vehicles')
    roads_dict = dict()
    for road in roadRoot.iter('road'):
        road_id = road.find('id').text
        lanes = int(road.find('laneCount').text)
        roads_dict[road_id] = {'lanes': lanes}

    # add roads as nodes to graph
    for road_id in roads_dict:
        G.add_node(road_id, type = 'road', **roads_dict[road_id])

    # add vehicles as nodes to graph
    for vehicle in vehicleRoot.iter('vehicle'):
        road_id = vehicle.find('road').text
        lane = int(vehicle.find('lane').text)
        vehicle_id = vehicle.find('id').text
        vehicle_type = vehicle.find('type').text
        speed = int(vehicle.find('speed').text)
        G.add_node(vehicle_id, type = 'vehicle', vehicletype=vehicle_type, speed=speed)
        G.add_edge(vehicle_id, road_id, lane=lane)

    return G

def save_graph(G, fn):
    # nx.write_gexf(G, fn + '.gexf')
    with open(fileName + '_m.pickle', 'wb') as f:
        pickle.dump(G, f)


# fileName = 'data1000_100000'
# G = create_graph(fileName + '.xml')
# save_graph(G, fileName)

for i in range(1,11):
    roadCount = 100 * i
    vehicleCount = 10000
    fileName = 'dataR' + str(roadCount) + '_' + str(vehicleCount)
    G = create_graph(fileName + '.xml')
    save_graph(G, fileName)