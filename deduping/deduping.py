#!/usr/bin/python

import os
import glob
import re
import shutil
import argparse

parser = argparse.ArgumentParser (description="This script selects all subdirectories with unique prefixes, copies them to destination directory, and removes all subdirectories in source directory")

args_general = parser.add_argument_group(title="Paths")
args_general.add_argument('-s', '--src', default='/home/payal/Documents/sample_deduping', help='source path')
args_general.add_argument('-d','--dest', default='/home/payal/Documents/deduped_dirs', help='destination path')
args = parser.parse_args()

#### CONFIG BEGIN ####
src = os.path.join(os.path.normpath(args.src),'')
dest = os.path.join(os.path.normpath(args.dest),'')
##### CONFIG END #####

subdirs = []
urls = []
url_set = []
retained_files = []

def get_subdirs():
    for x in os.listdir(src):
        subdirs.append(str(x))

def get_unique_dirs():
    for grps in subdirs:
        m = re.search('_\d+.*',grps)
        timestamp = str(m.group(0))
        urls.append(grps.replace(timestamp,""))
    url_set.extend(list(set(urls)))

def move_dirs():
    print("Moving all oldest unique url directories to destination...")
    for url in url_set:
        oldest = str(min(glob.iglob(os.path.join(src,url+'*')), key = os.path.getctime)).split("/")[-1]
        if not os.path.exists(dest):
            os.makedirs(dest)
        if not os.path.exists(os.path.join(dest,oldest)):
            shutil.copytree(os.path.join(src,oldest),os.path.join(dest,oldest))

def rm_dirs():
    print("Removing all subdirectories from source path...")
    for subdir in subdirs:
        shutil.rmtree(os.path.join(src,subdir))

get_subdirs()
get_unique_dirs()
move_dirs()
rm_dirs()

print("All done")
