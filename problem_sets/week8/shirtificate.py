from fpdf import FPDF
import os
import sys

class ShirtPDF(FPDF):

    def __init__(self, orientation='P', unit='mm', format='A4'):
        super().__init__(orientation=orientation, unit=unit, format=format)
        self.set_auto_page_break(auto=False)
        self.set_margins(0, 0, 0)

    def add_shirt_design(self, image_file, user_name):

        self.add_page()

        self.set_font('helvetica', style='B', size=24)
        self.set_text_color(0, 0, 0)

        title_text = "CS50 Shirtificate"
        title_width = self.get_string_width(title_text)

        title_x = (self.w - title_width) / 2 + 3
        title_y = 20
        self.text(x=title_x, y=title_y, text=title_text)

        image_y = title_y + 15

        img_width = 180
        img_x = (self.w - img_width) / 2

        self.image(image_file, x=img_x, y=image_y, w=img_width)

        self.set_font('helvetica', style='B', size=24)
        self.set_text_color(255, 255, 255)  # White text

        full_text = f"{user_name} took CS50"

        text_width = self.get_string_width(full_text)
        text_x = (self.w - text_width) / 2

        text_y = image_y + 85

        while text_width > (self.epw - 40) and self.font_size > 10:
            self.set_font_size(self.font_size - 1)
            text_width = self.get_string_width(full_text)
            text_x = (self.w - text_width) / 2

        self.text(x=text_x, y=text_y, text=full_text)

def main():
    user_name = str(input("Name: ")).strip()

    txt_output = user_name

    shirt_image = "shirtificate.png"

    if not os.path.exists(shirt_image):
        sys.exit("Error: not found in current directory")

    pdf = ShirtPDF()

    pdf.add_shirt_design(shirt_image, txt_output)

    filename = "shirtificate.pdf"
    pdf.output(filename)
    print(f"PDF generated: {filename}")

if __name__ == "__main__":
    main()






