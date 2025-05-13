from pentalpha import bautista, banzali, raymundo, managbanag, espinola

print("Prints the name of the constellation a star belongs to")
print("Ex: Regulus, Capella, Arcturus")
star_input = input("Enter Star Name (Leave blank for random): ")
bautista.get_constellation(star_input)
print("")

print("Prints the hashed text of the inputted string")
banzali.hash_text()
print("")

print("Convert an image to grayscale")
raymundo.convert_grayscale()
print("")

print("Generate a fake person profile")
managbanag.make_fake_person()
print("")

print("Prints random programming jokes depending on user input")
espinola.jokes()
print("")
