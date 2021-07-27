# Урок №3 курса [Знакомство с Django: ORM](https://dvmn.org/modules/django-orm/)

Это учебный проект, состоящий из [скрипта](https://github.com/ArtsAnton/devman_orm_3/blob/main/scripts.py) предназначенного для внесения изменений в учебную БД с помощью Django ORM. Скрпит работает совместно с [репозиторием](https://github.com/devmanorg/e-diary/tree/master).  

[Скрипт - scripts.py](https://github.com/ArtsAnton/devman_orm_3/blob/main/scripts.py) состоит из трех функций:
1. [fix_marks(schoolkid)](https://github.com/ArtsAnton/devman_orm_3/blob/main/scripts.py#L9-L13) - принимает экземпляр класса [ученика](https://github.com/devmanorg/e-diary/blob/master/datacenter/models.py#L4-L14) и заменяет оценки ниже 4 баллов на 5 в таблице БД- [class Mark](https://github.com/devmanorg/e-diary/blob/master/datacenter/models.py#L72-L96);
2. [remove_chastisements(schoolkid)](https://github.com/ArtsAnton/devman_orm_3/blob/main/scripts.py#L16-L18) - принимает экземпляр класса [ученика](https://github.com/devmanorg/e-diary/blob/master/datacenter/models.py#L4-L14) и удаляет замечания, полученные учеником за все время учебы из таблицы БД - [class Chastisement](https://github.com/devmanorg/e-diary/blob/master/datacenter/models.py#L102-L119);
3. [create_commendation(name, subject)](https://github.com/ArtsAnton/devman_orm_3/blob/main/scripts.py#L21-L37) - принимает имя ученика, название школьного предмета и создает положительный отзыв об ученике по результатам последнего проведенного урока - [table Commendation](https://github.com/devmanorg/e-diary/blob/master/datacenter/models.py#L125-L145).

### Цель проекта

Код написан в образовательных целях в рамках выполнения урока № 3 онлайн-курса для веб-разработчиков [devmn.org](https://dvmn.org/modules/django-orm/).
