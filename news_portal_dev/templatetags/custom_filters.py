from django import template

register = template.Library()


BAD_WORDS = ['мудак', 'дебил', 'ламо']

@register.filter()
def badwords(value):
   try:
       value = str(value)
   except ValueError as e:
      return f'Exception {e}'
   new_news = ''
   value = value.split()
   for word in value:
       if word.lower() not in BAD_WORDS:
           new_news += word + '\n'
       else:
          new_news += word[0] + '*' * (len(word) - 1) + '\n'
   return f'{new_news}'





