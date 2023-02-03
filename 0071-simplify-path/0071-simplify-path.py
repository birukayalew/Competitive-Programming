class Solution:
    def simplifyPath(self, path: str) -> str:
        split_path = [x for x in path.split('/') if x != "" and x != "."]
        answer = []
        for character in split_path:
            if character == "..":
                if answer:
                    answer.pop()
            else:
                answer.append(character)
        return "/" + "/".join(answer)