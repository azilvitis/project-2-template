import sys
from linked_list import *
#import array_list

# A Song consists of:
# - title is a str
# - artist is a str
# - album is a str

class Song:
   def __init__(self,number,title,artist,album):
      self.number = number
      self.title = title
      self.artist = artist
      self.album = album

   def __repr__(self):
      return 'Song({},{},{},{})'.format(self.number,self.title,self.artist,self.album)

   def __str__(self):
      return '{}--{}--{}--{}'.format(self.number,self.title,self.artist,self.album)

   def __eq__(self,other):
      return type(other) == Song and self.number == other.number and self.title == other.title and self.artist == other.artist and self.album == other.album

def main():
   try:
      catalog = open(sys.argv[1], "r")

   except FileNotFoundError:
      print("Invalid file.")

   except IndexError:
      print("Invalid index.")

   valid_catalog = empty_list()
   songs = empty_list()
   invalid_catalog = empty_list()
   l_num = 0
   s_num = 0
   acc = 0

   for l in catalog:
      line = l.rstrip()
      if line == "":
         l_num += 1
         continue

      if line_format(line) == True:
         split_line = song_attr(line,s_num)   
         songs = add(songs,s_num,split_line)
         valid_catalog = add(valid_catalog,s_num,line)
         s_num += 1
         
      else:
         invalid_catalog = add(invalid_catalog,acc,"line " + str(l_num + 1) + ": malformed song information")
         acc += 1
      l_num += 1
      
   print("Catalog input errors:")
   foreach(invalid_catalog,print)
   display_menu()
   
   choice = int(input("Enter selection: "))
   
   while choice != 0:
      if choice == 1:
         str_list(songs)
      elif choice == 2:
         song_choice = int(input("Enter song number: "))
         if song_choice < 0 or song_choice >= length(songs):
            print("")
            print("... Invalid song number", end="\n")
         else:
            song = get(songs, song_choice)
            song_info(song,song_choice)
      elif choice == 3:
         sort_menu()
         sort_choice = int(input("Sort by: "))
         if sort_choice < 0 or sort_choice > 3:
            print("")
            print("... Invalid sort option", end="\n")
         else:
            #print(insertion_sort(Pair(2,Pair(1,Pair(3,None)))))
            #print(sort(songs,sort_choice))
            print(0)
      elif choice == 4:
         new_file = input("Enter name of file to load: ")
         try:
            n_files = open(new_file + ".txt", "r")
         except:
            print("error")
         
         invalid_catalog = empty_list()
         lnum = 0
         accu = 0

         for l in n_files:
            line = l.rstrip()
            if line == "":
               lnum += 1
               continue

            if line_format(line) == True:
               split_line = song_attr(line,s_num)   
               songs = add(songs,s_num,split_line)
               s_num += 1
                                                                                                               
            else:
               invalid_catalog = add(invalid_catalog,accu,"line " + str(lnum + 1) + ": malformed song information")
               accu += 1
            lnum += 1
            
         print("Catalog input errors:")
         foreach(invalid_catalog,print)  
      else:
         print("Invalid option")
      display_menu()
      choice = int(input("Enter selection: "))

def song_info(song,num):
   print("")
   print("Song Information ...",end="\n   ")
   print("Number: " + song.number,end="\n   ")
   print("Title: " + song.title,end="\n   ")
   print("Artist: " + song.artist,end="\n   ")
   print("Album: " + song.album,end="\n")

def sort_menu():
   print("")
   print("Sort songs", end="\n   ")
   print("0) By Number",end="\n   ")
   print("1) By Title",end="\n   ")
   print("2) By Artist",end="\n   ")
   print("3) By Album",end="\n")

def song_attr(l,song_num):
   n_line = str(song_num)+ "--" + l
   line = n_line.split('--')
   song = Song(*line)
   return song

def line_format(line):
   n_line = line.split('--') 
   if len(n_line) != 3 or '--' not in line:
      return False
   else:
      return True

def comes_before(a,b):
   if a < b:
      return True
   elif a > b:
      return False
   else:
      print(a)
     # return comes_before(a,b)

def sort(lst,choice):
   position = 0
   sorted_list = empty_list()
   s_list = empty_list()
   if choice == 0:
      for i in range(length(lst)-1):
         if lst == None:
            break
         if lst.first and lst.rest.first:
            print(lst.first.number)
            print(lst.rest.first.number)
            if comes_before(lst.first.number,lst.rest.first.number) == True:   
               sorted_list = add(sorted_list,i,lst.first)
            else:
               val = lst.first
               lst.first = lst.rest.first
               lst.rest.first = val
               sorted_list = add(sorted_list,i,lst.first)
            print(sorted_list)
            print("current")
         
            current = lst.first.number
            print(current)
            count = 0
            
            while sorted_list != None:
               if comes_before(sorted_list.first.number,current) == False:
                  val = sorted_list.first
                  sorted_list.first = current
                  current = val
                  sorted_list = add(sorted_list,count,current)
                  s_list = sorted_list
               count += 1
               sorted_list = sorted_list.rest
         
                  
         lst = lst.rest
         position += 1
         print(s_list)
      return sorted_list
      
   elif choice == 1:
      pass
   elif choice == 2:
      pass
   elif choice == 3:
      pass
   else:
      pass

def insertion_sort(unsorted):    
    head = None
    while unsorted:
        current = unsorted
        unsorted = unsorted.rest
        if not head or current.first < head.first:
            current.first = head;
            head = current;
        else:
            find = head;
            while find and current.first > find.rest.first:
                find = find.rest
            current.rest = find.rest
            find.rest = current
    return head

def display_menu():
   print("")
   print("Song Catalog",end="\n   ")
   print("1) Print Catalog",end="\n   ")
   print("2) Song Information",end="\n   ")
   print("3) Sort",end="\n   ")
   print("4) Add Songs",end="\n   ")
   print("0) Quit",end="\n")

if __name__ == "__main__":
   main()
