import string
import random
import os
from lxml import etree


class LogoTemplate:

    def __init__(self, source, m_primitive, m_symbol, m_text, m_palette):
        self.primitive = m_primitive
        self.symbol = m_symbol
        self.palette = m_palette
        self.text = m_text
        self.svgXml = ""
        self.font = 0
        self.name = 0
        self.__setTemplateSVG(source)

    def __setColorByType(self, colorType):
        if colorType == "main":
            return self.palette.main
        elif colorType == "secondary":
            return self.palette.secondary
        elif colorType == "outline":
            return self.palette.outline
        elif colorType == "textmain":
            return self.palette.textMain
        elif colorType == "textsecondary":
            return self.palette.textSecondary
        else:
            return "#FFFFFF"

    def __setTemplateSVG(self, source):
        file = open(source)
        for line in file:
            if line[0:2] == "<g":
                temp = etree.fromstring(line)
                temp.set("fill", self.__setColorByType(temp.get("type")))
                self.svgXml += etree.tostring(temp).decode(encoding="UTF-8")
            if line[0:10] == "<primitive":
                temp = etree.fromstring(line)
                self.primitive.xCordinate = temp.get("x")
                self.primitive.yCordinate = temp.get("y")
                self.primitive.width = temp.get("width")
                self.primitive.height = temp.get("height")
                self.primitive.color = self.__setColorByType(temp.get("type"))
                self.primitive.setShapeAttributes()
                self.svgXml += etree.tostring(self.primitive.svgXml).decode(encoding="UTF-8")
            elif line[0:7] == "<symbol":
                temp = etree.fromstring(line)
                self.symbol.xCordinate = temp.get("x")
                self.symbol.yCordinate = temp.get("y")
                self.symbol.width = temp.get("width")
                self.symbol.height = temp.get("height")
                self.symbol.color = self.__setColorByType(temp.get("type"))
                self.symbol.setShapeAttributes()
                self.svgXml += etree.tostring(self.symbol.svgXml).decode(encoding="UTF-8")
            elif line[0:5] == "<text":
                temp = etree.fromstring(line)
                self.text.secondaryText = temp.get("secondary-color-text")
                self.text.anchorPosition = temp.get("text-anchor-position")
                self.text.xCordinate = temp.get("x")
                self.text.yCordinate = temp.get("y")
                self.text.width = temp.get("width")
                self.text.height = temp.get("height")
                self.text.anchor = temp.get("text-anchor")
                self.text.fontSize = temp.get("font-size")
                self.text.textSpacing = temp.get("letter-spacing")
                self.text.color = self.__setColorByType(temp.get("type"))
                self.text.secondaryColor = self.__setColorByType("textsecondary")
                self.text.setShapeAttributes()
                self.svgXml += etree.tostring(self.text.svgXml).decode(encoding="UTF-8")
            else:
                self.svgXml += str(line)

    def writeFile(self, location):
        file = open(location, "w")
        file.write(self.svgXml)
        file.close()


class ShapeText:

    def __init__(self, source):
        self.xCordinate = 0
        self.anchorPosition = 400
        self.yCordinate = 0
        self.width = 1000
        self.height = 0
        self.text = ""
        self.svgXml = 0
        self.secondaryText = 0
        self.textSpacing = 0
        self.fontSize = 100
        self.color = "#FFFFFF"
        self.secondaryColor = "#FFFFFF"
        self.mask = 0
        self.anchor = "middle"
        self.__getShapeFromFile(source)

    def __getShapeFromFile(self, source):
        xml = 0

        with open(source, "r") as file:
            xml = file.read().replace('\n', '')

        self.svgXml = etree.XML(xml)
        file.close()

    def setShapeAttributes(self):
        for element in self.svgXml.iter('svg'):
            element.set("x", str(self.xCordinate))
            element.set("y", str(self.yCordinate))
            element.set("width", str(self.width))
            element.set("height", str(self.height))

        for element in self.svgXml.iter('text'):
            element.set("font-size", str(self.fontSize))
            element.set("text-anchor", str(self.anchor))
            element.set("fill", self.color)

            if self.textSpacing is not 0 and self.textSpacing is not None:
                element.set("letter-spacing", str(self.textSpacing))

            element.set("x", self.anchorPosition)

            if self.secondaryText != 0 and self.secondaryText is not None:
                words = self.text
                words = words.split()
                if len(words) > 1:
                    self.text = words[0]
                    stuff = etree.SubElement(element, "tspan")
                    stuff.set("fill", str(self.secondaryColor))
                    stuff.text = " " + words[1]
            element.text = self.text


class ShapePrimitive:

    def __init__(self, source):
        self.xCordinate = 0
        self.yCordinate = 0
        self.width = 1000
        self.height = 0
        self.svgXml = 0
        self.color = "#FFFFFF"
        self.mask = 0
        self.__getShapeFromFile(source)

    def __getShapeFromFile(self, source):
        xml = 0

        with open(source, "r") as file:
            xml = file.read().replace('\n', '')

        self.svgXml = etree.XML(xml)
        file.close()

    def setShapeAttributes(self):
        for element in self.svgXml.iter('svg'):
            element.set("x", str(self.xCordinate))
            element.set("y", str(self.yCordinate))
            element.set("width", str(self.width))
            element.set("height", str(self.height))
            element.set("fill", self.color)


class ShapeSymbol:

    def __init__(self, source):
        self.xCordinate = 0
        self.yCordinate = 0
        self.width = 1000
        self.height = 0
        self.svgXml = 0
        self.color = "#FFFFFF"
        self.mask = 0
        self.__getShapeFromFile(source)

    def __getShapeFromFile(self, source):
        xml = 0

        with open(source, "r") as file:
            xml = file.read().replace('\n', '')

        self.svgXml = etree.XML(xml)
        file.close()

    def setShapeAttributes(self):
        for element in self.svgXml.iter('svg'):
            element.set("x", str(self.xCordinate))
            element.set("y", str(self.yCordinate))
            element.set("width", str(self.width))
            element.set("height", str(self.height))
            element.set("fill", self.color)


class ColorPalette:

    def __init__(self, source=None):
        self.main = "#FFFFFF"
        self.secondary = "#FFFFFF"
        self.outline = "#FFFFFF"
        self.textMain = "#FFFFFF"
        self.textSecondary = "#FFFFFF"
        if source is not None:
            self.getPaletteFromFile(source)

    def getPaletteFromFile(self, source):
        file = open(source, "r")
        lines = []

        for line in file:
            lines.append(etree.fromstring(line))

        file.close()

        for tag in lines:
            if tag.get("type") == "main":
                self.main = tag.text
            elif tag.get("type") == "secondary":
                self.secondary = tag.text
            elif tag.get("type") == "outline":
                self.outline = tag.text
            elif tag.get("type") == "textmain":
                self.textMain = tag.text
            elif tag.get("type") == "textsecondary":
                self.textSecondary = tag.text


class FileFinder:

    def __init__(self, m_folder, m_filetype):
        self.folder = m_folder
        self.filetype = m_filetype
        self.files = []
        self.__findAllFilesFromFolder(self.folder)

    def __findAllFilesFromFolder(self, folder):
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.endswith(self.filetype):
                    self.files.append(os.path.join(root, file))

    def getRandomFile(self):
        return random.sample(self.files, 1)[0]


dirColors = FileFinder("./palettes", "xml")
dirShapes = FileFinder("./primitives", "svg")
dirSymbols = FileFinder("./symbols", "svg")
dirTemplates = FileFinder("./templates", "xml")
dirFonts = FileFinder("./fonts", "xml")

colorPalette1 = ColorPalette(dirColors.getRandomFile())
shape01 = ShapePrimitive(dirShapes.getRandomFile())
symbol01 = ShapeSymbol(dirSymbols.getRandomFile())
font01 = ShapeText(dirFonts.getRandomFile())

font01.text = "BrandMe"

logo = LogoTemplate(dirTemplates.getRandomFile(), shape01, symbol01, font01, colorPalette1)
logo.writeFile("logo.svg")
