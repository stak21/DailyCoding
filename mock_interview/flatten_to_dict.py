def solution(arr):
    hash_map = {}
    for node in arr:
        parent_id = node['parent']
        if parent_id not in hash_map:
            hash_map[parent_id] = []
        hash_map[parent_id].append(node)

    ret_arr = hash_map.get(0)
    for node in arr:
        node_id = node['id']
        node['children'] = hash_map.get(node_id, [])

    return ret_arr
        

    #  def dfs(arr, target):
        #  if not arr:
            #  return
        #  # iterate through the children of arr as file
        #  for file in arr:
            #  if file['id'] == 3:
                #  print(file)
            #  if target is file['id']:
                #  return file
            #  file = dfs(file['children'], target)
            #  if file:
                #  return file
    #  def dfs(arr, path):
        #  if not arr:
            #  return
        #  # iterate through the children of arr as file
        #  for file in arr:
            #  if path[0] is file['id']:
                #  if len(path) == 1:
                    #  return file
                #  subfolder = dfs(file['children'], path[1:])
                #  if subfolder:
                    #  return subfolder 
        
    #  if not arr:
        #  return []
    #  # sorted(arr, key=lambda node: node['parent'])
    #  folder = []
    #  path = []
    #  memory = {}
    #  for node in arr:
        #  node['children'] = []
        #  parent = node['parent']
        #  memory[node['id']] = parent
        #  if parent == 0:
            #  folder.append(node)
        #  else:
            #  path = [parent]
            #  # Creates a path to look for the target subfolder
            #  while True:
                #  memory_parent = memory.get(path[0])
                #  if memory_parent is not None and memory_parent == 0:
                    #  break
                #  path.insert(0, memory_parent)
            #  sub = dfs(folder, path)
            #  sub['children'].append(node)


            #  #  parent = node['parent']
            #  #  file = dfs(folder, parent)
            #  #  if file:
                #  #  file['children'].append(node)

    #  return folder
    
    
    
arr = [
    {'id':1 ,'parent' : 0},
    {'id':5 ,'parent' : 0},
    {'id':6 ,'parent' : 0},
    {'id':3 ,'parent' : 1},
    {'id':2 ,'parent' : 1},
    {'id':8 ,'parent' : 1},
    {'id':4 ,'parent' : 2},
    {'id':7 ,'parent' : 4}
]

result = solution(arr)


import json
def pprint(data):
    print(json.dumps(data, indent=4, sort_keys=True))
    
    
pprint(result)
