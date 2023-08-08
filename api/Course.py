import math

class Course:
    def __init__(self, course_acronym, strength, date, time, day, room_no, room_capacity):
        self.course_acronym = course_acronym
        # self.course_code = course_code
        # self.section = section
        self.strength = strength
        self.date = date
        self.time = time
        self.day = day
        self.room_no = room_no.split(",")[:-1]
        self.building = room_no.split(",")[-1]
        self.req_invigilators = self.__set_req_invigilators(strength, self.room_no, room_capacity)
        self.course_ta = [] 
        self.invigilators = []

    def __set_req_invigilators(self, strength, room_no, room_capacity):
        if len(room_no) == 1:
            result = strength / 25
            if strength >= 150 or strength % 25 >= 10:
                return math.ceil(result)
            else:
                return math.floor(result)
        num_invigilators = 0
        print(self.course_acronym)
        for room in room_no:
            print(room)
            num_students = min(strength, room_capacity[room.lower().strip()])
            print(f"Num Students {num_students}")
            result = num_students/25
            if num_students >= 150 or num_students % 25 >= 10:
                num_invigilators += math.ceil(result)
                print(math.ceil(result))
            else:
                num_invigilators += math.floor(result)
                print(math.floor(result))
            strength -= num_students
        return num_invigilators
        
        
    def get_req_invigilator(self):
        return self.req_invigilators
        
    def add_invigilators(self, invigilator):
        self.invigilators.append(invigilator)

    def add_course_ta(self, course_ta):
        self.course_ta.append(course_ta)

    def get_course_acronym(self):
        return self.course_acronym

    def get_course_code(self):
        return self.course_code

    def get_section(self):
        return self.section
    
    def get_course_ta(self):
        return self.course_ta

    def get_strength(self):
        return self.strength

    def get_date(self):
        return self.date

    def get_time(self):
        return self.time
    
    def get_day(self):
        return self.day
    
    def get_room_no(self):
        return self.room_no
    
    def get_invigilators(self):
        return self.invigilators
    
    def get_building(self):
        return self.building

    