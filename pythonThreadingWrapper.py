import time
import threading

class customThread(threading.Thread):
   def __init__(self, threadID, functionPointer, functionParam=None):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.doThing = functionPointer
      self.param =  functionParam
      self.result = None;
   def run(self):
      if self.param:
         self.result=self.doThing(self.param)
      else:
         self.result=self.doThing()

'''#examples
def test(): ##whatever function to pass/use
   return 3


thread1=customThread(1,test)
thread1.start()

thread1.join()

print(thread1.result)
'''
