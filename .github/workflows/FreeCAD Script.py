import FreeCAD as App
import FreeCADGui as Gui

def convert_step_to_png(step_file, png_file):
    App.newDocument()
    App.open(step_file)
    Gui.activeDocument().activeView().saveImage(png_file, 1920, 1080, "Transparent")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python convert_step_to_png.py <step_file> <png_file>")
        sys.exit(1)
    
    step_file = sys.argv[1]
    png_file = sys.argv[2]
    convert_step_to_png(step_file, png_file)
