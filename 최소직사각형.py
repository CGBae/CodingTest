def solution(sizes):
    answer = 0
    max_width = max_height = 0
    
    for size in sizes:
        width, height = size
        max_width = max(max_width, max(width, height))
        max_height = max(max_height, min(width, height))
        
    answer = max_width * max_height
        
    return answer
