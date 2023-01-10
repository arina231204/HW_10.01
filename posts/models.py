from django.db import models
from accounts.models import Profile

class AbstractPost(models.Model):
    name = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Like(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tweet = models.ForeignKey('Tweet', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Tweet(AbstractPost):
    def __str__(self):
        return f'Tweet {self.id} by {self.profile.user.username}'

    # def has_like_from_user(self, user):
    #     return self.like_set.filter(user=user).exists()

class Comment(AbstractPost):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)

    def __str__(self):
        return f'Tweet {self.id} by {self.profile.user.username} to {self.tweet.id}'

class StatusType(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class StatusTweet(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.SET_DEFAULT, default=1)
    type = models.ForeignKey(StatusType, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['tweet', 'profile', ]

    def __str__(self):
        return f'{self.tweet.id} - {self.profile} - {self.type}'

class StatusComment(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.SET_DEFAULT, default=1)
    type = models.ForeignKey(StatusType, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['tweet', 'profile', ]

    def __str__(self):
        return f'{self.comment.id} - {self.profile} - {self.type}'

