import heapq

""" 
Given an array of integers citations where citations[i] is the number of citations a researcher received for their i(th) paper, return the researcher's h-index.
According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.
Constraints:
  - n == citations.length
  - 1 <= n <= 5000
  - 0 <= citations[i] <= 1000
  
The h-index is the largest h such that h articles have at least h citations each. 
For example, if an author has five publications, with 9, 7, 6, 2, and 1 citations (ordered from greatest to least), 
then the author's h-index is 3, because the author has three publications with 3 or more citations. 
However, the author does not have four publications with 4 or more citations.
"""

def hIndex(citations):

    """ 
    TRIAL 1:
        - Let n = citations.length
        - For i = n~1, find if there are enough values that are >= than i
        
    CODE:
        for i in range(len(citations), -1, -1):
        h_index = [j for j in citations if j >= i]
        if len(h_index) >= i:
            return i
    
    PERFORMANCE: 268ms
        - Solution accepted, but takes 268ms runtime (beats 5.00%).
        - Needs refactoring to make runtime close to 0.
    ————————————————————————————————————————————————————————————————————————————————
    TRIAL 2:
        - max heap 생성 > 최대값 뽑을 때마다 해당 값보다 작은 값이 몇번 발생하는지 확인 > 두 값 중 최소를 리스트에 넣음 > 리스트에서 최댓값 리턴
    
    CODE:
        citations_heap = list(citations)
        heapq._heapify_max(citations_heap)
        h_index = []
        
        while citations_heap:
            max_citations = heapq._heappop_max(citations_heap)
            count = sum(1 for i in citations if i >= max_citations)
            h_index.append(min(max_citations, count))
    
        return max(h_index)
        
    PERFORMANCE: 593ms
        - 어떻게 런타임이 증가...;;
    ————————————————————————————————————————————————————————————————————————————————
    TRIAL 3:
        - 리스트 정렬 > 그래프 안에서 제일 큰 정사각형을 찾는다고 생각 > 앞에서부터 시작해서 정사각형이 더 이상 안될때까지 숫자 증가

    CODE:
        citations.sort(reverse=True)
        count = 0
        for i in citations:
            if count < i:
                count += 1
            else:
                break
        return count

    PERFORMANCE: 2ms
        - Beats 26.23%

    """
    
    citations.sort(reverse=True)
    count = 0
    for i in citations:
        if count < i:
            count += 1
        else:
            break
    return count
        

citations1 = [1, 3, 1]                      # h_index = 1
citations2 = [0]                            # h_index = 0
citations3 = [0, 0, 0, 0]                   # h_index = 0
citations4 = [100]                          # h_index = 1
citations5 = [10, 10, 10, 10, 10, 1, 1, 1]  # h_index = 5
citations6 = [3, 0 ,6, 1, 5]                # h_index = 3
print(hIndex(citations1))
print(hIndex(citations2))
print(hIndex(citations3))
print(hIndex(citations4))
print(hIndex(citations5))
print(hIndex(citations6))