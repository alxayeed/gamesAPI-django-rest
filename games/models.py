from django.db import models


class GameCatagory(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)

    def __str__(self, name):
        return self.name


class Games(models.Model):
    name = models.CharField(max_length=200, blank=True, default="")
    catagory = models.ForeignKey(GameCatagory,
                                 related_name='games',
                                 on_delete=models.CASCADE)
    played = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    release_date = models.DateTimeField(auto_now_add=True)


class Player(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'male'),
        (FEMALE, 'female')
    )
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, blank=False, default='')
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        default=MALE
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class PlayerScore(models.Model):
    player = models.ForeignKey(Player,
                               related_name='scores',
                               on_delete=models.CASCADE)
    game = models.ForeignKey(Games,
                             on_delete=models.CASCADE)
    score = models.IntegerField()
    score_date = models.DateTimeField()
