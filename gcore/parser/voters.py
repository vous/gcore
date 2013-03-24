# -*- coding: utf-8 *-*

import xml.etree.ElementTree as et
import glob


def get_points(data):
    points_data = {}
    for item in data:
        if item.tag == "twelve":
            points_data["twelve"] = item.text
        if item.tag == "ten":
            points_data["ten"] = item.text
        if item.tag == "eight":
            points_data["eight"] = item.text
        if item.tag == "seven":
            points_data["seven"] = item.text
        if item.tag == "six":
            points_data["six"] = item.text
        if item.tag == "five":
            points_data["five"] = item.text
        if item.tag == "four":
            points_data["four"] = item.text
        if item.tag == "three":
            points_data["three"] = item.text
        if item.tag == "two":
            points_data["two"] = item.text
        if item.tag == "one":
            points_data["one"] = item.text
    return points_data


def get_voter_data(filename):
    """Given a location, return the voter data"""
    tree = et.parse(filename)
    root = tree.getroot()
    data = {}
    for item in root:
        # a voter should have all of these values
        if item.tag == "name":
            data["name"] = item.text
        elif item.tag == "image":
            data["image"] = item.text
        elif item.tag == "points":
            points_data = get_points(item)
            data["points"] = points_data
    print data
    return data


def get_voters_directory(main_directory=None, voters_directory=None):
    if main_directory is None:
        main_directory = "data"
    else:
        pass

    if voters_directory is None:
        voters_directory = "/voters"
    base_directory = main_directory + voters_directory

    return base_directory


def get_all_voters_data(voters_directory):
    voter_files = glob.glob(voters_directory + "/*.xml")
    print voter_files
    all_voter_data = []
    number = 0
    for voter in voter_files:
        voter_data = get_voter_data(voter)
        voter_data["id"] = number
        all_voter_data.append(voter_data)
        number = number + 1
    print "Read %d voters" % (number)
    return all_voter_data


def read_voters(main_directory=None, voters_directory=None):
    voter_location = get_voters_directory(main_directory, voters_directory)
    voters_data = get_all_voters_data(voter_location)
    return voters_data


def main():
    #filename = "data/voters/voter1.xml"
    read_voters()

if __name__ == '__main__':
    main()
