from simple_blogger.blogger.finite.cached import CachedFiniteSimpleBlogger
from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.generator.openai import OpenAiTextGenerator, OpenAiImageGenerator
from datetime import date

class ProblemBlogger(CachedFiniteSimpleBlogger):
    def _system_prompt(self):
        return 'Ты - архитектор решений'
    
    def root_folder(self):
        return f"./files/about_sql/problem"
    
    def _path_constructor(self, task):
        return f"{task['technology']},{task['soft']}/{task['problem']}"
    
    def _message_prompt_constructor(self, task):
        return f"Опиши проблему '{task['problem']}' связанную с технологией '{task['technology']}' и программным средством '{task['soft']}' из области '{task['domain']}', не описывай решение, используй не более 300 слов"
    
    def _image_prompt_constructor(self, task):
        return f"Нарисуй рисунок, вдохновлённый проблемой '{task['problem']}' связанную с технологией '{task['technology']}' и программным средством '{task['soft']}' из области '{task['domain']}'"
        
    def _message_generator(self):
        return OpenAiTextGenerator(self._system_prompt())
    
    def _image_generator(self):
        return OpenAiImageGenerator()
    
    def _posters(self):
        return [
            TelegramPoster(chat_id='@about_sql', send_text_with_image=False)
        ]

    def __init__(self, posters=None):
        super().__init__(posters=posters or self._posters())

class ProblemReviewer(ProblemBlogger):
    def _check_task(self, task, days_before=2, **_):
        return super()._check_task(task, days_before, **_)

class SolutionBlogger(CachedFiniteSimpleBlogger):
    def _system_prompt(self):
        return 'Ты - архитектор решений'
    
    def root_folder(self):
        return f"./files/about_sql/solution"
    
    def _path_constructor(self, task):
        return f"{task['technology']},{task['soft']}/{task['problem']}"
    
    def _message_prompt_constructor(self, task):
        return f"Опиши решение проблемы '{task['problem']}' связанной с технологией '{task['technology']}' и программным средством '{task['soft']}' из области '{task['domain']}', используй не более 300 слов"
    
    def _image_prompt_constructor(self, task):
        return f"Нарисуй рисунок, вдохновлённый решением проблемы '{task['problem']}' связанной с технологией '{task['technology']}' и программным средством '{task['soft']}' из области '{task['domain']}'"
        
    def _message_generator(self):
        return OpenAiTextGenerator(self._system_prompt())
    
    def _image_generator(self):
        return OpenAiImageGenerator()
    
    def _posters(self):
        return [
            TelegramPoster(chat_id='@about_sql', send_text_with_image=False)
        ]

    def __init__(self, posters=None):
        super().__init__(posters=posters or self._posters())

class SolutionReviewer(SolutionBlogger):
    def _check_task(self, task, days_before=2, **_):
        return super()._check_task(task, days_before, **_)

def review():
    blogger = ProblemReviewer(
        posters=[TelegramPoster(chat_id=-1002396564369, send_text_with_image=False)]
        # posters=[TelegramPoster(send_text_with_image=False)]
    )
    blogger.post()
    blogger = SolutionReviewer(
        posters=[TelegramPoster(chat_id=-1002396564369, send_text_with_image=False)]
        # posters=[TelegramPoster(send_text_with_image=False)]
    )
    blogger.post()

def post(index=None):
    if index is None:
        blogger = ProblemBlogger()
        blogger.post()
    else:
        blogger = SolutionBlogger()
        blogger.post()

def init():
    bloggers = [ProblemBlogger(), SolutionBlogger()]
    for blogger in bloggers:
        blogger.init_project()

def make_tasks():   
    bloggers = [ProblemBlogger(), SolutionBlogger()]
    for blogger in bloggers:
        blogger.create_simple_tasks(first_post_date=date(2025, 3, 3),days_between_posts=7, shuffle=False)