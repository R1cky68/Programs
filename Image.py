from PIL import Image, ImageFilter

image_path = "/Users/hargundadyala/Desktop/Image 1.png"
image = Image.open(image_path)

resized_image = image.resize((500, 500))
rotated_image = image.rotate(180)
filter_image = image.filter(ImageFilter.CONTOUR)

resized_output_path = "/Users/hargundadyala/Desktop/Image1*.png"
rotated_output_path = "/Users/hargundadyala/Desktop/Image2*.png"
filter_output_path = "/Users/hargundadyala/Desktop/Image3*.png"

resized_image.save(resized_output_path)
rotated_image.save(rotated_output_path)
filter_image.save(filter_output_path)
