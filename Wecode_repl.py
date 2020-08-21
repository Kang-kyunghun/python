# argument
def sum_of_numbers(*args):
  if len(args) == 0:
    return 0
  return sum(args)

# print(sum_of_numbers(1,2,3,4,5))

# keyword argument
def what_is_my_full_name(**kwargs):
    key = list(kwargs.keys())
    name = []
    for i in key:
        if i in ["last_name", "first_name"]:
            name.append(i)
    if len(name) == 0:
        return "Nobody"
    elif len(name) == 1:
        return kwargs[name[0]]
    else:
        key = list(kwargs.keys())
        name = []
        for i in key:
            if i in ["last_name", "first_name"]:
                name.append(i)
        
        if name[0] == "last_name":
            return kwargs[name[0]] + " " + kwargs[name[1]]
        else:
            return kwargs[name[1]] + " " + kwargs[name[0]]
print(what_is_my_full_name(a=1, first_name = "우성"))

# 변수 scope
what_is_my_scope = 7

def scope_test(what_is_my_scope):
  some_number = 9
  
  def inner_scope_test(what_is_my_scope):
    return some_number * what_is_my_scope
    
  return inner_scope_test(7)
print(scope_test(10))

# class 만들기
class Database:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.dict = {}
    def insert(self, field, value):
        if len(self.dict) <= self.size:
            self.dict[field] = value
    def select(self, feild):
        if feild in self.dict.keys():
            return self.dict[feild]
        else:
            return 'None'  #수정해야 할 수도 있음
    def update(self, feild, value):
        if feild in self.dict.keys():
            self.dict[feild] = value
    def delete(self,feild):
        if feild in self.dict.keys():
            del self.dict[feild]