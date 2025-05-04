import gradio as gr
import os
from PIL import Image

# Путь к папке с изображениями
image_folder = "./images"

# Функция для загрузки изображения по имени файла
def load_image(filename):
    return Image.open(os.path.join(image_folder, filename))

# Получаем список изображений из указанной папки
image_files = [
    f for f in os.listdir(image_folder)
    if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))
]

# Создаем интерфейс
interface = gr.Interface(
    fn=load_image,
    inputs=gr.Dropdown(choices=image_files, label="Выберите изображение"),
    outputs=gr.Image(label="Выбранное изображение"),
    live=False,
    title="Галерея изображений",
    description="Выберите изображение из папки './images' для просмотра."
)

# Запуск приложения
if __name__ == "__main__":
    interface.launch()
