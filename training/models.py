from django.db import models
from registration.models import User
from courses.models import Course


class Training(models.Model):
    participant_choice = (
        ('individual', 'individual'),
        ('group', 'group'),
        ('business', 'business'),
    )
    user = models.ForeignKey(User)
    course = models.ForeignKey(Course)
    participant = models.CharField(max_length=50, choices=participant_choice, default='individual')
    date = models.DateField(default=None)
    payment_method = models.CharField(max_length=30)
    coupon = models.CharField(max_length=20)
    is_send = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def course_title(self):
        return self.course.title
