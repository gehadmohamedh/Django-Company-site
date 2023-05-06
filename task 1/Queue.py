import json 
class Queue:
    all_queue = {}
    def __init__(self , name , size  ):
        self.arr = []
        self.name = name 
        self.size = size 
        Queue.all_queue[self.name]=self.arr
        
    def enqueue(self , item):
        if len(self.arr) == self.size:
            raise Exception("QueueOutOfRangeException")
        else :
           self.arr.append(item)
        
    def isEmpty(self):
        return bool(len(self.arr))
                
    def dequeue(self):
        if self.isEmpty():
            print ("The Queue is empty There is nothing to dequeue !!!")
            return None
        return self.arr.pop(0)
    
    @staticmethod
    def load ():
        file = open("queue_data.txt","r")
        return file.readlines()
    
    @staticmethod
    def save ():
        try:
            file = open("queue_data.txt","a")
            all_queue_str= json.dumps( Queue.all_queue)
            file.write(all_queue_str)
            print ("saved successfully ")
            return True
        except:
            print ("falied")
            return False
        
            
    
qq = Queue("qq", 3)
qq.enqueue(5225962)
qq.enqueue(7552488)
qq.enqueue(9454885)

Queue.save()
print(Queue.load())

print (qq.isEmpty())