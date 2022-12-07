class Folder:
    def __init__(self, name):
        self.name = name
        self.sub_folds = []
        self.upper_fold = []
        self.files = []


    def get_files_size(self):
        return sum(self.files)

    def get_size(self):
        sum_size = self.get_files_size()
        for i in range(len(self.sub_folds)):
            sum_size += self.sub_folds[i].get_size()
        return sum_size
