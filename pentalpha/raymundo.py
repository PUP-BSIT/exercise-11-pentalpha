from PIL import Image

def convert_grayscale():
    """ Convert an image to grayscale and save it """
    input_path = "modernhouse.jpg"
    output_path = "gray_image.jpg"
    
    image = Image.open(input_path)
    gray_image = image.convert("L")
    gray_image.save(output_path)
    print(f"Grayscale image saved as '{output_path}'.")
