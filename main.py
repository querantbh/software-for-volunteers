import os
import sys
import json
import requests
import configparser
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QDesktopWidget, QComboBox, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QScrollArea, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtCore import Qt, QSize, QEvent

class CustomWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.current_step = 0  

        comic_sans_font = QFont("Comic Sans MS", 10)  

        self.setWindowTitle("Учёт активности волонтёров")
        self.setGeometry(0, 0, 400, 355)
        self.setMinimumSize(400, 300)
        self.show

        self.setStyleSheet("""
            background-color: #2E2E2E;
            color: white; /* Устанавливаем белый цвет текста */
        """)

        self.setWindowFlag(Qt.FramelessWindowHint)

        self.welcomeLabel = QLabel("Добро пожаловать!", self)
        self.welcomeLabel.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        self.welcomeLabel.setAlignment(Qt.AlignCenter)

        self.descriptionLabel = QLabel(
            "Эта программа разработана для 'Молодежного Центра' и предназначена для работы с волонтёрами, а точнее контроль над их активностью.<br>",
            self
        )        
        self.descriptionLabel.setStyleSheet("color: white;")
        self.descriptionLabel.setAlignment(Qt.AlignCenter)
        self.descriptionLabel.setWordWrap(True)

        layout = QVBoxLayout(self)

        buttonLayout = QHBoxLayout()
        spacer = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        buttonLayout.addItem(spacer)

        self.themeButton = QPushButton(self)
        self.themeButton.setIconSize(QSize(15, 15))

        theme_image_url = 'https://i.ibb.co/94Jn6MW/theme-white.png'
        filename_theme = os.path.join(appdata_path, 'theme_white.png')

        if not os.path.exists(filename_theme):
            response = requests.get(theme_image_url)
            with open(filename_theme, 'wb') as file:
                file.write(response.content)

        self.themeButton.setIcon(QIcon(filename_theme))
        self.themePixmap = QPixmap(filename_theme)
        self.themeButton.setStyleSheet("background-color: transparent; border: none;")
        self.themeButton.clicked.connect(self.toggle_theme)

        self.themeButton.installEventFilter(self)

        theme_hover_image_url = 'https://i.ibb.co/8dcxW2R/theme-white-hover.png'
        filename_theme_hover = os.path.join(appdata_path, 'theme-white-hover.png')

        if not os.path.exists(filename_theme_hover):

            response = requests.get(theme_hover_image_url)
            with open(filename_theme_hover, 'wb') as file:
                file.write(response.content)

        self.themeHoverPixmap = QPixmap(filename_theme_hover)
        self.themeHoverPixmap = self.themeHoverPixmap.scaled(QSize(17, 17), Qt.KeepAspectRatio, Qt.SmoothTransformation)

        buttonLayout.addWidget(self.themeButton, alignment=Qt.AlignLeft | Qt.AlignTop)

        self.minimizeButton = QPushButton(self)
        self.minimizeButton.setIconSize(QSize(17, 17))

        minimize_image_url = 'https://i.ibb.co/zGPGr0h/collapse.png'
        filename_minimize = os.path.join(appdata_path, 'collapse.png')

        if not os.path.exists(filename_minimize):

            response = requests.get(minimize_image_url)
            with open(filename_minimize, 'wb') as file:
                file.write(response.content)

        self.minimizeButton.setIcon(QIcon(filename_minimize))
        self.minimizePixmap = QPixmap(filename_minimize)
        self.minimizeButton.setStyleSheet("background-color: transparent; border: none;")
        self.minimizeButton.clicked.connect(self.showMinimized)

        self.minimizeButton.installEventFilter(self)

        minimize_hover_image_url = 'https://i.ibb.co/Zz2f1xD/collapse-hover.png'
        filename_minimize_hover = os.path.join(appdata_path, 'collapse_hover.png')

        if not os.path.exists(filename_minimize_hover):

            response = requests.get(minimize_hover_image_url)
            with open(filename_minimize_hover, 'wb') as file:
                file.write(response.content)

        self.minimizeHoverPixmap = QPixmap(filename_minimize_hover)
        self.minimizeHoverPixmap = self.minimizeHoverPixmap.scaled(QSize(17, 17), Qt.KeepAspectRatio, Qt.SmoothTransformation)

        buttonLayout.addWidget(self.minimizeButton, alignment=Qt.AlignRight | Qt.AlignTop)

        self.closeButton = QPushButton(self)
        self.closeButton.setIconSize(QSize(15, 15))

        close_image_url = 'https://i.ibb.co/5v560wy/close.png'
        filename_close = os.path.join(appdata_path, 'close.png')

        if not os.path.exists(filename_close):

            response = requests.get(close_image_url)
            with open(filename_close, 'wb') as file:
                file.write(response.content)

        self.closeButton.setIcon(QIcon(filename_close))
        self.closePixmap = QPixmap(filename_close)
        self.closeButton.setStyleSheet("background-color: transparent; border: none;")
        self.closeButton.clicked.connect(self.close)

        self.closeButton.installEventFilter(self)

        close_hover_image_url = 'https://i.ibb.co/nnVTyxj/close-hover.png' 
        filename_close_hover = os.path.join(appdata_path, 'close_hover.png')

        if not os.path.exists(filename_close_hover):

            response = requests.get(close_hover_image_url)
            with open(filename_close_hover, 'wb') as file:
                file.write(response.content)

        self.closeHoverPixmap = QPixmap(filename_close_hover)
        self.closeHoverPixmap = self.closeHoverPixmap.scaled(QSize(15, 15), Qt.KeepAspectRatio, Qt.SmoothTransformation)

        buttonLayout.addWidget(self.closeButton, alignment=Qt.AlignRight | Qt.AlignTop)

        layout.addLayout(buttonLayout)

        add_button_style = """
            QPushButton {
                background-color: #483D8B; /* Зеленый цвет фона */
                color: white; /* Белый цвет текста */
                border: none; /* Убираем границу */
                padding: 5px 10px; /* Отступы внутри кнопки */
                font-size: 14px; /* Размер шрифта */
                border-radius: 5px; /* Закругление углов */
            }

            QPushButton:hover {
                background-color: #4D4491; /* Цвет фона при наведении */
            }
        """

        combo_box_style = """
            background-color: #FFFFFF;
            border: 1px solid #7F7F7F;
            border-radius: 5px;
            padding: 5px;
            color: #000000;
        """

        line_edit_style = """
            background-color: #FFFFFF;
            border: 1px solid #7F7F7F;
            border-radius: 5px;
            padding: 5px;
            color: #000000;
            selection-background-color: #ACCEF7;
        """

        self.personComboBox = QComboBox(self)
        self.personComboBox.addItem("Не выбрано")
        self.personComboBox.addItem("Добавить волонтёра...")
        self.personComboBox.setCurrentIndex(0)
        self.personComboBox.activated.connect(self.on_person_changed)
        self.personComboBox.setStyleSheet(combo_box_style)

        self.volunteerNameLineEdit = QLineEdit(self)
        self.volunteerNameLineEdit.setPlaceholderText("ФИО волонтера")
        self.volunteerNameLineEdit.setStyleSheet(line_edit_style)

        self.addVolunteerButton = QPushButton("Добавить волонтёра", self)
        self.addVolunteerButton.clicked.connect(self.addVolunteer)
        self.addVolunteerButton.setStyleSheet(add_button_style)

        self.taskComboBox = QComboBox(self)
        self.taskComboBox.addItem("Не выбрано")
        self.taskComboBox.addItem("Добавить задание...")
        self.taskComboBox.setCurrentIndex(0)
        self.taskComboBox.activated.connect(self.on_task_changed)
        self.taskComboBox.setStyleSheet(combo_box_style)

        self.taskNameLineEdit = QLineEdit(self)
        self.taskNameLineEdit.setPlaceholderText("Название задания")
        self.taskNameLineEdit.setStyleSheet(line_edit_style)

        self.taskDescriptionLineEdit = QLineEdit(self)
        self.taskDescriptionLineEdit.setPlaceholderText("Описание задания")
        self.taskDescriptionLineEdit.setStyleSheet(line_edit_style)

        self.taskScoreLineEdit = QLineEdit(self)
        self.taskScoreLineEdit.setPlaceholderText("Баллы задания")
        self.taskScoreLineEdit.setStyleSheet(line_edit_style)

        self.addTaskButton = QPushButton("Добавить задание", self)
        self.addTaskButton.clicked.connect(self.addTask)
        self.addTaskButton.setStyleSheet(add_button_style)

        self.scoreComboBox = QComboBox(self)
        self.scoreComboBox.setCurrentIndex(0)
        self.scoreComboBox.setStyleSheet(combo_box_style)

        self.submitButton = QPushButton("Внести баллы", self)
        self.submitButton.clicked.connect(self.add_score)
        self.submitButton.setStyleSheet(add_button_style)

        self.allScoresButton = QPushButton("Все баллы", self)
        self.allScoresButton.clicked.connect(self.showAllScores)
        self.allScoresButton.setStyleSheet(add_button_style)

        self.deleteVolunteerButton = QPushButton("Удалить волонтера", self)
        self.deleteVolunteerButton.clicked.connect(self.delete_volunteer)
        self.deleteVolunteerButton.setStyleSheet(add_button_style)

        self.deleteTaskButton = QPushButton("Удалить задание", self)
        self.deleteTaskButton.clicked.connect(self.delete_task)
        self.deleteTaskButton.setStyleSheet(add_button_style)

        self.scoreComboBox.setVisible(False)
        self.submitButton.setVisible(False)
        self.allScoresButton.setVisible(True)
        self.volunteerNameLineEdit.setVisible(False)
        self.addVolunteerButton.setVisible(False)
        self.taskNameLineEdit.setVisible(False)
        self.taskDescriptionLineEdit.setVisible(False)
        self.taskScoreLineEdit.setVisible(False)
        self.addTaskButton.setVisible(False)
        self.deleteTaskButton.setVisible(False)
        self.taskComboBox.setVisible(False)
        self.deleteVolunteerButton.setVisible(False)
        self.set_fields_visibility(False)

        self.welcomeLabel.setFont(comic_sans_font)
        self.descriptionLabel.setFont(comic_sans_font)
        self.volunteerNameLineEdit.setFont(comic_sans_font)
        self.addVolunteerButton.setFont(comic_sans_font)
        self.taskComboBox.setFont(comic_sans_font)
        self.taskNameLineEdit.setFont(comic_sans_font)
        self.taskDescriptionLineEdit.setFont(comic_sans_font)
        self.taskScoreLineEdit.setFont(comic_sans_font)
        self.addTaskButton.setFont(comic_sans_font)
        self.scoreComboBox.setFont(comic_sans_font)
        self.submitButton.setFont(comic_sans_font)
        self.allScoresButton.setFont(comic_sans_font)
        self.deleteVolunteerButton.setFont(comic_sans_font)
        self.deleteTaskButton.setFont(comic_sans_font)
        self.personComboBox.setFont(comic_sans_font)
        self.themeButton.setFont(comic_sans_font)

        layout.addWidget(self.welcomeLabel)
        layout.addWidget(self.descriptionLabel)
        layout.addWidget(self.personComboBox)
        layout.addWidget(self.taskComboBox)
        layout.addWidget(self.scoreComboBox)
        layout.addWidget(self.submitButton)
        layout.addWidget(self.taskNameLineEdit)
        layout.addWidget(self.taskDescriptionLineEdit)
        layout.addWidget(self.taskScoreLineEdit)
        layout.addWidget(self.addTaskButton)
        layout.addWidget(self.volunteerNameLineEdit)
        layout.addWidget(self.addVolunteerButton)
        layout.addWidget(self.deleteVolunteerButton)
        layout.addWidget(self.deleteTaskButton)
        layout.addWidget(self.allScoresButton)

        self.data_filename = os.path.join(appdata_path, 'volunteers.json')
        self.tasks_filename = os.path.join(appdata_path, 'tasks.json')

        if not os.path.exists(self.data_filename):

            with open(self.data_filename, 'w') as file:
                json.dump({}, file)

        if not os.path.exists(self.tasks_filename):

            with open(self.tasks_filename, 'w') as file:
                json.dump({}, file)

        self.load_data()
        self.load_theme()

    def addVolunteer(self):
        volunteer_name = self.volunteerNameLineEdit.text()

        if volunteer_name:
            self.personComboBox.addItem(volunteer_name)

            if volunteer_name not in self.data:
                self.data[volunteer_name] = {}

            self.volunteerNameLineEdit.clear()
            QMessageBox.information(self, "Уведомление", "Волонтёр успешно добавлен!")
            self.save_data()

    def addTask(self):
        task_name = self.taskNameLineEdit.text()
        task_description = self.taskDescriptionLineEdit.text()
        task_score = self.taskScoreLineEdit.text()

        if task_name and task_description and task_score:
            task_item = f"{task_name} - {task_description}"

            if task_item not in [self.taskComboBox.itemText(i) for i in range(self.taskComboBox.count())]:
                self.taskComboBox.addItem(task_item)

            with open(self.tasks_filename, 'r', encoding='utf-8') as file:
                tasks_data = json.load(file)

            if task_item in tasks_data:
                existing_task_info = tasks_data[task_item]
                existing_task_scores = existing_task_info.get("score", [])
                existing_task_scores.append(task_score)
                existing_task_info["score"] = existing_task_scores
            else:
                tasks_data[task_item] = {
                    "name": task_name,
                    "description": task_description,
                    "score": [task_score]
                }

            with open(self.tasks_filename, 'w', encoding='utf-8') as file:
                json.dump(tasks_data, file, indent=4)

            self.taskNameLineEdit.clear()
            self.taskDescriptionLineEdit.clear()
            self.taskScoreLineEdit.clear()

            self.save_data()

            QMessageBox.information(self, "Уведомление", "Задание успешно добавлено!")

    def delete_volunteer(self):
        selected_volunteer = self.personComboBox.currentText()
        if selected_volunteer != "Не выбрано" and selected_volunteer in self.data:
            del self.data[selected_volunteer]
            self.save_data()
            self.personComboBox.removeItem(self.personComboBox.currentIndex())
            self.deleteVolunteerButton.setVisible(False)
            self.personComboBox.setCurrentIndex(0)
            self.taskComboBox.setCurrentIndex(0)
            self.deleteTaskButton.setVisible(False)
            self.set_fields_visibility(False)
            self.taskComboBox.setVisible(False)
            self.welcomeLabel.setVisible(True)
            self.descriptionLabel.setVisible(True)
            QMessageBox.information(self, "Уведомление", "Удаление произошло успешно!")

    def delete_task(self):
        selected_task = self.taskComboBox.currentText()
        if selected_task != "Не выбрано":
            for person in self.data.keys():
                if selected_task in self.data[person]:
                    del self.data[person][selected_task]
            self.save_data()
            self.taskComboBox.removeItem(self.taskComboBox.currentIndex())

            with open(self.tasks_filename, 'r') as file:
                tasks_data = json.load(file)
                if selected_task in tasks_data:
                    del tasks_data[selected_task]
            
            with open(self.tasks_filename, 'w') as file:
                json.dump(tasks_data, file, indent=4)

            self.taskComboBox.setCurrentIndex(0)
            self.set_fields_visibility(False)
            self.deleteTaskButton.setVisible(False)
            self.welcomeLabel.setVisible(True)
            self.descriptionLabel.setVisible(False)
            QMessageBox.information(self, "Уведомление", "Удаление произошло успешно!")

    def eventFilter(self, obj, event):
        if obj is not None:
            if event.type() == QEvent.Enter:
                if obj == self.closeButton:
                    obj.setIcon(QIcon(self.closeHoverPixmap))
                elif obj == self.minimizeButton:
                    obj.setIcon(QIcon(self.minimizeHoverPixmap))
                elif obj == self.themeButton:
                    obj.setIcon(QIcon(self.themeHoverPixmap))
            elif event.type() == QEvent.Leave:
                if obj == self.closeButton:
                    obj.setIcon(QIcon(self.closePixmap))
                elif obj == self.minimizeButton:
                    obj.setIcon(QIcon(self.minimizePixmap))
                elif obj == self.themeButton:
                    obj.setIcon(QIcon(self.themePixmap))
        return super().eventFilter(obj, event)

    def add_score(self):
        person = self.personComboBox.currentText()
        task = self.taskComboBox.currentText()
        score = self.scoreComboBox.currentText()

        if person == "Не выбрано" or task == "Не выбрано":
            return

        if person not in self.data:
            self.data[person] = {}
        if task not in self.data[person]:
            self.data[person][task] = 0

        try:
            score = int(score)
            self.data[person][task] += score
            self.save_data()
        except ValueError:
            pass
        QMessageBox.information(self, "Уведомление", "Баллы были внесены!")

    def set_fields_visibility(self, visible):

        self.scoreComboBox.setVisible(visible)
        self.submitButton.setVisible(visible)

    def on_person_changed(self):
        current_person = self.personComboBox.currentText()

        if current_person == "Не выбрано" or current_person == "Добавить волонтёра...":
            self.taskComboBox.setCurrentIndex(0)
            self.deleteTaskButton.setVisible(False)

        if current_person == "Не выбрано":
            self.set_fields_visibility(False)
            self.deleteVolunteerButton.setVisible(False) 
            self.addVolunteerButton.setVisible(False) 
            self.volunteerNameLineEdit.setVisible(False)
            self.taskComboBox.setVisible(False)
            self.taskNameLineEdit.setVisible(False)
            self.taskDescriptionLineEdit.setVisible(False)
            self.taskScoreLineEdit.setVisible(False)
            self.addTaskButton.setVisible(False)
            self.welcomeLabel.setVisible(True)
            self.descriptionLabel.setVisible(True)
            self.current_step = 0 
        elif current_person == "Добавить волонтёра...":
            self.set_fields_visibility(False)
            self.deleteVolunteerButton.setVisible(False)  
            self.addVolunteerButton.setVisible(True) 
            self.volunteerNameLineEdit.setVisible(True)
            self.taskComboBox.setVisible(False)
            self.taskNameLineEdit.setVisible(False)
            self.taskDescriptionLineEdit.setVisible(False)
            self.taskScoreLineEdit.setVisible(False)
            self.addTaskButton.setVisible(False)
            self.welcomeLabel.setVisible(True)
            self.descriptionLabel.setVisible(False)
            self.current_step = 0  
        else:
            self.set_fields_visibility(self.current_step >= 1)
            self.deleteVolunteerButton.setVisible(True)
            self.addVolunteerButton.setVisible(False)
            self.volunteerNameLineEdit.setVisible(False)
            self.scoreComboBox.setVisible(False)
            self.taskComboBox.setVisible(True)
            self.submitButton.setVisible(False)
            self.welcomeLabel.setVisible(True)
            self.descriptionLabel.setVisible(False)
            self.taskComboBox.setCurrentIndex(0)
            self.deleteTaskButton.setVisible(False)
            self.taskNameLineEdit.setVisible(False)
            self.taskDescriptionLineEdit.setVisible(False)
            self.taskScoreLineEdit.setVisible(False)
            self.addTaskButton.setVisible(False)

            self.allScoresButton.setVisible(True)

    def on_task_changed(self):
        current_task = self.taskComboBox.currentText()

        if current_task == "Не выбрано":
            self.taskNameLineEdit.setVisible(False)
            self.taskDescriptionLineEdit.setVisible(False)
            self.taskScoreLineEdit.setVisible(False)
            self.scoreComboBox.setVisible(False)
            self.submitButton.setVisible(False)
            self.deleteTaskButton.setVisible(False)
            self.addTaskButton.setVisible(False)
            self.welcomeLabel.setVisible(True)
            self.descriptionLabel.setVisible(False)
            self.current_step = 0
        elif current_task == "Добавить задание...":
            self.taskNameLineEdit.setVisible(True)
            self.taskDescriptionLineEdit.setVisible(True)
            self.taskScoreLineEdit.setVisible(True)
            self.addTaskButton.setVisible(True)
            self.scoreComboBox.setVisible(False)
            self.submitButton.setVisible(False)
            self.deleteTaskButton.setVisible(False)
            self.welcomeLabel.setVisible(False)
            self.descriptionLabel.setVisible(False)
            self.current_step = 0
        else:
            self.taskNameLineEdit.setVisible(False)
            self.taskDescriptionLineEdit.setVisible(False)
            self.taskScoreLineEdit.setVisible(False)
            self.addTaskButton.setVisible(False)
            self.set_fields_visibility(self.current_step >= 1)
            self.deleteTaskButton.setVisible(True)
            self.welcomeLabel.setVisible(False)
            self.descriptionLabel.setVisible(False)
            if self.current_step == 0:
                self.current_step = 1
                self.scoreComboBox.setVisible(True)
                self.submitButton.setVisible(True)

        self.allScoresButton.setVisible(True)
        self.update_score_combobox()

    def save_data(self):
        with open(self.data_filename, 'w') as file:
            json.dump(self.data, file, indent=4)

    def load_data(self):
        try:
            with open(self.data_filename, 'r') as file:
                self.data = json.load(file)

                self.update_person_combobox()
                self.update_task_combobox()

        except FileNotFoundError:
            self.data = {}

    def update_person_combobox(self):
        self.personComboBox.clear()

        self.personComboBox.addItem("Не выбрано")

        for volunteer_name in self.data.keys():
            self.personComboBox.addItem(volunteer_name)

        self.personComboBox.addItem("Добавить волонтёра...")

        self.personComboBox.setCurrentIndex(0)

    def update_score_combobox(self):
        self.scoreComboBox.clear()

        selected_task = self.taskComboBox.currentText()

        if selected_task != "Не выбрано" and selected_task != "Добавить задание...":
            with open(self.tasks_filename, 'r') as file:
                tasks_data = json.load(file)

                selected_task_info = tasks_data.get(selected_task)

                if selected_task_info:
                    task_score = selected_task_info.get("score")

                    if isinstance(task_score, str):  # Проверьте, является ли это строкой
                        scores = task_score.split(',')
                        for score in scores:
                            self.scoreComboBox.addItem(score.strip())
                    elif isinstance(task_score, list):  # Обработайте случай, если это список
                        for score in task_score:
                            self.scoreComboBox.addItem(str(score))

    def update_task_combobox(self):
        self.taskComboBox.clear()

        self.taskComboBox.addItem("Не выбрано")

        with open(self.tasks_filename, 'r') as file:
            tasks_data = json.load(file)
            for task in tasks_data.keys():
                self.taskComboBox.addItem(task)

        self.taskComboBox.addItem("Добавить задание...")

        self.taskComboBox.setCurrentIndex(0)

    def center_window(self):
        desktop = QDesktopWidget()
        screen_geometry = desktop.screenGeometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)

    def showAllScores(self):
        self.showAllScoresWindow()

    def showAllScoresWindow(self):
        self.allScoresWindow = AllScoresWindow(self.data)
        self.allScoresWindow.custom_window = self
        self.allScoresWindow.show()
        self.hide()

    def toggle_theme(self):
        current_stylesheet = self.styleSheet()
        if "background-color: #2E2E2E;" in current_stylesheet:
            new_stylesheet = """
                background-color: #F0F0F0;
                color: black;
            """
            self.welcomeLabel.setStyleSheet("color: black; font-size: 20px; font-weight: bold;")
            self.descriptionLabel.setStyleSheet("color: black;")
            theme_name = 'light'
        else:
            new_stylesheet = """
                background-color: #2E2E2E;
                color: white;
            """
            self.welcomeLabel.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
            self.descriptionLabel.setStyleSheet("color: white;")
            theme_name = 'dark'

        self.setStyleSheet(new_stylesheet)
        self.save_theme(theme_name, theme_config_file)

    def save_theme(self, theme_name, config_file):
        config = configparser.ConfigParser()
        config['Theme'] = {'current_theme': theme_name}

        with open(config_file, 'w') as configfile:
            config.write(configfile)

    def load_theme(self):
        if os.path.isfile(theme_config_file):
            config = configparser.ConfigParser()
            config.read(theme_config_file)

            if 'Theme' in config:
                theme_name = config['Theme'].get('current_theme', 'light')
                if theme_name == 'light':
                    self.apply_light_theme()
                elif theme_name == 'dark':
                    self.apply_dark_theme()
        else:
            self.save_theme('light', theme_config_file)

    def apply_light_theme(self):
        self.setStyleSheet("""
            background-color: #F0F0F0;
            color: black;
        """)
        self.welcomeLabel.setStyleSheet("color: black; font-size: 20px; font-weight: bold;")
        self.descriptionLabel.setStyleSheet("color: black;")

    def apply_dark_theme(self):
        self.setStyleSheet("""
            background-color: #2E2E2E;
            color: white;
        """)
        self.welcomeLabel.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        self.descriptionLabel.setStyleSheet("color: white;")

class AllScoresWindow(QWidget):
    def __init__(self, data):
        super().__init__()

        self.setWindowTitle("Все баллы")
        self.setGeometry(0, 0, 1000, 700)

        self.setStyleSheet("""
            background-color: #2E2E2E;
            color: white;
        """)
        
        comic_sans_font = QFont("Comic Sans MS", 18)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setMouseTracking(True)

        layout = QVBoxLayout(self)

        buttonLayout = QHBoxLayout()
        spacer = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        buttonLayout.addItem(spacer)

        self.minimizeButton = QPushButton(self)
        self.minimizeButton.setIconSize(QSize(17, 17))

        minimize_image_url = 'https://i.ibb.co/zGPGr0h/collapse.png'
        filename_minimize = os.path.join(appdata_path, 'collapse.png')

        if not os.path.exists(filename_minimize):
            response = requests.get(minimize_image_url)
            with open(filename_minimize, 'wb') as file:
                file.write(response.content)

        self.minimizeButton.setIcon(QIcon(filename_minimize))
        self.minimizePixmap = QPixmap(filename_minimize)
        self.minimizeButton.setStyleSheet("background-color: transparent; border: none;")
        self.minimizeButton.clicked.connect(self.showMinimized)

        self.minimizeButton.installEventFilter(self)

        minimize_hover_image_url = 'https://i.ibb.co/Zz2f1xD/collapse-hover.png'
        filename_minimize_hover = os.path.join(appdata_path, 'collapse_hover.png')

        if not os.path.exists(filename_minimize_hover):
            response = requests.get(minimize_hover_image_url)
            with open(filename_minimize_hover, 'wb') as file:
                file.write(response.content)

        self.minimizeHoverPixmap = QPixmap(filename_minimize_hover)
        self.minimizeHoverPixmap = self.minimizeHoverPixmap.scaled(QSize(17, 17), Qt.KeepAspectRatio, Qt.SmoothTransformation)

        buttonLayout.addWidget(self.minimizeButton, alignment=Qt.AlignRight | Qt.AlignTop)

        self.closeButton = QPushButton(self)
        self.closeButton.setIconSize(QSize(15, 15))

        close_image_url = 'https://i.ibb.co/5v560wy/close.png'
        filename_close = os.path.join(appdata_path, 'close.png')

        if not os.path.exists(filename_close):
            response = requests.get(close_image_url)
            with open(filename_close, 'wb') as file:
                file.write(response.content)

        self.closeButton.setIcon(QIcon(filename_close))
        self.closePixmap = QPixmap(filename_close)
        self.closeButton.setStyleSheet("background-color: transparent; border: none;")
        self.closeButton.clicked.connect(self.close)

        self.closeButton.installEventFilter(self)

        close_hover_image_url = 'https://i.ibb.co/nnVTyxj/close-hover.png' 
        filename_close_hover = os.path.join(appdata_path, 'close_hover.png')

        if not os.path.exists(filename_close_hover):
            response = requests.get(close_hover_image_url)
            with open(filename_close_hover, 'wb') as file:
                file.write(response.content)

        self.closeHoverPixmap = QPixmap(filename_close_hover)
        self.closeHoverPixmap = self.closeHoverPixmap.scaled(QSize(15, 15), Qt.KeepAspectRatio, Qt.SmoothTransformation)

        buttonLayout.addWidget(self.closeButton, alignment=Qt.AlignRight | Qt.AlignTop)

        layout.addLayout(buttonLayout)

        title_label = QLabel("Баллы всех людей", self)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 10px;")
        title_label.setFont(comic_sans_font)
        layout.addWidget(title_label, alignment=Qt.AlignHCenter | Qt.AlignTop)

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setGeometry(100, 100, 400, 200)
        self.scores_widget = ScoresWidget(data)
        self.scroll_area.setWidget(self.scores_widget)
        self.scores_widget.setContentsMargins(0, 0, 0, 0)
        self.scroll_area.setStyleSheet("border: none;")

        scroll_area_width = 400
        scroll_area_height = 200

        window_width = 600
        window_height = 400

        x = (window_width - scroll_area_width) // 2
        y = (window_height - scroll_area_height) // 2

        self.scroll_area.setGeometry(x, y, scroll_area_width, scroll_area_height)

        self.scores_widget = ScoresWidget(data)
        self.scroll_area.setWidget(self.scores_widget)

        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        layout.addWidget(self.scroll_area)

        add_button_style = """
            QPushButton {
                background-color: #483D8B; /* Зеленый цвет фона */
                color: white; /* Белый цвет текста */
                border: none; /* Убираем границу */
                padding: 5px 10px; /* Отступы внутри кнопки */
                font-size: 14px; /* Размер шрифта */
                border-radius: 5px; /* Закругление углов */
            }

            QPushButton:hover {
                background-color: #4D4491; /* Цвет фона при наведении */
            }
        """

        self.backButton = QPushButton("Назад", self)
        self.backButton.clicked.connect(self.open_custom_window)
        self.backButton.setStyleSheet(add_button_style)
        self.backButton.setFont(comic_sans_font)
        layout.addWidget(self.backButton, alignment=Qt.AlignCenter)

        self.custom_window = None

        self.center_window()
        self.load_theme()

    def eventFilter(self, obj, event):
        if obj is not None:
            if event.type() == QEvent.Enter:
                if obj == self.closeButton:
                    obj.setIcon(QIcon(self.closeHoverPixmap))
                elif obj == self.minimizeButton:
                    obj.setIcon(QIcon(self.minimizeHoverPixmap))
            elif event.type() == QEvent.Leave:
                if obj == self.closeButton:
                    obj.setIcon(QIcon(self.closePixmap))
                elif obj == self.minimizeButton:
                    obj.setIcon(QIcon(self.minimizePixmap))
        return super().eventFilter(obj, event)

    def center_window(self):
        desktop = QDesktopWidget()
        screen_geometry = desktop.screenGeometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)

    def open_custom_window(self):
        if self.custom_window:
            self.custom_window.show()
            self.close()
    
    def load_theme(self):
        if os.path.isfile(theme_config_file):
            config = configparser.ConfigParser()
            config.read(theme_config_file)

            if 'Theme' in config:
                theme_name = config['Theme'].get('current_theme', 'light')
                if theme_name == 'light':
                    self.apply_light_theme()
                elif theme_name == 'dark':
                    self.apply_dark_theme()
        else:
            self.save_theme('light', theme_config_file)

    def apply_light_theme(self):
        self.setStyleSheet("""
            background-color: #F0F0F0;
            color: black;
        """)

    def apply_dark_theme(self):
        self.setStyleSheet("""
            background-color: #2E2E2E;
            color: white;
        """)

class ScoresWidget(QWidget):
    def __init__(self, data):
        super().__init__()

        self.setWindowFlag(Qt.FramelessWindowHint)

        layout = QVBoxLayout(self)

        sorted_data = dict(sorted(data.items()))

        all_scores_label = QLabel(self)
        all_scores_text = "<html>"

        for person, scores in sorted_data.items():
            all_scores_text += f"<p><b>{person}:</b></p>"
            all_scores_text += "<ul>"
            total_score = 0  
            for task, score in scores.items():
                all_scores_text += f"<li>{task}: {score} баллов</li>"
                total_score += score  
            all_scores_text += f"<li><b>Всего баллов:</b> {total_score} баллов</li>"
            all_scores_text += "</ul>"

        all_scores_text += "</html>"
        all_scores_label.setText(all_scores_text)

        comic_sans_font = QFont("Comic Sans MS", 16)
        all_scores_label.setFont(comic_sans_font)

        all_scores_label.setStyleSheet("font-size: 16px;")
        layout.addWidget(all_scores_label)

        self.setLayout(layout)
        self.load_theme()

    def load_theme(self):
        if os.path.isfile(theme_config_file):
            config = configparser.ConfigParser()
            config.read(theme_config_file)

            if 'Theme' in config:
                theme_name = config['Theme'].get('current_theme', 'light')
                if theme_name == 'light':
                    self.apply_light_theme()
                elif theme_name == 'dark':
                    self.apply_dark_theme()
        else:
            self.save_theme('light', theme_config_file)

    def apply_light_theme(self):
        self.setStyleSheet("""
            background-color: #F0F0F0;
            color: black;
        """)

    def apply_dark_theme(self):
        self.setStyleSheet("""
            background-color: #2E2E2E;
            color: white;
        """)

appdata_path = os.path.expanduser("~\\AppData\\Roaming\\queran")

if not os.path.exists(appdata_path):
    os.makedirs(appdata_path)

theme_config_file = os.path.join(appdata_path, 'theme.cfg')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CustomWindow()
    window.center_window()
    window.show()
    sys.exit(app.exec_())

# Нужно реализовать поиск по ФИО
# Нужно сделать кнопки который будут противоположны теме (белая тема = чёрные кнопочки)
# Нужно сделать окно с контактами где будет связь со мной (как разрабом) и Ирой
# Нужно сделать попробовать сделать динамическое окно, т. е. оно будет меняться по мере поступления информации, чтобы не было пустых мест