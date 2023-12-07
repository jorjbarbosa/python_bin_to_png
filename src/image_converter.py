from PyQt5.QtWidgets import QMainWindow, QFileDialog, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from image_processing import read_and_convert_to_png

class ImageConverterApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Image Converter')
        self.setGeometry(100, 100, 400, 300)

        self.file_label = QLabel('Select input file:')
        self.file_button = QPushButton('Browse')
        self.file_button.clicked.connect(self.get_input_file)

        self.output_label = QLabel('Output file:')
        self.output_file = QLabel()

        self.convert_button = QPushButton('Convert')
        self.convert_button.clicked.connect(self.convert_image)

        self.preview_label = QLabel('Image Preview:')
        self.image_preview = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.file_label)
        layout.addWidget(self.file_button)
        layout.addWidget(self.output_label)
        layout.addWidget(self.output_file)
        layout.addWidget(self.convert_button)
        layout.addWidget(self.preview_label)
        layout.addWidget(self.image_preview)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def get_input_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, 'Select input file', '', 'All Files (*);;Binary Files (*.bin);;PNG Files (*.png)', options=options)
        
        if file_name:
            self.input_file = file_name
            self.output_file.setText(f'{self.input_file.replace(".bin", ".png")}')

    def convert_image(self):
        if hasattr(self, 'input_file'):
            output_file = self.input_file.replace(".bin", ".png")
            read_and_convert_to_png(self.input_file, output_file)
            self.show_image_preview(output_file)

    def show_image_preview(self, image_path):
        pixmap = QPixmap(image_path)
        self.image_preview.setPixmap(pixmap.scaledToWidth(200))
        self.image_preview.setAlignment(Qt.AlignCenter)
