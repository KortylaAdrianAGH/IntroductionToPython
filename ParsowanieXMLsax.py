#!/usr/bin/env python3
import xml.sax


class PlayerHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.position = ""
        self.birth = ""
        self.rating = ""
        self.foot = ""
        self.description = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "player":
            print("\n-------Player---------")
            name = attributes["name"]
            print("Name:", name)

    def endElement(self, tag):
        if self.CurrentData == "position":
            print("Position:", self.position)

        elif self.CurrentData == "birth":
            print("Birth:", self.birth)

        elif self.CurrentData == "rating":
            print("Rating:", self.rating)

        elif self.CurrentData == "foot":
            print("Foot:", self.foot)

        elif self.CurrentData == "description":
            print("Description:", self.description)

        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "position":
            self.position = content

        elif self.CurrentData == "birth":
            self.birth = content

        elif self.CurrentData == "rating":
            self.rating = content

        elif self.CurrentData == "foot":
            self.foot = content

        elif self.CurrentData == "description":
            self.description = content


if (__name__ == "__main__"):
    # XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    #ContextHandler
    Handler = PlayerHandler()
    parser.setContentHandler(Handler)

    parser.parse("Pilkarze.xml")

