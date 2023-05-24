import networkx as nx
import pickle
import datetime

# fileName = 'data1000_100000'
# road_id = 'road1'
# with open(fileName + '.pickle', 'rb') as f:
#     G = pickle.load(f)

def search_vehicle_id(road_id):
    start_time = datetime.datetime.now()
    ngb = G.neighbors(road_id)
    res = []
    for n in ngb:
        if G.nodes[n]['type'] == 'vehicle':
            res.append(n)
    end_time = datetime.datetime.now() 
    time_diff = (end_time - start_time).microseconds
    # print("检索用时：{}微秒".format(time_diff)) 
    return time_diff,res



res = []
for i in range(1,11):
    tmp = []
    #解析XML文件
    fileName = 'dataR' + str(i*100) + '_10000'
    # G = nx.read_gexf(fileName + '.gexf')
    with open(fileName + '_m.pickle', 'rb') as f:
        G = pickle.load(f)
    for j in range(1,i*100+1):
        roadName = 'road' + str(j)
        time_diff,_ = search_vehicle_id(roadName)
        # print("检索用时：{}微秒".format(time_diff)) 
        tmp.append(time_diff)
    tmpSum = sum(tmp)/1000
    print('道路数量为', i * 100, '时的查询用时为：', tmpSum , '毫秒')
    res.append(tmpSum)
print(res)


# i = 10
# tmp = []
# #解析XML文件
# fileName = 'dataR' + str(i*100) + '_10000'
# # G = nx.read_gexf(fileName + '_m.pickle')
# with open(fileName + '_m.pickle', 'rb') as f:
#     G = pickle.load(f)
# for j in range(1,i*100+1):
#     roadName = 'road' + str(j)
#     time_diff,_ = search_vehicle_id(roadName)
#     # print("检索用时：{}微秒".format(time_diff)) 
#     tmp.append(time_diff)
# tmpSum = sum(tmp)/1000
# print('道路数量为', i * 100, '时的查询用时为：', tmpSum , '毫秒')