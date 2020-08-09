class Zoo(object):
    def __init__(self, name):
        self.animal = {}
        self.zoo_name = name
    def add_amimal(self, obj_animal):
        if obj_animal in self.animal:
            print('此动物已存在')
            return self.animal[obj_animal]
        else:
            self.animal[obj_animal] = obj_animal
            print('添加成功')
            return True
			
class Animal(object):
    size_dict = {
        '小型':1,
        '中型':2,
        '大型':3,
    }
    like_meat_type = {
        '食肉':True,
        '食草':False,
        '杂食':False,
    }
    is_fierce_type = {
        '凶猛':True,
        '温顺':False,        
    }
 def __init__(self, like_meat, size, is_fierce):
        super().__init__()
        self.size = Animal.size_dict[size]
        self.like_meat = Animal.like_meat_type[like_meat]
        self.is_fierce = Animal.is_fierce_type[is_fierce]
        if self.size>=2 and self.like_meat==True and self.is_fierce==True:
            self.is_fierce_animal = True
        else:
            self.is_fierce_animal = False
			
class Cat(Animal):
    cry = '喵喵喵'
    def __init__(self, name, size, like_meat, is_fierce, for_pet=False):
        super().__init__(size, like_meat, is_fierce)
        self.name = name
        self.for_pet = for_pet

if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小型', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = getattr(z, 'Cat')
