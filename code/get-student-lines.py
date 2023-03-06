# Makes use of git blame to create a binary file that contains every line a student has modified in each of
# their repositories.
#
# Author: Niklas Wicklund

from glob import glob
import io
import re
import subprocess
import os
import pickle
from tqdm import tqdm
from optparse import OptionParser


#Returns list of tuples with information about all student repos in specific directory.
def get_all_student_files(directory):
    repos = []
    students = [ (f.path,f.name) for f in os.scandir(directory) if f.is_dir() ]
    for t in tqdm(students):
        student = t[1]
        _dirs = [ (f.path,f.name) for f in os.scandir(t[0]) if f.is_dir() ] # (student,path,dirname,task)
        for d in _dirs:
            task = re.search(f"{student}-(.*)",d[1])
            if task is not None:
                res = []
                start_dir = d[0]
                pattern = "*.java"
                for dir,_,_ in os.walk(start_dir):
                    res.extend(glob(os.path.join(dir,pattern)))
                
                repos.append((student,res,start_dir,task.group(1)))
    

    return repos

#Return email of users that aren't "known", meaning deemed to be the students.
def get_ok_users_in_repo(repo_path,student,task,known):
        command = "git log --all --format='%ae' | sort -u"
        users = []
        users2 = []
        process = subprocess.Popen(
            command,
            cwd=repo_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
        )
        #
        while True:
            line = process.stdout.readline().decode("utf-8").rstrip()
            if not line:
                break
            users2.append(line)
            if line not in known:
                users.append(line)
        return users


#Runs a specific command
def run(command,top_path):
    process = subprocess.Popen(
        command,
        cwd=top_path,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
    )
    lines = []
    for line in io.TextIOWrapper(process.stdout,encoding="utf-8"):
        line_mod = re.sub("[\(\)]","",line)
        objects = line_mod.split()
        try:
            objects.pop(0)
            for o in objects:
                if o.isdigit():
                    lines.append(o)
                    break
        except:
            print(command)
    return lines


def analyze(directory,output_file,year,one_task,known_tas_path):
    repos = get_all_student_files(directory)
    stats = {}


    known = []
    with open(known_tas_path,"r") as infile:
        while True:
            ta = infile.readline()
            if not ta:
                break
            known.append(ta.rstrip())
    for repo in tqdm(repos):
        student = repo[0]
        files = repo[1]
        top_path = repo[2]
        task = repo[3]
        if one_task is not None and task != one_task:
            continue
        
        if task == "quicksort":
            task = "task-19"
        task_number = task.split('-')[1]
        if task_number not in stats:
            stats[task_number] = {}
        
        if student not in stats[task_number]:
            stats[task_number][student] = {}

        ok_emails = get_ok_users_in_repo(top_path,student,task_number,known)
        stats[task_number][student]["loc"] = {}
        if len(ok_emails) == 0:
            stats[task_number][student]["loc"] = {}
            continue
        for file in files:
            in_file = re.sub(f"{top_path}/","",file)
            key =in_file
            in_file = re.sub(" ","\ ",in_file)
            pattern = '\|'.join(ok_emails) 
            added_part = "| grep -P \".*20[\d]{2}-[\d]{2}-[\d]{2} [\d]{2}:[\d]{2}:[\d]{2} [-+]\d{4}\s+\d+\)\s*[^\s//*]+\""
            command = f"git blame -w -M -e -C -C -C {in_file} {added_part}| grep -i \"{pattern}\""
            lines_extra = run(command,top_path)
            
            command = f"git blame -w -M -e -C -C -C {in_file} | grep -i \"{pattern}\""
            lines_basic = run(command,top_path)
            match = re.search('.*Test.java',in_file) #Exclude violations found in test-files
            if match is None:
                stats[task_number][student]["loc"][key] = len(lines_extra)

            stats[task_number][student][key] = lines_basic
            
    #Saves student lines to a binary file.
    with open(f"{output_file}-{year}.bin","wb") as outfile:
        pickle.dump(stats,outfile)

parser = OptionParser()
parser.add_option("-d", "--directory", dest="sourcedir",default='.',
                  help="directory of violations", metavar="DIR")
parser.add_option("-y", "--year", dest="year",
                  help="year to look at")
parser.add_option("-o", "--output", dest="outputfile",
                  help="file to save result in", metavar="FILE",default='')
parser.add_option("-t", "--known", dest="known_ta_path",
                  help="path to file with know TAs for the year", metavar="FILE")
parser.add_option("-a", "--task", dest="task",
                  help="specific task")  
(options, args) = parser.parse_args()

if options.year is None:
    print("Need year -y <year>")
    quit()
analyze(options.sourcedir,options.outputfile,options.year,options.task,options.known_ta_path)