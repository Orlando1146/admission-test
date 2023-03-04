## 列表 ##
lista = [1, 2, 3, 4]
# 列表訪問
print(lista[0])
print(lista[-1])

# 列表修改
lista.append(5)
print(lista)

lista.insert(0, 0)
print(lista)

lista[0] = "a"
print(lista)

print(lista[0:3])

# 排序
lista.sort
print(lista)

## 集合 ##
seta = {1, 2, 3, 4}

# 集合增減
seta.add(5)
print(seta)

seta.remove(3)
print(seta)

# 去除重複
setb = set([1, 1, 2, 2, 2, 2, 3])
print(setb)

# 集合邏輯運算
setc = {1, 2, 3}
setd = {3, 4, 5}
print(setc | setd) #聯集
print(setc ^ setd)
print(setc - setd) #差集
print(setc & setd) #交集

## 字典 ##
dicta = {
    "a" : 1,
    "b" : 2,
    "c" : 3
}

print(dicta["a"])

dicta["d"] = 4
print(dicta)

dicta["a"] = 0
print(dicta)
# 列出所有key
print(dicta.keys())

print(dicta.values())

# 移除key b
dicta.pop("b")
print(dicta)

dicta.clear()
print(dicta)

## 元組 ##
tuplea = (1, 2, 3, 4)

print(tuplea[0])