from django.db import models
import uuid

class Applied_users(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.TextField()
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=15)
    education = models.CharField(max_length=30)
    program_experience = models.CharField(max_length=20)
    need_to_join = models.TextField()
    carrier_goals = models.TextField()
    referral_code = models.CharField(max_length=15)
    payment_screenshot = models.TextField()
    create_refer = models.CharField(max_length=20, editable=False, blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, db_index=True)


    def save(self, *args, **kwargs):
        if not self.create_refer:
            last_user = Applied_users.objects.order_by('-created_at').first()
            if last_user and last_user.create_refer:
                last_number = int(last_user.create_refer[4:9])
            else:
                last_number = 0
            self.create_refer = f'TECH{last_number + 1:05d}REF'
        super().save(*args, **kwargs)


class ContactForm(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.TextField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, db_index=True)