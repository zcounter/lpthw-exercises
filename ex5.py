name = 'Michael Quintero'
age = 37 # Not a lie
height = 74 # inches
weight = 240 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Black'
fav_music = 'Jazz'
instrument_age = 19
cm = 10.0 
inch = 12



print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He likes %s." % fav_music
print "His trombone is %d years old." % instrument_age
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)

# The following formula will convert in to cm.  in x 2.54 = cm
# We assign the length variable as raw input function (the portion within the brackets, "Length in cm\n" will run the read
# with the comment "Length in cm" then throw a newline...which will then be floated using the float function

length = float (raw_input("Length in cm\n"))
length_in_inches = length * 0.393700787

# The %.2f indicates a floating output, with up to 2 decimal spaces, in this case for the length_in_inches array

print "You entered", length, "cm, that comes to %.2f inches" % length_in_inches


# The following forumula will convert cm to in. cm x 0.39 = in
weight = float (raw_input("Weight in kilos\n"))
weight_in_pounds = weight * 2.2

print "You entered ", weight, "kg, that comes to %.2f pounds" % weight_in_pounds

