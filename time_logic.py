seconds = int(input("enter a large integer: "))
hours = seconds // 3600
remainsec = seconds % 3600
minutes = remainsec //60
second = remainsec %60
print(seconds, "second is",hours, "hours", minutes,"minutes",second,"seconds")