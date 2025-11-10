def func(pos1, pos2, /, mix1, mix2, *, key1, key2):
    print(pos1, pos2, mix1, mix2, key1, key2)
    
if __name__ == "__main__":
    print("Hello", "world", sep="#|", end=" |")
    func(5,10,"hi","22",key1="abc",key2=False)
    func(5,10,mix1="hi",mix2="22",key1="abc",key2=False)
    func(5,10,"hi",mix2="22",key1="abc",key2=False)
    func(5,pos2=10,mix1="hi",mix2="22",key1="abc",key2=False)
    

    
    
print("Hello", "world", sep="#|", end=" |")
