#сортування вибором за спаданням

def SortbyChoiceDesc(array):  
    for i in range(len(array)):
        max_index = i
        for j in range(i+1, len(array)):  
            if array[j] > array[max_index]:
                max_index = j
        array[i], array[max_index] = array[max_index], array[i]    
    return array
                  
arr = [64, 25, 12, 22, 11, 111, 122, 111, 55, 22, 2, 2, 3, 4, 6,7]
sorted_arr = SortbyChoiceDesc(arr)

    
    
def SortbyInsert(array):
    
    for i in range(len(array)):
        index_f = len(array) - 1 - i        
        for j in range(len(array)):   
            index_s = index_f - j - 1 
            if array[index_s] < array[index_f] and index_s >= 0: 
                array[index_s], array[index_f] = array[index_f], array[index_s]  
                                                            
    return array
arr1 = [64, 25, 12, 22, 11, 111, 122, 11546541, 5, 22]          
sorted_arr1 = SortbyInsert(arr1)
print(sorted_arr1)

      
        
        