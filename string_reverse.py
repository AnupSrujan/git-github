ex_string = "hello dude"

def reverse(ex_string):

   reverse_string = ""
   for i in range(len(ex_string)-1, -1, -1):
      reverse_string += ex_string[i]

   return reverse_string

print(reverse(ex_string))