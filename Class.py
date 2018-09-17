class StudentRecord:
    students = list()
    sort_id = list()
    def append(self, student_id, name):
        self.students.append({"student_id" : student_id, "name" : name})
    def search(self, student_id):
        for i in self.students:
            self.n_id = i.get("student_id")
            self.n_name = i.get("name")
            if self.n_id == student_id:
                print(self.n_name)
    def name_list(self):
        for i in self.students:
            self.sort_id.append(i.get("student_id"))
        self.sort_id.sort()
        print(self.sort_id)
        
