# pydoclite
#### pydoclite is the python api for doclite. More info on doclite can be found here [https://github.com/haibeey/doclite](https://github.com/haibeey/doclite)

### Installation 
##### pip install pydoclite

#### Example 
``` 
from pydoclite import doclite

d = doclite.Doclite.Connect(b"doclitetest.db")
baseCollection = d.Base()

for i in range(10): 
    baseCollection.Insert({"a":1})

print(baseCollection.FindOne(1))
baseCollection.DeleteOne(2)

print(baseCollection.Find({"a":1}))
baseCollection.Delete({"a":1})

print(baseCollection.Find({"a":1}))

d.Close()
 ```