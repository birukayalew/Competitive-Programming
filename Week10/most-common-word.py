word_counter = {}
        banned_set = set(banned)
        
        temp = []
        for char in paragraph:
            
            if char not in "!?',;.' '":
                temp.append(char)
            else:
                curr = "".join(temp).lower()
                if curr not in banned_set and curr != "":
                    if curr in word_counter:
                        word_counter[curr] += 1
                    else:
                        word_counter[curr] = 1
                temp = []
        maximum = 0
        curr_string = ""
        for key in word_counter:
            if word_counter[key] > maximum:
                curr_string = key
                maximum = word_counter[key]
        return  curr_string
