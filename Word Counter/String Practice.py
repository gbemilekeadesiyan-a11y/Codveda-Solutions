fruit ="Banana"
if "nana" in fruit:
    print("Yes") 


fruit_2= "BANANA"
fruit_2 = fruit_2.lower() 
print(fruit_2)    

fruit_3 = fruit_2.upper() 
print(fruit_3)   

str = "favour"
pos = str.find("o")
print(pos)

greet = "Hello Genny"
new_greet = greet.replace("Genny", "Evergreen")
print(new_greet)

name = "            Main Character"
name = name.strip()
print(name)                       

line = "Please have a nice day"
answer = line.startswith("Please")
print(answer)  


email_header = "From openscout+on-the-side@substack.com  26 May 2026 at 15:07 (Delivered after 224 seconds) " 
atpos = email_header.find("@")
print(atpos)  
sppos= email_header.find(" ",atpos)
print(sppos)
host= email_header[atpos+1:sppos]
print(host)