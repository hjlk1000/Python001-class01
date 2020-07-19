>>> import pandas
>>> import numpy
>>> 
>>> 
>>> data = pandas.DataFrame({
    'id':numpy.arange(1,16),
    'age':numpy.random.randint(20,90,15)
})
>>> data

    id  age
0    1   58
1    2   29
2    3   70
3    4   35
4    5   37
5    6   67
6    7   88
7    8   25
8    9   50
9   10   46
10  11   55
11  12   27
12  13   49
13  14   20
14  15   20

>>> table1 = pandas.DataFrame({
    'id':numpy.arange(1,11),
    'age':numpy.random.randint(20,90,10)
})

>>> table1
   id  age
0   1   78
1   2   25
2   3   26
3   4   30
4   5   24
5   6   87
6   7   50
7   8   84
8   9   46
9  10   46
>>> table2 = pandas.DataFrame({
    'id':numpy.arange(1,11),
    'age':numpy.random.randint(20,90,10)
})
>>> table2
   id  age
0   1   54
1   2   63
2   3   75
3   4   59
4   5   51
5   6   79
6   7   80
7   8   53
8   9   23
9  10   57
>>> 

1. SELECT * FROM data;

>>> print(data)
    id  age
0    1   58
1    2   29
2    3   70
3    4   35
4    5   37
5    6   67
6    7   88
7    8   25
8    9   50
9   10   46
10  11   55
11  12   27
12  13   49
13  14   20
14  15   20
>>> 

2. SELECT * FROM data LIMIT(10);

>>> print(data.iloc[:10])
   id  age
0   1   58
1   2   29
2   3   70
3   4   35
4   5   37
5   6   67
6   7   88
7   8   25
8   9   50
9  10   46
>>> 

3. SELECT id FROM data; //id 是 data 表的特定一列

>>> print(data['id'])
0      1
1      2
2      3
3      4
4      5
5      6
6      7
7      8
8      9
9     10
10    11
11    12
12    13
13    14
14    15
Name: id, dtype: int32

4. SELECT COUNT(id) FROM data;
>>> print(data.id.shape[0])
15
>>> 


5. SELECT * FROM data WHERE id<1000 AND age>30;
print(data[(data['id']<1000) & (data['age']>30)])
>>> print(data[(data['id']<1000) & (data['age']>30)])
    id  age
0    1   58
2    3   70
3    4   35
4    5   37
5    6   67
6    7   88
8    9   50
9   10   46
10  11   55
12  13   49
>>> 

6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;

>>> table1['order_id'] = numpy.random.randint(20,25,10)
>>> table1
   id  age  order_id
0   1   78        20
1   2   25        23
2   3   26        21
3   4   30        20
4   5   24        20
5   6   87        21
6   7   50        23
7   8   84        20
8   9   46        22
9  10   46        20

>>> for i in table1.drop_duplicates("order_id").groupby('id'):
    print(i)

    
(1,    id  age  order_id
0   1   78        20)
(2,    id  age  order_id
1   2   25        23)
(3,    id  age  order_id
2   3   26        21)
(9,    id  age  order_id
8   9   46        22)

7. SELECT * FROM table1 t1 INNER_JOIN table2 t2 ON t1.id = t2.id;
>>> table1.id = numpy.arange(5,15)
>>> table1
   id  age  order_id
0   5   78        20
1   6   25        23
2   7   26        21
3   8   30        20
4   9   24        20
5  10   87        21
6  11   50        23
7  12   84        20
8  13   46        22
9  14   46        20

>>> table2
   id  age
0   1   54
1   2   63
2   3   75
3   4   59
4   5   51
5   6   79
6   7   80
7   8   53
8   9   23
9  10   57

list(table2.id)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

>>> mask = []
>>> for a in list(table1.id):
    if a in list(table2.id):
        mask.append(True)
    else:
        mask.append(False)

        
>>> table1[mask]
   id  age  order_id
0   5   78        20
1   6   25        23
2   7   26        21
3   8   30        20
4   9   24        20
5  10   87        21

8. SELECT FROM table1 UNION SELECT FROM table2;

print(pandas.concat([table1,table2]).reset_index(drop=True))
    id  age  order_id
0    5   78      20.0
1    6   25      23.0
2    7   26      21.0
3    8   30      20.0
4    9   24      20.0
5   10   87      21.0
6   11   50      23.0
7   12   84      20.0
8   13   46      22.0
9   14   46      20.0
10   1   54       NaN
11   2   63       NaN
12   3   75       NaN
13   4   59       NaN
14   5   51       NaN
15   6   79       NaN
16   7   80       NaN
17   8   53       NaN
18   9   23       NaN
19  10   57       NaN
>>> 

9. DELETE FROM table1 WHERE id=10;
>>> table1.drop(table1[table1['id'] == 10].index[0])
   id  age  order_id
0   5   78        20
1   6   25        23
2   7   26        21
3   8   30        20
4   9   24        20
6  11   50        23
7  12   84        20
8  13   46        22
9  14   46        20

10. ALTER TABLE table1 DROP COLUMN column_name;
table1.drop(columns=['age'] , axis=1)
   id  order_id
0   5        20
1   6        23
2   7        21
3   8        20
4   9        20
5  10        21
6  11        23
7  12        20
8  13        22
9  14        20