from django.db import models


class InternshipRegistration(models.Model):

    INTERNSHIP_CHOICES = [
        ('Online', 'Online'),
        ('Offline', 'Offline'),
    ]

    STATE_CHOICES = [
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Goa', 'Goa'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jharkhand', 'Jharkhand'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Manipur', 'Manipur'),
        ('Meghalaya', 'Meghalaya'),
        ('Mizoram', 'Mizoram'),
        ('Nagaland', 'Nagaland'),
        ('Odisha', 'Odisha'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Sikkim', 'Sikkim'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Tripura', 'Tripura'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttarakhand', 'Uttarakhand'),
        ('West Bengal', 'West Bengal'),
    ]

    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    aadhaar_number = models.CharField(max_length=12)

    state = models.CharField(
        max_length=50,
        choices=STATE_CHOICES
    )

    university_name = models.CharField(max_length=200)
    college_name = models.CharField(max_length=200)

    course = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)

    internship_type = models.CharField(
        max_length=10,
        choices=INTERNSHIP_CHOICES
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.course_name


class Event(models.Model):
    title = models.CharField(max_length=200)
    event_date = models.DateField()
    mode = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name