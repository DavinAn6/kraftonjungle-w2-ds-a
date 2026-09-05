"""
[위상 정렬 - Topological Sort]

문제 설명:
- 방향 그래프에서 순서를 정합니다.
- 선행 작업이 먼저 오도록 정렬합니다.
- 예: 과목 선수과목, 작업 순서

입력:
- graph: 방향 그래프
- vertices: 정점 개수

출력:
- 위상 정렬 순서

예제:
과목:
0(기초) → 1(중급) → 3(고급)

0(기초) → 2(응용)

위상 정렬: [0, 1, 2, 3] 또는 [0, 2, 1, 3]

힌트:
- 진입 차수(in-degree) 사용
- 진입 차수가 0인 정점부터 시작
- 큐 사용
"""

from collections import deque

def topological_sort(vertices, edges):
    """
    위상 정렬 (Kahn's Algorithm)
    
    Args:
        vertices: 정점 개수
        edges: (출발, 도착) 간선 리스트
    
    Returns:
        위상 정렬 순서
    """
    
    """ [Topological Sorting using BFS - Kahn's Algorithm]
        1. Compute the in-degree of every vertex — representing how many incoming edges each vertex has. 
        
        2. Then, all vertices with an in-degree of 0 are added to a queue, as they can appear first in the ordering.
        
        3. We repeatedly remove a vertex from the queue, add it to our result list, 
        and reduce the in-degree of all its adjacent vertices. 
        
        4. If any of those vertices now have an in-degree of 0, they are added to the queue.
        
        5. This process continues until the queue is empty, 
        and the resulting order represents one valid topological sort of the graph.
    """
    
    # TODO: 그래프와 진입 차수 초기화.
    # TODO: 그래프 구성 및 진입 차수 계산
    """ Note
    - Compute the in-degree of every vertex. i.e. count how many times vergex occurs in edge list tuple's [1]
    - in_degree list : Each index represents vertex. Values are the in_degree count
    
    edges = [
        (0, 1),  # 0 → 1
        (0, 2),  # 0 → 2
        (1, 3),  # 1 → 3
        ]
    indegree = {'0': 0, '1': 1, '2': 1, '3': 1}
    """
    in_degree = {}
    for v in range(vertices):
        in_degree[v] = 0
    for e in edges:
        in_degree[e[1]] = in_degree.get(e[1], 0) + 1    # If e[1] isn't a key .get() returns 0
    
    # TODO: 진입 차수가 0인 정점들을 큐에 추가
    dq = deque()
    queue_vertex = []
    for i in in_degree.keys():
        if in_degree.get(i) == 0:
            dq.append(i)        # add vertex with in_degree 0 to queue
            queue_vertex.append(i)
    
    for j in queue_vertex:
        del in_degree[j]    # remove vertex from in_degree data
    queue_vertex.clear()
    
    result = []
    # TODO: 큐가 빌 때까지 반복
    ## 큐에서 정점 꺼내기
    ## 인접한 정점들의 진입 차수 감소
    while len(dq) > 0:
    # for n in range(2):
        # Remove vertex from queue
        vertex = dq.popleft()
        result.append(vertex)
        
        # Reduce in_degree of vertices dependent on removed vertex
        for e in edges:
            if e[0] == vertex:
                in_degree[e[1]] = in_degree.get(e[1], 0) - 1
        
        for i in in_degree.keys():
            if in_degree[i] == 0:
                dq.append(i)
                queue_vertex.append(i)
                
        for j in queue_vertex:
            del in_degree[j]    
        queue_vertex.clear()
        
    return result







# 테스트 케이스
if __name__ == "__main__":
    # 과목 선수과목 예제
    vertices = 4
    edges = [
        (0, 1),  # 0 → 1
        (0, 2),  # 0 → 2
        (1, 3),  # 1 → 3
    ]
    
    print("=== 위상 정렬 ===")
    print("과목 관계:")
    print("  0(기초) → 1(중급) → 3(고급)")
    print("  0(기초) → 2(응용)")
    print()
    
    result = topological_sort(vertices, edges)
    print(f"수강 순서: {result}")
