import glob, os
import xmltodict
import json
import pprint

#Printing results
pp = pprint.PrettyPrinter(indent=4)

def process():
    # Finds all XML files on data/ and append to list
    pascal_voc_contents = []
    os.chdir("data")

    print("Found {} files in data directory!".format(str(len(glob.glob("*.xml")))))
    for file in glob.glob("*.xml"):
        f_handle = open(file, 'r')
        print("Parsing file '{}'...".format(file))
        pascal_voc_contents.append(xmltodict.parse(f_handle.read()))

    # Process each file individually
    for index in pascal_voc_contents:
        image_file = index['annotation']['filename']
        # If there's a corresponding file in the folder,
        # process the images and save to output folder
        if os.path.isfile(image_file):
            print("Image file found, extracting boxed images to '{}/'...".format("output/"+image_file.split('.')[0]))
            # TODO image processing here
        else:
            print("Image file '{}' not found, skipping file...".format(image_file))


if __name__ == '__main__':
    print("------------------------------------")
    print("----- PascalVOC-to-Images v0.1 -----")
    print("Created by Giovanni Cimolin da Silva")
    print("------------------------------------")
    process()