import sys


sys.setrecursionlimit(100000)
class Node():
    def __init__(self,value,left=None,right=None,parent=None):
        self.value=value
        self.left=left
        self.right=right

num_list=[int(line.strip()) for line in sys.stdin]
node_dict={}

def makeNodes(arr_list): # 숫자 배열을 넣고 그 배열의 루트값을 갖는 노드 객체를 출력하는 함수
    if not arr_list:
        return None
    root=arr_list[0]
    node_dict[root]=Node(root) # 노드를 사용하려면 초기화 부터하고, 각 property들을 채워주면 됩니다.
    thisNode=node_dict[root]
    more=[]
    less=[]
    for i in range(1,len(arr_list)): # 작은수들과 큰수들을 각각의 배열에 저장합니다.
        num=arr_list[i]
        more.append(num) if num>root else less.append(num)
    
    thisNode.left=makeNodes(less)
    thisNode.right=makeNodes(more)

    return thisNode
    # 맨 앞의 수를 노드로 정합니다.
    # 안정 배열을 지키며 작은수들과 큰수들의 배열을 만들어 저장합니다.
    # 작은 수들을 가지고 하위 트리를 구성하게끔 합니다. (재귀)

def postorder(root_node): # 루트 노드객체를 받으면 후위순회를 출력합니다.
    if root_node:
        postorder(root_node.left)
        postorder(root_node.right)
        print(root_node.value)

postorder(makeNodes(num_list))

# 언제끝날지 모른다면 그냥 read를 쓰자
# 테스트할때는 ctrl+z 하고 엔터 하면 EOF 생성

# 트리를 만드는 과정을 공부할 수 있는 문제였음.
# 후위 순회도는 방법은 이전 문제에서 배우면 될듯