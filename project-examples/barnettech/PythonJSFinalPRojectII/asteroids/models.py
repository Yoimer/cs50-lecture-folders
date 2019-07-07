from django.db import models

# Model to hold highscores.
class Highscore(models.Model):
    """
    Model to hold the users highscores.
    """
    username = models.CharField(max_length=200)
    besttime = models.IntegerField(default=0)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.username