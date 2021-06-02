from fpdf import FPDF

image_list = []

for i in range(0,10):
    image_list.append("./place-cards/"+str(i)+".png")

pdf = FPDF()
# imagelist is the list with all image filenames
for image in image_list:
    print(image)
    pdf.add_page()
    pdf.image(image,10,10,100,100)
pdf.output("yourfile.pdf", "F")