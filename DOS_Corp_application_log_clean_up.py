import datetime
import os
class FileDeleter:
    def __init__(self, path, days_threshold):
        self.path = path
        self.days_threshold = days_threshold

    def delete_old_files(self):
        today = datetime.datetime.now().date()
        threshold_date = today - datetime.timedelta(days=self.days_threshold)
        total_deleted = 0
        for root, dirs, files in os.walk(self.path):
            for file in files:
                file_path = os.path.join(root, file)
                creation_date = datetime.datetime.fromtimestamp(os.path.getctime(file_path)).date()
                print(creation_date)

                if creation_date < threshold_date:
                    os.remove(file_path)
                    total_deleted += 1
        print(f"Total files deleted: {total_deleted}")

    def run(self,path):
        print(f"Deleting files older than {self.days_threshold} days from {path}...")
        self.delete_old_files()


def main():
    paths = [r"D:\applications\inhouse\App_Data\Logs",r"D:\batch\App_Data\BatchJobsLogs"]  # Specify the directory path here
    days_threshold = 30  # Specify the threshold in days here
    for path in paths:
        deleter = FileDeleter(path, days_threshold)
        deleter.run(path)


if __name__ == '__main__':
    main()
