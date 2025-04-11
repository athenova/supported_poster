from simple_blogger.blogger.auto import AutoBlogger
from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.editor import Editor
from simple_blogger.generator.openai import OpenAiTextGenerator, OpenAiImageGenerator
from datetime import date

root_folder = f"./files/FinancialQuest"

class FinanceBlogger(AutoBlogger):
    def _system_prompt(self):
        return 'Ты - известный финансист, блоггер с 1000000 подписчиков'
    
    def root_folder(self):
        return root_folder
    
    def _path_constructor(self, task):
        return f"{task['category']}/{task['topic']}"
    
    def _message_prompt_constructor(self, task):
        return f"Выбери рандомно актуальную проблему по теме '{task['topic']}' из области '{task['category']}', опиши проблему, выбери рандомно метод решения, опиши метод решения, используй смайлики, используй менее 300 слов"
    
    def _image_prompt_constructor(self, task):
        return f"Нарисуй картинку, вдохновлённую темой '{task['topic']}' из области '{task['category']}'"
        
    def _message_generator(self):
        return OpenAiTextGenerator(self._system_prompt())
    
    def _image_generator(self):
        return OpenAiImageGenerator()
    
    def _posters(self):
        return [
            TelegramPoster(chat_id='@FinancialQuest',send_text_with_image=False)
        ]

    def __init__(self, posters=None, force_rebuild=False):
        super().__init__(posters=posters or self._posters(), first_post_date=date(2025, 3, 4), force_rebuild=force_rebuild)

class FinanceReviewer(FinanceBlogger):
    def _check_task(self, task, tasks, days_before=1):
        return super()._check_task(task, tasks, days_before)

def review():
    blogger = FinanceReviewer(
        # posters=[TelegramPoster(send_text_with_image=False)]
        posters=[TelegramPoster(chat_id=-1002396564369,send_text_with_image=False)],
        force_rebuild=True
    )
    blogger.post()

def post():
    blogger = FinanceBlogger()
    blogger.post()

def init():
    editor = Editor(root_folder)
    editor.init_project()

def make_tasks():
    editor = Editor(root_folder)
    editor.create_auto()
