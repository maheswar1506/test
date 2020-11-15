import numpy as np 
import pandas as pd 
import os,csv

def individual():
    headera = ["Subject", "Credits", "Type", "Grade", "Sem"]
    header1 = ["sub_code", "total_credits", "sub_type", "credit_obtained", "sem", "roll"]
    cols = ["sub_code", "total_credits", "sub_type", "credit_obtained", "sem"]
    df = pd.read_csv("acad_res_stud_grades.csv", usecols=header1)
    if os.path.exists("./grades"):
        pass
    else:
        os.makedirs("./grades")

    basepath = "./grades"
    basename = "_individual.csv"
    
    for index,row in df.iterrows():
        roll_num = row["roll"]
        row.drop("roll")
        filename = roll_num+basename
        if(os.path.exists(os.path.join(basepath,filename))):
            with open(os.path.join(basepath,filename),"a+") as file:
                row = pd.DataFrame(row).transpose()
                row.to_csv(file, header=False, index=False, columns=cols)
        else:
            with open(os.path.join(basepath,filename),"a+") as file:
                start = "Roll: {}".format(roll_num)
                info = "Semester Wise Details"
                start = pd.Series(start)
                info = pd.Series(info)
                start.to_csv(file, header=False, quoting=csv.QUOTE_NONNUMERIC, index=False)
                info.to_csv(file, header=False, quoting=csv.QUOTE_NONNUMERIC, index=False)
                row = pd.DataFrame(row).transpose()
                row.to_csv(file, index=False, columns=cols, header=headera)


def spi(credits, grades):
    gra = {"AA":10, "AB":9, "BB":8, "BC":7, "CC":6, "CD":5, "DD":4, "F":0, "I":0}
    grade_sum = 0
    weighted_sum = 0
    for x in grades:
        grade_sum += gra[x]
    for x,y in zip(credits, grades):
        weighted_sum += (x*gra[y])
    return (weighted_sum/grade_sum)

def cpi(credits,spi_li):
    weighted_sum = 0
    for x,y in zip(credits,spi_li):
        weighted_sum += (x*y)
    return(weighted_sum/credits.sum())

def overall():
    files = [file for file in os.listdir("./grades")]
    basepath = "./grades"
    for file in files:
        with open(os.path.join(basepath,file), "a+") as f:
            tempfile = os.path.join(basepath,file)
            temp = pd.read_csv(tempfile, skiprows = 2)
            pass
            """
            li = temp["Sem"].unique()
            sem_li = list()
            sem_credits_li = list()
            sem_credits_cleared_li = list()
            sem_spi_li = list()
            total_credits_li = list()
            sem_cpi_li = list()
            for semester in li:
                sem_res = temp[temp["Sem"] == semester]
                sem_li.append(semester)
                sem_credits_li.append(sem_res["Credits"].sum())
                sem_credits_cleared_li.append(sem_credits_li)
                sem_spi_li.append(spi(list(sem_res["Credits"]), list(sem_res["Grade"])))
                total_credits_li.append(sum(sem_credits_li))
                if (len(sem_cpi_li) == 0):
                    sem_cpi_li.append(sem_spi_li[0])
                else:
                    sem_cpi_li.append(cpi(sem_res["Credits"], sem_spi_li))

            dictionary = {"Semester": sem_li, "Semester Credits": sem_credits_li, "Semester Credits Cleared": sem_credits_li, "SPI": sem_spi_li, "Total Credits": total_credits_li, "Total Credits Cleared": total_credits_li, "CPI": sem_cpi_li}
            results = pd.DataFrame.from_dict(dictionary)
            print(dictionary)"""

overall()
#individual()
