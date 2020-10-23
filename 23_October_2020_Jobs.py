class Job:
    def __init__(self,job_id,company,job_role,start_salary,high_salary):
        self.job_id=job_id
        self.company=company
        self.job_role=job_role
        self.start_salary=start_salary
        self.high_salary=high_salary

class Jobsportal:
    def __init__(self,portal_name,job_list):
        self.portal_name=portal_name
        self.job_list=job_list

    def get_bestjobbyrole(self,job_r):
        ss=[]
        out=[]
        for i in self.job_list:
            if i.job_role.lower()==job_r.lower():
                ss.append(i.start_salary)
        if len(ss)!=0:
            m=max(ss)
            for i in self.job_list:
                if i.start_salary==m:
                    out.append(i)
        return out

    def jobswithsalary(self,sal):
        dic={}
        for i in self.job_list:
            if sal>=i.start_salary and sal<=i.high_salary:
                dic[i.job_id]=i.company
        return dic

if __name__=="__main__":
    c=int(input())
    job_list=[]
    for i in range(c):
        job_id=int(input())
        company=input()
        job_role=input()
        start_salary=int(input())
        high_salary=int(input())
        job_list.append(Job(job_id,company,job_role,start_salary,high_salary))
    jp=Jobsportal("abc",job_list)
    job_r=input()
    sal=int(input())
    bj=jp.get_bestjobbyrole(job_r)
    if len(bj)==0:
        print("Job Not Found for the given role")
    else:
        for i in bj:
            print(i.job_id,i.company,i.start_salary)
    js=jp.jobswithsalary(sal)
    if len(js)==0:
        print("No matching jobs for the given salary")
    else:
        for x,y in js.items():
            print(x,y)
