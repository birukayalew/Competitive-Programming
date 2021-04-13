class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        existing_names = {}             #contains used folder names
        for index,name in enumerate(names):
            if name in existing_names:    
                k = existing_names[name] + 1
                new_name = name + '(' + str(k) + ')'  #adding a new suffix
                if new_name in existing_names:    #f we have used newname before 
                    while new_name in existing_names: #continue till u get unused newname
                        k += 1
                        new_name = name + '(' + str(k) + ')'
                existing_names[name] = k
                names[index] = new_name  #update our names holder with the newname
                existing_names[new_name] = 0
            else:   # if name is not used, no need to add suffix
                existing_names[name] = 0
                
        return names
    
    
                
