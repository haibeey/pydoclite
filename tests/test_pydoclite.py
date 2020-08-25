from pydoclite import Doclite
import glob
import os

def test_basic():

    def removeFiles():
        for f in glob.glob("doclitetest.db*"):
            try:
                os.remove(f)
            except OSError:
                pass

    removeFiles()

    d = Doclite.Connect(b"doclitetest.db")
    baseCollection = d.Base()

    for i in range(10): 
        baseCollection.Insert({"a":1})

    assert {"a":1} == baseCollection.FindOne(1)
    baseCollection.DeleteOne(2)

    assert len(baseCollection.Find({"a":1})) == 9
    baseCollection.Delete({"a":1})

    assert len(baseCollection.Find({"a":1})) == 0

    d.Close()
    
    removeFiles()
