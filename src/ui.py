from __future__ import annotations

from sys import argv, exit

from csv_reader import read_all_rows, row
from filter import filter_rows_value_equal, filter_rows_value_greater_equal_than, filter_rows_value_lower_equal_than
from dictionary import LanguagePack
from utils import *

from PyQt5.QtGui import QIcon, QCloseEvent
from PyQt5.QtWidgets import QPushButton, QLabel, QGroupBox, QLineEdit, QApplication, QWidget,\
                            QHBoxLayout, QVBoxLayout, QComboBox, QDesktopWidget, QScrollArea
from PyQt5.QtCore import Qt

ICON_PATH = get_resource_path('images\\icon.png')

class details(QWidget):
    def __init__(self, dictionary:LanguagePack, row_to_display:row, parent:main) -> None:
        super().__init__()
    
        self.setWindowTitle(row_to_display['Course Name'])
        self.setGeometry(0, 0, 200, 350)        
        self.setWindowIcon(QIcon(ICON_PATH))

        qr = self.frameGeometry()
        qr.moveCenter(QDesktopWidget().availableGeometry().center())
        self.move(qr.topRight())

        self.row:row = row_to_display
        self.dictionary:LanguagePack = dictionary
        self.main:main = parent
        self.setLayout(QVBoxLayout())

        for w in ['Course Name', 'Suggested Learning Stage', 'Teacher', 'Place Limit', 
        'Course Type', 'Test Type', 'Hours Winter', 'Hours Summer', 
        'ECTS Winter', 'ECTS Summer', 'ECTS Combined', 'Faculty', 
        'Faculty Name', 'Weekday', 'Start Hour', 'End Hour', 
        'Room', 'Additional Pass Info', 'Additional Info']:
            key_label:QLabel = QLabel(dictionary[w])
            key_label.setFixedWidth(200)

            value_label:QLabel = QLabel(row_to_display[w])
            value_label.setFixedWidth(400)

            small_box:QGroupBox = QGroupBox()
            small_box.setLayout(QHBoxLayout())
            small_box.setFixedWidth(600)
            small_box.layout().addWidget(key_label)
            small_box.layout().addWidget(value_label)
            self.layout().addWidget(small_box)

        self.show()

    def closeEvent(self, event:QCloseEvent) -> None:
        event.accept()
        self.main.add_windows.remove(self)
        self.close()


class main(QWidget):
    def __init__(self, dictionary:LanguagePack, database:list[row]) -> None:
        super().__init__()

        self.setWindowTitle("Fakultety")
        self.setGeometry(0, 0, 600, 400)
        self.setWindowIcon(QIcon(ICON_PATH))

        qr = self.frameGeometry()
        qr.moveCenter(QDesktopWidget().availableGeometry().center())
        self.move(qr.topLeft())

        self.database:list[row] = database
        self.dictionary:LanguagePack = dictionary
        self.add_windows:list[QWidget] = []

        #Filter labels
        self.filter_label:QLabel = QLabel(self.dictionary['Filters'])
        self.course_name_label:QLabel = QLabel(self.dictionary['Course Name'])
        self.suggested_learning_stage_label:QLabel = QLabel(self.dictionary['Suggested Learning Stage'])
        self.teacher_name_label:QLabel = QLabel(self.dictionary['Teacher'])
        self.place_limit_label:QLabel = QLabel(self.dictionary['Place Limit'])
        self.course_type_label:QLabel = QLabel(self.dictionary['Course Type'])
        self.test_type_label:QLabel = QLabel(self.dictionary['Test Type'])
        self.hours_winter_label:QLabel = QLabel(self.dictionary['Hours Winter'])
        self.hours_summer_label:QLabel = QLabel(self.dictionary['Hours Summer'])
        self.ects_winter_label:QLabel = QLabel(self.dictionary['ECTS Winter'])
        self.ects_summer_label:QLabel = QLabel(self.dictionary['ECTS Summer'])
        self.ects_combined_label:QLabel = QLabel(self.dictionary['ECTS Combined'])
        self.faculty_label:QLabel = QLabel(self.dictionary['Faculty'])
        self.faculty_name_label:QLabel = QLabel(self.dictionary['Faculty Name'])
        self.weekday_label:QLabel = QLabel(self.dictionary['Weekday'])
        self.start_hour_label:QLabel = QLabel(self.dictionary['Start Hour'])
        self.end_hour_label:QLabel = QLabel(self.dictionary['End Hour'])
        self.room_label:QLabel = QLabel(self.dictionary['Room'])

        # Input fields (QLineEdit)
        self.course_name_input:QLineEdit = QLineEdit()
        self.teacher_name_input:QLineEdit = QLineEdit()
        self.place_limit_input:QLineEdit = QLineEdit()
        self.hours_winter_input:QLineEdit = QLineEdit()
        self.hours_summer_input:QLineEdit = QLineEdit()
        self.ects_winter_input:QLineEdit = QLineEdit()
        self.ects_summer_input:QLineEdit = QLineEdit()
        self.ects_combined_input:QLineEdit = QLineEdit()
        self.start_hour_input:QLineEdit = QLineEdit()
        self.end_hour_input:QLineEdit = QLineEdit()
        self.room_input:QLineEdit = QLineEdit()

        # Dropdowns (QComboBox)
        self.suggested_learning_stage_dropdown:QComboBox = QComboBox()
        self.course_type_dropdown:QComboBox = QComboBox()
        self.test_type_dropdown:QComboBox = QComboBox()
        self.faculty_dropdown:QComboBox = QComboBox()
        self.weekday_dropdown:QComboBox = QComboBox()

        # Buttons (QPushButton)
        self.filter_button:QPushButton = QPushButton(self.dictionary['Filter'])
        self.clear_filters_button:QPushButton = QPushButton(self.dictionary['Clear Filters'])
        self.filter_button.clicked.connect(lambda: self.filter())
        self.clear_filters_button.clicked.connect(lambda: self.clear_filters())

        self.add_items_to_dropdowns()

        # Group boxes (QGroupBox)
        self.right_filters_box:QGroupBox = QGroupBox()
        self.right_filters_box.setLayout(QVBoxLayout())

        self.small_box_1:QGroupBox = QGroupBox()
        self.small_box_1.setLayout(QHBoxLayout())
        self.small_box_1.layout().addWidget(self.course_name_label)
        self.small_box_1.layout().addWidget(self.course_name_input)

        # Suggested Learning Stage
        self.small_box_2:QGroupBox = QGroupBox()
        self.small_box_2.setLayout(QHBoxLayout())
        self.small_box_2.layout().addWidget(self.suggested_learning_stage_label)
        self.small_box_2.layout().addWidget(self.suggested_learning_stage_dropdown)

        # Teacher Name
        self.small_box_3:QGroupBox = QGroupBox()
        self.small_box_3.setLayout(QHBoxLayout())
        self.small_box_3.layout().addWidget(self.teacher_name_label)
        self.small_box_3.layout().addWidget(self.teacher_name_input)

        # Place Limit
        self.small_box_4:QGroupBox = QGroupBox()
        self.small_box_4.setLayout(QHBoxLayout())
        self.small_box_4.layout().addWidget(self.place_limit_label)
        self.small_box_4.layout().addWidget(self.place_limit_input)

        # Course Type
        self.small_box_5:QGroupBox = QGroupBox()
        self.small_box_5.setLayout(QHBoxLayout())
        self.small_box_5.layout().addWidget(self.course_type_label)
        self.small_box_5.layout().addWidget(self.course_type_dropdown)

        # Test Type
        self.small_box_6:QGroupBox = QGroupBox()
        self.small_box_6.setLayout(QHBoxLayout())
        self.small_box_6.layout().addWidget(self.test_type_label)
        self.small_box_6.layout().addWidget(self.test_type_dropdown)

        # Hours Winter
        self.small_box_7:QGroupBox = QGroupBox()
        self.small_box_7.setLayout(QHBoxLayout())
        self.small_box_7.layout().addWidget(self.hours_winter_label)
        self.small_box_7.layout().addWidget(self.hours_winter_input)

        # Hours Summer
        self.small_box_8:QGroupBox = QGroupBox()
        self.small_box_8.setLayout(QHBoxLayout())
        self.small_box_8.layout().addWidget(self.hours_summer_label)
        self.small_box_8.layout().addWidget(self.hours_summer_input)

        # ECTS Winter
        self.small_box_9:QGroupBox = QGroupBox()
        self.small_box_9.setLayout(QHBoxLayout())
        self.small_box_9.layout().addWidget(self.ects_winter_label)
        self.small_box_9.layout().addWidget(self.ects_winter_input)

        # ECTS Summer
        self.small_box_10:QGroupBox = QGroupBox()
        self.small_box_10.setLayout(QHBoxLayout())
        self.small_box_10.layout().addWidget(self.ects_summer_label)
        self.small_box_10.layout().addWidget(self.ects_summer_input)

        # ECTS Combined
        self.small_box_11:QGroupBox = QGroupBox()
        self.small_box_11.setLayout(QHBoxLayout())
        self.small_box_11.layout().addWidget(self.ects_combined_label)
        self.small_box_11.layout().addWidget(self.ects_combined_input)

        # Faculty
        self.small_box_12:QGroupBox = QGroupBox()
        self.small_box_12.setLayout(QHBoxLayout())
        self.small_box_12.layout().addWidget(self.faculty_label)
        self.small_box_12.layout().addWidget(self.faculty_dropdown)

        # Weekday
        self.small_box_13:QGroupBox = QGroupBox()
        self.small_box_13.setLayout(QHBoxLayout())
        self.small_box_13.layout().addWidget(self.weekday_label)
        self.small_box_13.layout().addWidget(self.weekday_dropdown)

        # Start Hour
        self.small_box_14:QGroupBox = QGroupBox()
        self.small_box_14.setLayout(QHBoxLayout())
        self.small_box_14.layout().addWidget(self.start_hour_label)
        self.small_box_14.layout().addWidget(self.start_hour_input)

        # End Hour
        self.small_box_15:QGroupBox = QGroupBox()
        self.small_box_15.setLayout(QHBoxLayout())
        self.small_box_15.layout().addWidget(self.end_hour_label)
        self.small_box_15.layout().addWidget(self.end_hour_input)

        # Room
        self.small_box_16:QGroupBox = QGroupBox()
        self.small_box_16.setLayout(QHBoxLayout())
        self.small_box_16.layout().addWidget(self.room_label)
        self.small_box_16.layout().addWidget(self.room_input)
        
        self.right_buttons_box:QGroupBox = QGroupBox()
        self.right_buttons_box.setLayout(QHBoxLayout())
        
        for w in [self.filter_button, self.clear_filters_button]:
            self.right_buttons_box.layout().addWidget(w)        
        
        self.right_box:QGroupBox = QGroupBox()
        self.right_box.setLayout(QVBoxLayout())
        self.right_box.setMaximumWidth(400)

        for w in [
        self.small_box_1, self.small_box_2, self.small_box_3, self.small_box_4,
        self.small_box_5, self.small_box_6, self.small_box_7, self.small_box_8,
        self.small_box_9, self.small_box_10, self.small_box_11, self.small_box_12,
        self.small_box_13, self.small_box_14, self.small_box_15, self.small_box_16]:
            self.right_box.layout().addWidget(w)

        self.right_box.layout().addWidget(self.right_buttons_box)

        self.left_box:QGroupBox = QGroupBox()
        left_box_layout = QVBoxLayout()
        left_box_layout.setAlignment(Qt.AlignTop)
        self.left_box.setLayout(left_box_layout)
        self.left_box.layout().addWidget(self.create_header_row())

        for item in self.database:
            self.left_box.layout().addWidget(self.create_course_row(item))

        self.left_scroll:QScrollArea = QScrollArea()
        self.left_scroll.setWidgetResizable(True)
        self.left_scroll.setWidget(self.left_box)
        self.left_scroll.setFixedWidth(1330)

        self.main_box:QGroupBox = QGroupBox()
        self.main_box.setLayout(QHBoxLayout())
        
        for w in [self.left_scroll, self.right_box]:
            self.main_box.layout().addWidget(w)

        self.down_box:QGroupBox = QGroupBox()
        self.down_box.setLayout(QHBoxLayout())

        self.setLayout(QVBoxLayout())

        for w in [self.main_box, self.down_box]:
            self.layout().addWidget(w)
            self.layout().addWidget(w)

    def add_items_to_dropdowns(self) -> None:
        self.suggested_learning_stage_dropdown.addItem('')
        self.course_type_dropdown.addItem('')
        self.test_type_dropdown.addItem('')
        self.faculty_dropdown.addItem('')
        self.weekday_dropdown.addItem('')

        self.suggested_learning_stage_dropdown.addItems(get_all_values_from_column(
            rows=self.database,
            column_name='Suggested Learning Stage'
        ))

        self.course_type_dropdown.addItems(get_all_values_from_column(
            rows=self.database,
            column_name='Course Type'
        ))

        self.test_type_dropdown.addItems(get_all_values_from_column(
            rows=self.database,
            column_name='Test Type'
        ))

        self.faculty_dropdown.addItems(get_all_values_from_column(
            rows=self.database,
            column_name='Faculty'
        ))

        self.weekday_dropdown.addItems(get_all_values_from_column(
            rows=self.database,
            column_name='Weekday'
        ))

    def create_header_row(self) -> QGroupBox:
        main_box:QGroupBox = QGroupBox()
        main_box.setLayout(QHBoxLayout())
        main_box.setFixedWidth(1300)
        main_box.setFixedHeight(48)
        
        course_name_label:QLabel = QLabel(self.dictionary['Course Name'])
        course_name_label.setFixedWidth(300)

        teacher_label:QLabel = QLabel(self.dictionary['Teacher'])
        teacher_label.setFixedWidth(300)

        weekday_label:QLabel = QLabel(self.dictionary['Weekday'])
        weekday_label.setFixedWidth(100)

        start_hour_label:QLabel = QLabel(self.dictionary['Start Hour'])
        start_hour_label.setFixedWidth(100)

        end_hour_label:QLabel = QLabel(self.dictionary['End Hour'])
        end_hour_label.setFixedWidth(100)
        
        room_label:QLabel = QLabel(self.dictionary['Room'])
        room_label.setFixedWidth(100)
        
        ects_combined_label:QLabel = QLabel(self.dictionary['ECTS Combined'])
        ects_combined_label.setFixedWidth(220)

        for w in [course_name_label, teacher_label, weekday_label, start_hour_label, end_hour_label, ects_combined_label]:
            main_box.layout().addWidget(w)

        return main_box

    def create_course_row(self, row_to_display:row) -> QGroupBox:
        main_box:QGroupBox = QGroupBox()
        main_box.setLayout(QHBoxLayout())
        main_box.setFixedWidth(1300)
        main_box.setFixedHeight(48)

        if row_to_display is None:
            return main_box
        
        course_name_label:QLabel = QLabel(row_to_display['Course Name'])
        course_name_label.setFixedWidth(300)

        teacher_label:QLabel = QLabel(row_to_display['Teacher'])
        teacher_label.setFixedWidth(300)

        weekday_label:QLabel = QLabel(row_to_display['Weekday'])
        weekday_label.setFixedWidth(100)

        start_hour_label:QLabel = QLabel(row_to_display['Start Hour'])
        start_hour_label.setFixedWidth(100)

        end_hour_label:QLabel = QLabel(row_to_display['End Hour'])
        end_hour_label.setFixedWidth(100)
        
        room_label:QLabel = QLabel(row_to_display['Room'])
        room_label.setFixedWidth(100)
        
        ects_combined_label:QLabel = QLabel(row_to_display['ECTS Combined'])
        ects_combined_label.setFixedWidth(100)

        details_button:QPushButton = QPushButton(self.dictionary['Details'])
        details_button.clicked.connect(lambda: self.show_details(row_to_display))
        details_button.setFixedWidth(100)

        for w in [course_name_label, teacher_label, weekday_label, start_hour_label, end_hour_label, ects_combined_label, details_button]:
            main_box.layout().addWidget(w)

        return main_box

    def closeEvent(self, event:QCloseEvent) -> None:
        event.accept()
        
        for window in QApplication.topLevelWidgets():
            window.close()

    def show_details(self, row_to_display:row) -> None:
        new_window:details = details(self.dictionary, row_to_display, self)
        self.add_windows.append(new_window)

    def filter(self) -> None:
        layout = self.left_box.layout()
        matching_rows:list[row] = self.database.copy()
        
        if layout is not None:
            while layout.count():
                child = layout.itemAt(0).widget()
                layout.removeWidget(child)
                child.deleteLater()

        eq_values_dict: dict[str, str] = {
            'Course Name': self.course_name_input.text().strip(),
            'Suggested Learning Stage': self.suggested_learning_stage_dropdown.currentText(),
            'Teacher': self.teacher_name_input.text().strip(),
            'Place Limit': self.place_limit_input.text().strip(),
            'Course Type': self.course_type_dropdown.currentText(),
            'Test Type': self.test_type_dropdown.currentText(),
            'Hours Winter': self.hours_winter_input.text().strip(),
            'Hours Summer': self.hours_summer_input.text().strip(),
            'ECTS Winter': self.ects_winter_input.text().strip(),
            'ECTS Summer': self.ects_summer_input.text().strip(),
            'ECTS Combined': self.ects_combined_input.text().strip(),
            'Faculty': self.faculty_dropdown.currentText(),
            'Weekday': self.weekday_dropdown.currentText(),
            'Room': self.room_input.text().strip()
        }

        for k in eq_values_dict.keys():
            if eq_values_dict[k] != "":
                matching_rows = filter_rows_value_equal(matching_rows, k, eq_values_dict[k])

        if self.start_hour_input.text().strip() != "":
            matching_rows = filter_rows_value_greater_equal_than(matching_rows, 'Start Hour', self.start_hour_input.text().strip())
            
        if self.end_hour_input.text().strip() != "":
            matching_rows = filter_rows_value_lower_equal_than(matching_rows, 'End Hour', self.end_hour_input.text().strip())

        self.left_box.layout().addWidget(self.create_header_row())

        for item in matching_rows:
            self.left_box.layout().addWidget(self.create_course_row(item))

    def clear_filters(self) -> None:
        line_edits = [
            self.course_name_input,
            self.teacher_name_input,
            self.place_limit_input,
            self.hours_winter_input,
            self.hours_summer_input,
            self.ects_winter_input,
            self.ects_summer_input,
            self.ects_combined_input,
            self.start_hour_input,
            self.end_hour_input,
            self.room_input
        ]

        for line_edit in line_edits:
            line_edit.setText("")

        combo_boxes = [
            self.suggested_learning_stage_dropdown,
            self.course_type_dropdown,
            self.test_type_dropdown,
            self.faculty_dropdown,
            self.weekday_dropdown
        ]

        for combo_box in combo_boxes:
            combo_box.setCurrentText("")

        self.filter()


class app:
    def __init__(self, dictionary:LanguagePack, path:str) -> None:
        self.all_rows = read_all_rows(path)

        self.app:QApplication = QApplication(argv)
        self.dictionary:LanguagePack = dictionary
        self.main:main = main(self.dictionary, self.all_rows)

        self.main.show()
        exit(self.app.exec())

