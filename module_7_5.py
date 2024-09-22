import os
import time

directory = r'D:\Pyton_project\Serg\datas\7mod'

for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = os.path.join(str(directory))
    filetime = os.path.getmtime(file)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(file)
    parent_dir = os.path.dirname(directory)
    print(f'Обнаружен файл: {file}, Путь: {filepath},'
          f' Размер: {filesize} байт, Время изменения: {formatted_time},'
          f' Родительская директория: {parent_dir}')
