from urllib.request import urlopen
import re
def getName(classDepartment, classID):
        url = "https://app.coursedog.com/api/v1/cm/umn_umntc_peoplesoft/courses/search/" + classDepartment + classID
        page = urlopen(url)
        html = page.read().decode("utf-8")
        pattern = "\"longName\":.*?\"milestones\""
        match_results = re.search(pattern, html, re.IGNORECASE).group()
        match_results = re.sub("\"longName\":\"", classDepartment + classID + " - ", match_results)
        match_results = re.sub("\",\"milestones\"", ": ", match_results)
        return match_results

def getDescription(classDepartment, classID):
        url = "https://app.coursedog.com/api/v1/cm/umn_umntc_peoplesoft/courses/search/" + classDepartment + classID
        page = urlopen(url)
        html = page.read().decode("utf-8")
        pattern = "\"description\".*?\"designation\""
        match_results = re.search(pattern, html, re.IGNORECASE).group()
        match_results = re.sub(" \",\"designation\"", "", match_results)
        match_results = re.sub("\"description\":\"", "", match_results)
        return match_results

def getAssessment(classDepartment, classID):
        url = "https://app.coursedog.com/api/v1/cm/umn_umntc_peoplesoft/courses/search/" + classDepartment + classID
        page = urlopen(url)
        html = page.read().decode("utf-8")
        pattern = "\"learningOutcomes\":.*?\"objective\":"
        match_results = re.search(pattern, html, re.IGNORECASE).group()
        match_results = re.sub("\"learningOutcomes\":.*?name\":\"", "Learning Outcomes: ", match_results)
        match_results = re.sub("\",\"activity\":\"", "", match_results)
        match_results = re.sub("\",\"assessment\":\"", " ", match_results)
        match_results = re.sub("\",\"objective\":", "", match_results)
        return match_results

def getContent(classDepartment, classID):
    return (getName(classDepartment, classID) + getDescription(classDepartment, classID) + getAssessment(classDepartment, classID))
