from rembg import remove
import easygui
from PIL import Image

inputPath = easygui.fileopenbox(title='Select The Image')
outputPath = easygui.filesavebox(title='Select The Save Folder')

input = Image.open(inputPath)
output = remove(input)
output.save(outputPath)
