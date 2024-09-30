from dictionary import PL

LANGUAGE:PL = PL()

class row:
    def __init__(self, course_name:str, suggested_learning_stage:str, teacher:str, place_limit:str, course_type:str, test_type:str, hours_winter:str, hours_summer:str, ects_winter:str, ects_summer:str, ects_combined:str, faculty:str, faculty_name:str, weekday:str, start_hour:str, end_hour:str, room:str, additional_pass_info:str, additional_info:str) -> None:
        self.values:dict[str, str] = {
            'Course Name': course_name.strip(),
            'Suggested Learning Stage': suggested_learning_stage.strip(),
            'Teacher': teacher.strip(),
            'Place Limit': place_limit.strip(),
            'Course Type': course_type.strip(),
            'Test Type': test_type.strip(),
            'Hours Winter': hours_winter.strip(),
            'Hours Summer': hours_summer.strip(),
            'ECTS Winter': ects_winter.strip(),
            'ECTS Summer': ects_summer.strip(),
            'ECTS Combined': ects_combined.strip(),
            'Faculty': faculty.strip(),
            'Faculty Name': faculty_name.strip(),
            'Weekday' : weekday.strip(),
            'Start Hour': start_hour.strip(),
            'End Hour': end_hour.strip(),
            'Room': room.strip(),
            'Additional Pass Info': additional_pass_info.strip(),
            'Additional Info': additional_info.strip()
        }

        self.correct_attributes()

    def __str__(self) -> str:
        return f"[{self['Course Name']}, {self['Teacher']}]"
    
    def __getitem__(self, key:str) -> str:
        return self.values[key]
    
    def correct_attributes(self) -> None:
        if len(self.values['Start Hour']) > 5:
            self.values['Start Hour'] = self.values['Start Hour'][-5:-1]

        if len(self.values['End Hour']) > 5:
            self.values['End Hour'] = self.values['End Hour'][-5:-1]

        while len(self.values['Start Hour']) < 5:
            self.values['Start Hour'] = "0" + self.values['Start Hour']

        while len(self['End Hour']) < 5:
            self.values['End Hour'] = "0" + self.values['End Hour']


def read_one_row(content:str) -> row:
    splitted_content:list[str] = content.split(';')

    if len(splitted_content) < 14:
        raise ValueError(LANGUAGE['Course loading error'])

    clustered_info:str = splitted_content[13]

    add_info:str = ""
    add_pass_info:str = ""
    start_hour:str = ""
    end_hour:str = ""
    room:str = ""
    weekday:str = ""

    result:row

    if len(splitted_content) == 15:
        add_info = splitted_content[14]
    else:
        add_info = ""

    if len(clustered_info) > 0:
        clustered_info_splitted:list[str] = clustered_info.split(',')
        
        if len(clustered_info_splitted) < 3:
            add_pass_info = clustered_info_splitted[0]
        else:            
            weekday = clustered_info_splitted[0]
            time = clustered_info_splitted[1].split('-')
            room = clustered_info_splitted[2]

            if len(time) != 2:
                start_hour = '???'
                end_hour = '???'
            else:
                start_hour = time[0].replace('.', ':')
                end_hour = time[1].replace('.', ':')
            

            if len(clustered_info_splitted) == 3:                
                add_pass_info = ""
            elif len(clustered_info_splitted) == 4:
                add_pass_info = clustered_info_splitted[2]
                room = clustered_info_splitted[3]
            else:
                add_pass_info = ""

                for item in clustered_info_splitted:
                    add_pass_info += item.strip() + ' '     
        
        result = row(
            course_name=splitted_content[0],
            suggested_learning_stage=splitted_content[1],
            teacher=splitted_content[2],
            place_limit=splitted_content[3],
            course_type=splitted_content[4],
            test_type=splitted_content[5],
            hours_winter=splitted_content[6],
            hours_summer=splitted_content[7],
            ects_winter=splitted_content[8],
            ects_summer=splitted_content[9],
            ects_combined=splitted_content[10],
            faculty=splitted_content[11],
            faculty_name=splitted_content[12],
            weekday=weekday,
            start_hour=start_hour,
            end_hour=end_hour,
            room=room,
            additional_pass_info=add_pass_info,
            additional_info=add_info
        )
    else:
        result = row(
            course_name=splitted_content[0],
            suggested_learning_stage=splitted_content[1],
            teacher=splitted_content[2],
            place_limit=splitted_content[3],
            course_type=splitted_content[4],
            test_type=splitted_content[5],
            hours_winter=splitted_content[6],
            hours_summer=splitted_content[7],
            ects_winter=splitted_content[8],
            ects_summer=splitted_content[9],
            ects_combined=splitted_content[10],
            faculty=splitted_content[11],
            faculty_name=splitted_content[12],
            weekday="",
            start_hour="",
            end_hour="",
            room="",
            additional_pass_info="",
            additional_info=add_info
        )

    return result

def read_all_rows(path:str) -> list[row]:
    errors:int = 0
    result:list[row] = []

    with open(path, 'r', encoding='utf8') as file:
        for line in file:
            try:
                to_append:row = read_one_row(line)
                result.append(to_append)
            except ValueError:
                errors += 1

    return result