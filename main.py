bad_code = """
import   math,sys

def  calculate_area( radius ):
  if(radius<=0):
   print("invalid radius")
   return None
  else:
     area=math.pi*radius*radius
     print( "Area is :",area )
     return area

def process_list( items ):
    total=0
    for i in items:
     if(i%2==0):
      total=total+i
     else:
        total = total+ i
    print("Total:",total);return total

class  student:
 def __init__( self,name,age ):
  self.name=name
  self.age=age
 def display(self ):
   print( "Name:",self.name,"Age:",self.age )
"""
