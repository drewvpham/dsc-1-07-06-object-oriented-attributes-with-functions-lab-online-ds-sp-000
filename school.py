class School():
    
    def __init__(self, name, roster=[]):
        self.name=name
        self._roster = {}
        
    def roster(self):
        return self._roster
    
    def add_student(self,name, grade):
        if grade not in self._roster.keys():
            self._roster[grade]=[name]
        else:
            self._roster[grade].append(name)
        return self._roster
    
    def grade(self, grade):
        return self._roster[grade]
    
    def sort_roster(self):
        copy= self._roster
        for key in copy:
            copy[key].sort()
        return copy