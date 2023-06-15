import shutil
import os
import sched
import time
#stable V1
class disk_cleaner:
    def __init__(self,path,threshold) -> None:
        self.path = path 
        self.threshold = threshold
    
    def check_disk_space(self):
        total, used, free = shutil.disk_usage(self.path)
        return free
    
    def delete_files(self):
        files = os.listdir(self.path)
        total_deleted = 0
 
        for file  in files:
            file_path =  os.path.join(self.path,file)
            if os.path.isfile(file_path):
                os.remove(file_path)
                total_deleted += 1
        print("Total Files Deleted: ", total_deleted)
 
    def run(self):
        free_space = self.check_disk_space() //(2**30)
        print(f'Free Disk Space: {free_space} GB')
 
        if free_space < self.threshold:
            print("Deleting files...")
            self.delete_files()
        else:
            print("No files to delete. Disk Space is sufficient")
 
def perform_disk_cleanup(path, threshold):
    checker = disk_cleaner(path,threshold)
    checker.run()
 
def schedule_disk_cleanup(path,threshold,hour =0, minute=0, second =0):
    scheduler = sched.scheduler(time.time, time.sleep)
    def perform_cleanup():
        perform_disk_cleanup( path,threshold)
        scheduler.enter(86400,1,perform_cleanup)
        print('------------------------------------------------------------------------------------------------------------------')
        print(f'checking again at {hour}:00 if Free Disk Space is Below {threshold} GB(s) in {path} all files will be deleted.....')
        print('------------------------------------------------------------------------------------------------------------------')
    first_cleanup_time = time.mktime(time.strptime(time.strftime('%y-%m-%d'),'%y-%m-%d'))+ hour * 3600 + minute * 60 + second
    scheduler.enterabs(first_cleanup_time, 1, perform_cleanup)
    scheduler.run()

def main():
    path = input("Please enter the folder path to check:")
 
    threshold = int(input("Please enter the GB threshold:"))
    hour = int(input("Please enter what hour(24 hour format) to run the check: "))
    print(f'At {hour}:00 if Free Disk Space is Below {threshold} GB(s) in {path} all files will be deleted.....')
    print('----------------------------------------------------------------------------------------------------')
    schedule_disk_cleanup(path,threshold, hour=hour)
   
 
if __name__ == '__main__':
    main()
