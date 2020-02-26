class InvalidMove(Exception):
    pass

class InvalidTab(Exception):
    pass

class InvalidRange(Exception):
    pass

class IncorrectInt(Exception):
    pass

# def ParsetInt(self,answer):
#     try:
#         result = int(answer)
#     except:
#         raise IncorrectInt("Type a correct number...")
    
#     if result < 1 or result >8:
#         raise InvalidRange("please write a number in the range from 1 to 8")
    
#     return result
