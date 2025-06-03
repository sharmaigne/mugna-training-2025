@register.simple_tag(takes_context=True)
def get_genre_count(context, genre):
    return context['movies'].filter(genre=genre).count()

