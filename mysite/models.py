from django.db import models

# Create your models here.
class Article(models.Model):
    class Meta:
        db_table = 'article'

    title = models.CharField(verbose_name='タイトル', max_length=255, null=False)
    url = models.CharField(verbose_name='URL', max_length=255, null=False)
    classification = models.CharField(verbose_name='分類', max_length=255, null=True, blank=True)
    text = models.CharField(verbose_name='内容', max_length=255, null=True, blank=True)
    primaryNum = models.IntegerField(verbose_name='優先度', null=False)
    updateTime = models.DateTimeField(verbose_name='更新日時', null=False)
    util = models.CharField(verbose_name='予備', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

# class Heading(models.Model):
#     class Meta:
#         db_table = 'heading'
#
#     heading = models.CharField(verbose_name='見出し', max_length=255)
#     article = models.ForeignKey(Article, verbose_name='タイトル',on_delete=models.CASCADE)

class Question(models.Model):
    class Meta:
        db_table = 'question'

    text = models.CharField(verbose_name='問い合わせ', max_length=255, null=False)
    updateTime = models.DateTimeField(verbose_name='問い合わせ日時', null=False)

    def __str__(self):
        return self.text