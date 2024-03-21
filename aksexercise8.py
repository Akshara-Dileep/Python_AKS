'''In a company, worker efficiency is determined on the basis of the time required for a worker to complete a particular job.
 If the time taken by the worker is between 2 – 3 hours, then the worker is said to be highly efficient.
If the time required by the worker is between 3 – 4 hours, then the worker is ordered to improve speed.
If the time taken is between 4 – 5 hours, the worker is given training to improve his speed,
and if the time taken by the worker is more than 5 hours, then the worker has to leave the company.
If the time taken by the worker is input through the keyboard, find the efficiency of the worker.

'''
hours=float(input("Enter the time taken by the worker:"))
if hours>=2 and hours<=3:
    print("The worker is efficient")
elif hours>3 and hours<=4:
    print("The worker has to be improved")
elif hours>4 and hours<=5:
    print("Training to be provided")
else:
    print("Worker has to leave")    

    '''output
    Enter the time taken by the worker:5
    Training to be provided'''