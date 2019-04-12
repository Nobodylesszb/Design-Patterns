import threading
import time

#这里使用__new__实现单例模式

class Singleton:
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super(Singleton,cls).__new__(cls,*args,**kwargs)
        return cls._instance

#总线

class Bus(Singleton):
    lock = threading.RLock()
    def sendData(self,data):
        self.lock.acquire()
        time.sleep(3)
        print('sending signal data',data)
        self.lock.release()

class VisitEntity(threading.Thread):
    my_bus = ''
    name = ''
    def getName(self):
        return self.name
    def setName(self,name):
        self.name = name
    def run(self):
        self.bus = Bus()
        self.bus.sendData(self.name)

if  __name__=="__main__":
    for i in range(3):
        print ("Entity %d begin to run..."%i)
        my_entity=VisitEntity()
        my_entity.setName("Entity_"+str(i))
        my_entity.start()

"""
output:
Entity 0 begin to run...
Entity 1 begin to run...
Entity 2 begin to run...
sending signal data Entity_0
sending signal data Entity_1
sending signal data Entity_2
"""
        
