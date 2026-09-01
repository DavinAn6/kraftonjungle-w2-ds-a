import heapq

def hIndex(citations):
    
    # paper_count = ciitations.count(max_citations)

    # for paper in citations:
    #     if citations[paper] >= max_citations:
    #         paper_count += 1



    # Gotta iterate grabbing the max citation number until there is nothing left
    # How to ignore duplciate max values
    # Can't remove the max value because we need to check citations later
    # How to jump through largest values without sorting?
    # Maybe just go through duplicates as well... but still how to get next max
    
    # if (sum(citations) == 0):
    #     return 0
    # if (len(citations) == 1):
    #     return 1
    
    # citations_heap = list(citations)
    # heapq._heapify_max(citations_heap)
    
    # while citations_heap:
    #     max_citations = heapq._heappop_max(citations_heap)
    #     h_index = [i for i in citations if i >= max_citations]
    #     if len(h_index) >= max_citations:
    #         return max_citations
    
    # Change directions : decrease number of papers, until there is enough citations to equal
    # Otherwise we need to have tuples of (unique value, # of occurrance)
    
    
    # If n = citations.length, 
    # For i = n~1, find if there are enough values that are >= than i
    
    
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