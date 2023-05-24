import xml.etree.ElementTree as ET
import datetime
# #解析XML文件
# tree = ET.parse('data10_1000.xml') 
# root = tree.getroot()
# #获取所有车辆元素
# vehicles = root.findall(".//vehicle")

#根据道路id检索车辆id
def search_vehicle_id(road_id): 
    start_time = datetime.datetime.now()
    vehicle_ids = [] 
    for vehicle in vehicles: 
        road_elem = vehicle.find("road") 
        if road_elem.text == road_id: 
            vehicle_ids.append(vehicle.find('id').text)
    end_time = datetime.datetime.now() 
    time_diff = (end_time - start_time).microseconds
    # print("检索用时：{}微秒".format(time_diff)) 
    return time_diff


res = []
for i in range(1,11):
    tmp = []
    #解析XML文件
    fileName = 'dataR' + str(i*100) + '_10000.xml'
    tree = ET.parse(fileName) 
    root = tree.getroot()

    #获取所有车辆元素
    vehicles = root.findall(".//vehicle")
    for j in range(1,100*i+1):
        roadName = 'road' + str(j)
        time_diff = search_vehicle_id(roadName)
        # print("检索用时：{}微秒".format(time_diff)) 
        tmp.append(time_diff)
    tmpSum = sum(tmp) / 1000
    print('道路数量为', i * 100, '时的查询用时为：', tmpSum, '毫秒' )
    res.append(tmpSum)
print(res)


# i = 5
# res = 0
# #解析XML文件
# fileName = 'dataR' + str(i*100) + '_10000.xml'
# tree = ET.parse(fileName) 
# root = tree.getroot()
# #获取所有车辆元素
# vehicles = root.findall(".//vehicle")
# for j in range(1,100*i+1):
#     roadName = 'road' + str(j)
#     time_diff = search_vehicle_id(roadName)
#     res += time_diff / 1000
#     print('累计用时：', res, '毫秒')
# print('车辆数量为', i * 10000, '时的查询用时为：', res, '毫秒' )


# i = 7
# #解析XML文件
# fileName = 'data100_' + str(i*10000) + '.xml'
# tree = ET.parse(fileName) 
# root = tree.getroot()

# #获取所有车辆元素
# vehicles = root.findall(".//vehicle")
# a = datetime.datetime.now()
# for j in range(1,101):
#     roadName = 'road' + str(j)
#     time_diff = search_vehicle_id(roadName)
# b = datetime.datetime.now()
# c = (b-a).microseconds / 1000
# print('车辆数量为', i * 10000, '时的查询用时为：', c, '毫秒' )