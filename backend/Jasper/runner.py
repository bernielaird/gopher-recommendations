import csv
import Scraper
import csvWriter
from GPT import gpt3_completion

def getResponse(prompt):
    setup = 'You are going to help me create an array of attributes for this class. I will give you the name of the class and a brief description of the course content. You will then rate the course using your best judgement in several categories which I will give you. You are not rating based on difficulty, but simply how much each attribute applies to the class. You will give me a score from 0 to 10 for each of the following categories: Math, English, History, Critical Thinking, Writing, Research, Science, Language, Communication, Technology, Social Studies, Workload, Test based, homework based, project based, collaboration, Effort, Boring, Technical, and barrier to entry. '
    response = gpt3_completion(setup + prompt)
    return(response)

def runIt(n):
    classList = csvWriter.classList()
    content = ""
    with open('test.csv', mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for i in range(n):
            content = Scraper.getContent(classList[i][0],classList[i][1])
            a = getResponse(content)
            csv_writer.writerow([int(i) for i in a.split() if i.isdigit()])

runIt(2)


    
