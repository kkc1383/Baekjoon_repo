import sys

class Node:
    def __init__(self, value, left=None, right=None): # 없을 경우 default값 명시하는 것도 하나의 팁!
        self.value=value
        self.left=left
        self.right=right

n=int(sys.stdin.readline().strip())
node_dict={}

for _ in range(n):
    value, left, right=sys.stdin.readline().strip().split()
    if value not in node_dict: # 넣으려는 value가 dict에 없을 경우
        node_dict[value]=Node(value)
    temp=node_dict[value] # temp가 해당 노드의 객체를 대변하고 있음

    if left!='.': # 왼쪽 자식이 점이 아니면
        if left not in node_dict: # 노드를 중복생성하지 않도록
            node_dict[left]=Node(left) # left 값에 해당하는 노드 생성
        temp.left=node_dict[left] # 그 노드 객체를 dict에 저장 이미 있더라도 left 설정은 해야 하니까

    if right!='.': # 오른쪽 자식이 점이 아니면
        if right not in node_dict:
            node_dict[right]=Node(right)
        temp.right=node_dict[right]



def preorder(root_node): # 입력은 Node 객체 출력은 따로 없고 조건에 따른 print
    if root_node: # 노드가 있으면
        print(root_node.value, end="")
        preorder(root_node.left)
        preorder(root_node.right)

def inorder(root_node): # 입력은 Node 객체 출력은 따로 없고 조건에 따른 print
    if root_node: # 노드가 있으면            
        inorder(root_node.left)
        print(root_node.value, end="")
        inorder(root_node.right)

def postorder(root_node): # 입력은 Node 객체 출력은 따로 없고 조건에 따른 print
    if root_node: # 노드가 있으면          
        postorder(root_node.left)
        postorder(root_node.right)
        print(root_node.value, end="")

preorder(node_dict['A'])
print()
inorder(node_dict['A'])
print()
postorder(node_dict['A'])

# 본 노드 밑에 자식이 없다면 각 재귀함수를 바로 탈출한다는 사실을 알아두면 이해할 수 있을 것이다.
# 어짜피 왼쪽 봤다가 오른쪽 보는 것은 정해져 있는데 언제 출력을 하는지에 따라 차이가 있음.
# 이제 슬슬 property얘기도 나오고 객체를 서로 넘기고 하다보니 생각보다 복잡하다
# 풀다보니 중요한거 같은데 None 객체에 property를 접근하지 않도록 주의하는것이 중요함

# 어렵지 않은 문제이지만 개념을 알지 못하면 전혀 풀수 없는 문제