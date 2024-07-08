from django.contrib.auth.models import User
from news.models import Author, Category, Post, Comment

# Создание пользователей
user1 = User.objects.create_user('user1', 'user1@example.com', 'password1')
user2 = User.objects.create_user('user2', 'user2@example.com', 'password2')

# Создание авторов
author1 = Author.objects.create(user=user1)
author2 = Author.objects.create(user=user2)

# Создание категорий
cat1 = Category.objects.create(name='Спорт')
cat2 = Category.objects.create(name='Политика')
cat3 = Category.objects.create(name='Образование')
cat4 = Category.objects.create(name='Технологии')

# Создание постов
post1 = Post.objects.create(author=author1, post_type='AR', title='Первая статья', text='Текст первой статьи')
post2 = Post.objects.create(author=author1, post_type='AR', title='Вторая статья', text='Текст второй статьи')
news1 = Post.objects.create(author=author2, post_type='NW', title='Первая новость', text='Текст первой новости')

# Присвоение категорий постам
post1.categories.add(cat1, cat2)
post2.categories.add(cat3)
news1.categories.add(cat2, cat4)

# Создание комментариев
comment1 = Comment.objects.create(post=post1, user=user1, text='Комментарий к первой статье')
comment2 = Comment.objects.create(post=post1, user=user2, text='Еще один комментарий к первой статье')
comment3 = Comment.objects.create(post=post2, user=user1, text='Комментарий ко второй статье')
comment4 = Comment.objects.create(post=news1, user=user2, text='Комментарий к первой новости')

# Применение лайков и дизлайков
post1.like()
post1.like()
post1.dislike()

comment1.like()
comment2.like()
comment3.dislike()
comment4.like()
comment4.dislike()
comment4.dislike()

# Обновление рейтинга авторов
author1.update_rating()
author2.update_rating()

top_author = Author.objects.order_by('-rating').first()
print(f'Лучший пользователь: {top_author.user.username}, рейтинг: {top_author.rating}')


top_post = Post.objects.order_by('-rating').first()
print(f'Дата: {top_post.created_at}, Имя автора: {top_post.author.user.username}, Рейтинг: {top_post.rating}, Заголовок: {top_post.title}')
print(f'Предварительный просмотр: {top_post.preview()}')

comments = Comment.objects.filter(post=top_post)
for comment in comments:
    print(f'Дата: {comment.created_at}, Пользователь: {comment.user.username}, Рейтинг: {comment.rating}, Текст: {comment.text}')