from simple_blogger.blogger.finite.cached import CachedFiniteSimpleBlogger
from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.instagram import InstagramPoster
from simple_blogger.generator.openai import OpenAiTextGenerator, OpenAiImageGenerator
from datetime import date

class CoachProblemBlogger(CachedFiniteSimpleBlogger):
    def _system_prompt(self):
        return 'Ты - коуч будущего с передовыми техниками, нестандартными инсайтами и проверенными стратегиями, которые помогут твоим клиентам создать свою новую реальность'
    
    def root_folder(self):
        return f"./files/NextToTheFuture/problem"
    
    def _path_constructor(self, task):
        return f"{task['group']},{task['technic']}/{task['problem']}"
    
    def _message_prompt_constructor(self, task):
        return f"Опиши проблему '{task['problem']}' из области '{task['group']}', не описывай решение, создай заголовок и выдели его одиночными обратными апострофами, сократи текст до тезизов 'Как было', 'Причины', 'Что сделано', 'Результат', используй не более 300 слов"
    
    def _image_prompt_constructor(self, task):
        return f"Нарисуй рисунок, вдохновлённый проблемой '{task['problem']}' из области '{task['group']}'"
        
    def _message_generator(self):
        return OpenAiTextGenerator(self._system_prompt())
    
    def _image_generator(self):
        return OpenAiImageGenerator()
    
    def _posters(self):
        return [
            TelegramPoster(chat_id='@NextToTheFuture', send_text_with_image=False),
            InstagramPoster(account_token_name='FUTUREUNLOCKED_OFFICIAL_TOKEN')
        ]

    def __init__(self, posters=None):
        super().__init__(posters=posters or self._posters())

class CoachProblemReviewer(CoachProblemBlogger):
    def _check_task(self, task, days_before=1, **_):
        return super()._check_task(task, days_before, **_)


class CoachSolutionBlogger(CachedFiniteSimpleBlogger):
    def _system_prompt(self):
        return 'Ты - коуч будущего с передовыми техниками, нестандартными инсайтами и проверенными стратегиями, которые помогут твоим клиентам создать свою новую реальность'
    
    def root_folder(self):
        return f"./files/NextToTheFuture/solution"
    
    def _path_constructor(self, task):
        return f"{task['group']},{task['technic']}/{task['problem']}"
    
    def _message_prompt_constructor(self, task):
        return f"Опиши решение проблемы '{task['problem']}' с помощью техники '{task['technic']}' из области '{task['group']}', создай заголовок и выдели его одиночными обратными апострофами, используй не более 300 слов"
    
    def _image_prompt_constructor(self, task):
        return f"Нарисуй рисунок, вдохновлённый темой '{task['technic']}' из области '{task['group']}'"
        
    def _message_generator(self):
        return OpenAiTextGenerator(self._system_prompt())
    
    def _image_generator(self):
        return OpenAiImageGenerator()
    
    def _posters(self):
        return [
            TelegramPoster(chat_id='@NextToTheFuture', send_text_with_image=False),
            InstagramPoster(account_token_name='FUTUREUNLOCKED_OFFICIAL_TOKEN')
        ]

    def __init__(self, posters=None):
        super().__init__(posters=posters or self._posters())

class CoachSolutionReviewer(CoachSolutionBlogger):
    def _check_task(self, task, days_before=1, **_):
        return super()._check_task(task, days_before, **_)

def review():
    blogger = CoachProblemReviewer(
        posters=[TelegramPoster(chat_id=-1002312034777, send_text_with_image=False)]
        # posters=[TelegramPoster(send_text_with_image=False)]
    )
    blogger.post()
    blogger = CoachSolutionReviewer(
        posters=[TelegramPoster(chat_id=-1002312034777, send_text_with_image=False)]
        # posters=[TelegramPoster(send_text_with_image=False)]
    )
    blogger.post()

def post(index=None):
    if index is None:
        blogger = CoachProblemBlogger()
        blogger.post()
    else:
        blogger = CoachSolutionBlogger()
        blogger.post()

def init():
    bloggers = [CoachProblemBlogger(), CoachSolutionBlogger()]
    for blogger in bloggers:
        blogger.init_project()

def make_tasks():   
    bloggers = [CoachProblemBlogger(), CoachSolutionBlogger()]
    for blogger in bloggers:
        blogger.create_simple_tasks(first_post_date=date(2025, 2, 24),days_between_posts=3)
