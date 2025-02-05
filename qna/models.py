from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Issue(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_solved = models.BooleanField(default=False)
    tags = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title
    
class Reply(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='replies')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    def __str__(self):
        return f"Reply by {self.author.username} on {self.issue.title}"
    
class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=10, choices=[('up', 'Upvote'), ('down', 'Downvote')])

    class Meta:
        unique_together = ('user', 'reply')  # ensure a user can only vote once per reply

    def __str__(self):
        return f"{self.user.username} voted {self.vote_type} on {self.reply}"